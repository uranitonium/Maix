from Maix import FPIOA, GPIO
from board import board_info
import utime, lcd, image, sensor
import KPU as kpu

fpioa = FPIOA()
fpioa.set_function(board_info.BOOT_KEY, FPIOA.GPIOHS0)
boot_key = GPIO(GPIO.GPIOHS0, GPIO.IN)

class_num = 3
sample_num = 15
THRESHOLD = 11
class_names = ['class1', 'class2', 'class3']
cap_num = 0
train_status = 0

def draw(img, x, y, text, color, scale, bg=None):
    if bg:
        img.draw_rectangle(x-2, y-2, len(text)*8*scale+4, 16*scale, fill=True, color=bg)

    img = img.draw_string(x, y, text, color=color, scale=scale)
    return img

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224,224))
lcd.init()

model = kpu.load(0x300000)
classifier = kpu.classifier(model, class_num, sample_num)

def capture_image(pin_num):
    global cap_num
    global train_status
    global img
    if cap_num < class_num:
        index = classifier.add_class_img(img)
        cap_num += 1
        print("add class img: ", index)
    else:
        index = classifier.add_sample_img(img)
        cap_num += 1
        print("add sample img: ", index)
    if cap_num >= class_num + sample_num:
        print("start train"),
        img = draw(img, 30, 100, "training", color=lcd.WHITE, scale=2, bg=lcd.RED)
        lcd.display(img)
        classifier.train()
        print("train end")
        train_status = 1
    utime.sleep_ms(50)

boot_key.irq(capture_image, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT)

while True:
    img = sensor.snapshot()
    if train_status == 0:
        if cap_num < class_num:
            img = draw(img, 0, 200, "press boot key to cap " + class_names[cap_num],
                       color=lcd.WHITE, scale=1, bg=lcd.RED)
        elif cap_num < class_num + sample_num:
            img = draw(img, 0, 200, "boot key to cap sample " + str (cap_num-class_num),
                       color=lcd.WHITE, scale=1, bg=lcd.RED)

    else:
        res_index = -1
        res_index, min_dist = classifier.predict(img)
        print(min_dist)

        if res_index >= 0 and min_dist < THRESHOLD :
            print ("predict result:", class_names[res_index])
            img = draw(img, 2, 2, str(class_names[res_index]),
            color=lcd.WHITE, scale=2, bg=lcd.RED)
        else:
            print ("unknown, maybe:", class_names[res_index])
            img = draw(img, 2, 2, 'maybe' + str(class_names[res_index]),
            color=lcd.WHITE, scale=2, bg=lcd.RED)

    lcd.display(img)



#from Maix import FPIOA, GPIO
#from board import board_info
#import utime, lcd, image, sensor
#import KPU as kpu

#task_fd = kpu.load(0x300000)
#task_ld = kpu.load(0x400000)
#task_fe = kpu.load(0x500000)

#anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
#kpu.init_yolo2(task_fd, 0.5, 0.3, 5, anchor)

#fpioa = FPIOA()
#fpioa.set_function(board_info.BOOT_KEY, FPIOA.GPIOHS0)
#boot_key = GPIO(GPIO.GPIOHS0, GPIO.IN)

#start_processing = False
#def set_key_state(pin_num):
    #global start_processing
    #start_processing = True
    #utime.sleep_ms(50)
    #print('Boot Key Pressed')

#boot_key.irq(set_key_state, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT)

#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#img_face = image.Image(size = (128,128))
#img_face.pix_to_ai()

#face_points = [(44, 59), (84, 59),
#(64, 82), (47, 105), (81, 105) ]
#names = ['Person 1', 'Person 2', 'Person 3',
#'Person 4', 'Person 5', 'Person 6']
#record_ftr = []
#record_ftrs = []


#while True:
    #img = sensor.snapshot()
    #faces = kpu.run_yolo2(task_fd, img)

    #if faces:
        #face = faces[0]
        #del faces
        #img.draw_rectangle(face.rect())
        #face_cut = img.cut(face.x(), face.y(), face.w(), face.h())
        #face_cut_128 = face_cut.resize(128, 128)
        #face_cut_128.pix_to_ai()

        #fmap = kpu.forward(task_ld, face_cut_128)
        #plist = fmap[:]
        #kpu.fmap_free(fmap)
        #del fmap
        #left_eye = (face.x() + int(plist[0] * face.w() - 10), face.y() + int(plist[1] * face.h()))
        #right_eye = (face.x() + int(plist[2] * face.w()), face.y() + int(plist[3] * face.h()))
        #nose = (face.x() + int(plist[4] * face.w()), face.y() + int(plist[5] * face.h()))
        #left_mouse = (face.x() + int(plist[6] * face.w()), face.y() + int(plist[7] * face.h()))
        #right_mouse = (face.x() + int(plist[8] * face.w()), face.y() + int(plist[9] * face.h()))

        #img.draw_circle(left_eye[0], left_eye[1], 4)
        #img.draw_circle(right_eye[0], right_eye[1], 4)
        #img.draw_circle(nose[0], nose[1], 4)
        #img.draw_circle(left_mouse[0], left_mouse[1], 4)
        #img.draw_circle(right_mouse[0], right_mouse[1], 4)
        #src_point = [left_eye, right_eye, nose, left_mouse, right_mouse]
        #T = image.get_affine_transform(src_point, face_points)
        #image.warp_affine_ai(img, img_face, T)
        #img_face.ai_to_pix()

        #del left_eye
        #del right_eye
        #del nose
        #del left_mouse
        #del right_mouse
        #del T
        #del src_point
        #del face_cut
        #del face_cut_128

        #fmap = kpu.forward(task_fe, img_face)
        #feature = kpu.face_encode(fmap[:])
        #kpu.fmap_free(fmap)
        #del fmap

        #scores = []
        #for j in range(len(record_ftrs)):
            #score = kpu.face_compare(record_ftrs[j], feature)
            #scores.append(score)

        #max_score = 0
        #index = 0

        #for k in range(len(scores)):
            #if max_score < scores[k]:
                #max_score = scores[k]
                #index = k

        #del scores

        #if max_score > 85: # ACCURACY
            #img.draw_string(face.x(), face.y(), ("%s :%2.1f" % (names[index], max_score)), color=(0, 255, 0), scale=2)
        #else:
            #img.draw_string(face.x(), face.y(), ("Unknown :%2.1f" % (max_score)), color=(255, 0, 0), scale=2)


        #if start_processing:
            #record_ftr = feature
            #record_ftrs.append(record_ftr)
            #start_processing = False

    #lcd.display(img)
    #del img
