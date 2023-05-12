#import KPU as kpu
#import lcd, image, sensor, utime
#lcd.init()
#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.set_windowing((224,224))
#sensor.skip_frames()
#red = [255,0,0]
#green = [0,255,0]
#black = [0,0,0]
#with open("/sd/labels.txt") as f:
        #labels = f.readlines()
#model = kpu.load(0x500000)
#def remove_values_from_list(the_list, val):
   #return [value for value in the_list if value > val]
#while True:
    #img = sensor.snapshot()
    #fmap = kpu.forward(model, img)
    #plist = fmap[:]
    #pmax = max(plist)
    #max_index = plist.index(pmax)
    #x = remove_values_from_list(plist, 0.1)
    #intx = int(x)
    #print(x)
    #print(str(pmax))
    #print(str(max_index))
    #object_name = labels[max_index].strip()
    #lessobject_name = labels[x].strip()
    #print(object_name)
    #print(lessobject_name)
    #img.draw_string(0,0,object_name, scale = 1, color = green)
    #lcd.display(img)

#import KPU as kpu
#import lcd, image, sensor
#import math
#lcd.init()
#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time=3000)
#model = kpu.load(0x800000)
#anchor = (1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52)
#kpu.init_yolo2(model, 0.5, 0.2, 5, anchor)
#classes = ['airplane', 'bicycle', 'bird',
           #'boat', 'bottle', 'bus', 'car',
           #'cat', 'chair', 'cow', 'dining table',
           #'dog', 'horse', 'motor bike',
           #'person', 'potted plant', 'sheep',
           #'sofa', 'train', 'TV monitor']
#red = [255,0,0]
#green = [0,255,0]
#black = [0,0,0]
#while True:
    #img = sensor.snapshot()

    #objects = kpu.run_yolo2(model, img)
    #if objects:
        #for obj in objects:
            #prob = math.trunc(obj.value()*100)
            #img.draw_rectangle(obj.rect(), color = green, thickness=3)
            #img.draw_string(obj.x(), obj.y()-25, str(classes[obj.classid()]).upper(), color = green, scale = 2)
            #img.draw_string(obj.x()+200, obj.y()-25, str(prob)+"%", color = green, scale = 2)
    #lcd.display(img)

#import sensor, image, utime, lcd, re
#import KPU as kpu

#model = kpu.load(0x300000)
#print(model)
#anchors = (0.1606, 0.3562, 0.4712, 0.9568, 0.9877, 1.9108, 1.8761, 3.5310, 3.4423, 5.6823)
#kpu.init_yolo2(model, 0.5, 0.2, 5, anchors)

#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time=10000)
#red = [255,0,0]
#green = [0,255,0]
#black = [0,0,0]
#while True:
    #img = sensor.snapshot()

    #objects = kpu.run_yolo2(model, img)
    #if objects:
        #for i in range(len(objects)):
            #if objects[i].classid()==1:
                #img.draw_rectangle(objects[i].rect(), color = green, thickness=3)
                #img.draw_string(objects[i].x(), objects[i].y()-25, "MASK", color = green, scale = 2)
                #print("Found Mask")
            #else:
                #img.draw_string(objects[i].x(), objects[i].y()-25, "NO MASK", color = red, scale = 2)
                #img.draw_rectangle(objects[i].rect(), color = red, thickness=3)
                #print("Found Face")

    #lcd.display(img)

#import sensor, image, utime, lcd
#import KPU as kpu

#model = kpu.load(0x300000)
#print(model)
#anchors = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
#kpu.init_yolo2(model, 0.5, 0.3, 5, anchors)

#lcd.init()
#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time=10000)

#while True:
    #img = sensor.snapshot()

    #objects = kpu.run_yolo2(model, img)
    #if objects:
        #for i in range(len(objects)):
            #img.draw_string(objects[i].x(), objects[i].y()-15, str(objects[i].value()*100)+'%', color = [255,0,0])
            #img.draw_rectangle(objects[i].rect(), color = [255,0,0], thickness=3)

    #lcd.display(img)
    #print(objects)

#import time
#from Maix import GPIO, I2S
#from fpioa_manager import fm

## user setting
#sample_rate   = 16000
#record_time   = 4  #s

#fm.register(20,fm.fpioa.I2S0_IN_D0, force=True)
#fm.register(30,fm.fpioa.I2S0_WS, force=True)
#fm.register(32,fm.fpioa.I2S0_SCLK, force=True)

#rx = I2S(I2S.DEVICE_0)
#rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode=I2S.STANDARD_MODE)
#rx.set_sample_rate(sample_rate)
#print(rx)

#from speech_recognizer import asr

#class maix_asr(asr):

    #asr_vocab = ["lv", "shi", "yang", "chun", "yan", "jing", "da", "kuai", "wen", "zhang", "de", \
      #"di", "se", "si", "yue", "lin", "luan", "geng", "xian", "huo", "xiu", "mei", "yi", "ang", "ran", \
      #"ta", "jin", "ping", "yao", "bu", "li", "liang", "zai", "yong", "dao", "shang", "xia", "fan", \
      #"teng", "dong", "she", "xing", "zhuang", "ru", "hai", "tun", "zhi", "tou", "you", "ling", "pao", \
      #"hao", "le", "zha", "zen", "me", "zheng", "cai", "ya", "shu", "tuo", "qu", "fu", "guang", "bang", \
      #"zi", "chong", "shui", "cuan", "ke", "shei", "wan", "hou", "zhao", "jian", "zuo", "cu", "hei", \
      #"yu", "ce", "ming", "dui", "cheng", "men", "wo", "bei", "dai", "zhe", "hu", "jiao", "pang", "ji", \
      #"lao", "nong", "kang", "yuan", "chao", "hui", "xiang", "bing", "qi", "chang", "nian", "jia", "tu", \
      #"bi", "pin", "xi", "zou", "chu", "cun", "wang", "na", "ge", "an", "ning", "tian", "xiao", "zhong", \
      #"shen", "nan", "er", "ri", "zhu", "xin", "wai", "luo", "gang", "qing", "xun", "te", "cong", "gan", \
      #"lai", "he", "dan", "wei", "die", "kai", "ci", "gu", "neng", "ba", "bao", "xue", "shuai", "dou", \
      #"cao", "mao", "bo", "zhou", "lie", "qie", "ju", "chuan", "guo", "lan", "ni", "tang", "ban", "su", \
      #"quan", "huan", "ying", "a", "min", "meng", "wu", "tai", "hua", "xie", "pai", "huang", "gua", \
      #"jiang", "pian", "ma", "jie", "wa", "san", "ka", "zong", "nv", "gao", "ye", "biao", "bie", "zui", \
      #"ren", "jun", "duo", "ze", "tan", "mu", "gui", "qiu", "bai", "sang", "jiu", "yin", "huai", "rang", \
      #"zan", "shuo", "sha", "ben", "yun", "la", "cuo", "hang", "ha", "tuan", "gong", "shan", "ai", "kou", \
      #"zhen", "qiong", "ding", "dang", "que", "weng", "qian", "feng", "jue", "zhuan", "ceng", "zu", \
      #"bian", "nei", "sheng", "chan", "zao", "fang", "qin", "e", "lian", "fa", "lu", "sun", "xu", "deng", \
      #"guan", "shou", "mo", "zhan", "po", "pi", "gun", "shuang", "qiang", "kao", "hong", "kan", "dian", \
      #"kong", "pei", "tong", "ting", "zang", "kuang", "reng", "ti", "pan", "heng", "chi", "lun", "kun", \
      #"han", "lei", "zuan", "man", "sen", "duan", "leng", "sui", "gai", "ga", "fou", "kuo", "ou", "suo", \
      #"sou", "nu", "du", "mian", "chou", "hen", "kua", "shao", "rou", "xuan", "can", "sai", "dun", "niao", \
      #"chui", "chen", "hun", "peng", "fen", "cang", "gen", "shua", "chuo", "shun", "cha", "gou", "mai", \
      #"liu", "diao", "tao", "niu", "mi", "chai", "long", "guai", "xiong", "mou", "rong", "ku", "song", \
      #"che", "sao", "piao", "pu", "tui", "lang", "chuang", "keng", "liao", "miao", "zhui", "nai", "lou", \
      #"bin", "juan", "zhua", "run", "zeng", "ao", "re", "pa", "qun", "lia", "cou", "tie", "zhai", "kuan", \
      #"kui", "cui", "mie", "fei", "tiao", "nuo", "gei", "ca", "zhun", "nie", "mang", "zhuo", "pen", "zun", \
      #"niang", "suan", "nao", "ruan", "qiao", "fo", "rui", "rao", "ruo", "zei", "en", "za", "diu", "nve", \
      #"sa", "nin", "shai", "nen", "ken", "chuai", "shuan", "beng", "ne", "lve", "qia", "jiong", "pie", \
      #"seng", "nuan", "nang", "miu", "pou", "cen", "dia", "o", "zhuai", "yo", "dei", "n", "ei", "nou", "bia", "eng", "den", "_"]

    #def get_asr_list(string='xiao-ai-fas-tong-xue'):
        #return [__class__.asr_vocab.index(t) for t in string.split('-') if t in __class__.asr_vocab]

    #def get_asr_string(listobj=[117, 214, 257, 144]):
        #return '-'.join([__class__.asr_vocab[t] for t in listobj if t < len(__class__.asr_vocab)])

    #def config(self, sets):
        #self.set([(sets[key], __class__.get_asr_list(key)) for key in sets])

    #def recognize(self):
        #res = self.result()
        ## print(tmp)
        #if res != None:
            #sets = {}
            #for tmp in res:
                #sets[__class__.get_asr_string(tmp[1])] = tmp[0]
            #return sets
        #return None

#from machine import Timer

#def on_timer(timer):
    #timer.callback_arg().state()

## configure asr and timer
#t = maix_asr(0x500000, I2S.DEVICE_0, 3, shift=0) # maix bit set shift=1
#tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=64, callback=on_timer, arg=t)

#t.config({
    #'jia-na-da' : 0.5,
    #'ni-hao' : 0.5,
    #'xie-xie' : 0.5,
    #'wan-shang-hao': 0.5,
    #'zai-jian': 0.5,
    #'zao-shang-hao': 0.5
#})

#print(t.get())

#while True:
    ##time.sleep(1)
    #tmp = t.recognize()
    ##print(tmp)
    #if tmp != None:
        #print(tmp)

#from Maix import GPIO, I2S
#from fpioa_manager import fm
#import utime

#fm.register(20,fm.fpioa.I2S0_IN_D0, force=True)
#fm.register(32,fm.fpioa.I2S0_SCLK, force=True)
#fm.register(30,fm.fpioa.I2S0_WS, force=True)

#rx = I2S(I2S.DEVICE_0)
#rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
#rx.set_sample_rate(16000)
#print(rx)

#from speech_recognizer import isolated_word

#sr = isolated_word(dmac=2, i2s=I2S.DEVICE_0,size=10,shift=0)
#print(sr.size())
#print(sr)

#sr.set_threshold(0,0,10000)

#while True:
    #utime.sleep_ms(100)
    #print(sr.state())
    #if sr.Done == sr.record(0):
        #data = sr.get(0)
        #print(data)
        #break
    #if sr.Speak == sr.state():
        #print("Vocalize A")
#sr.set(1,data)

#while True:
    #utime.sleep_ms(100)
    #print(sr.state())
    #if sr.Done == sr.record(2):
        #data = sr.get(2)
        #print(data)
        #break
    #if sr.Speak == sr.state():
        #print("Vocalize B")
#sr.set(3,data)

#while True:
    #utime.sleep_ms(200)
    #if sr.Done == sr.recognize():
            #res = sr.result()
            #if res != None:
                #if res[0] == 0:
                    #print(str(res[0]))
                    #print("You Said A")
                #if res[0] == 2:
                    #print("You Said B")

#from Maix import GPIO, I2S
#from fpioa_manager import fm
#import image, lcd, time
#import audio

#fm.register(20,fm.fpioa.I2S0_IN_D0)
#fm.register(19,fm.fpioa.I2S0_WS)
#fm.register(18,fm.fpioa.I2S0_SCLK)

#rx = I2S(I2S.DEVICE_0)
#rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
#rx.set_sample_rate(16000)
#print(rx)

#from speech_recognizer import isolated_word

#sr = isolated_word(dmac=2, i2s=I2S.DEVICE_0,size=10,shift=0)
#print(sr.size())
#print(sr)

#sr.set_threshold(0,0,10000)

#from fpioa_manager import fm

#sample_rate = 38640
#sample_points = 1024
#fft_points = 512
#hist_x_num = 50

#lcd.init(freq=15000000)

#fm.register(20,fm.fpioa.I2S0_IN_D0)
#fm.register(19,fm.fpioa.I2S0_WS)
#fm.register(18,fm.fpioa.I2S0_SCLK)
#fm.register(34,fm.fpioa.I2S2_OUT_D1)
#fm.register(35,fm.fpioa.I2S2_SCLK)
#fm.register(33,fm.fpioa.I2S2_WS)

#rx = I2S(I2S.DEVICE_0)
#rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
#rx.set_sample_rate(sample_rate)
#img = image.Image()

#if hist_x_num > 320:
    #hist_x_num = 320

#hist_width = int(320 / hist_x_num)
#x_shift = 0

#while True:
    #audio = rx.record(sample_points)
    #fft_res = FFT.run(audio.to_bytes(),fft_points)
    #fft_amp = FFT.amplitude(fft_res)
    #img = img.clear()
    #x_shift = 0

    #for i in range(hist_x_num):
        #if fft_amp[i] > 240:
            #hist_height = 240
        #else:
            #hist_height = fft_amp[i]

        #img = img.draw_rectangle((x_shift,240-hist_height,hist_width,hist_height),[0,255,255],2,True)
        #x_shift = x_shift + hist_width

    #lcd.display(img)
    #fft_amp.clear()

#import image, lcd, time
#import audio
#from Maix import GPIO, I2S
#from fpioa_manager import fm

## user setting
#sample_rate   = 16000
#record_time   = 10  #10 seconds
## default seting
#sample_points = 2048
#wav_ch        = 2

#fm.register(8, fm.fpioa.GPIO0, force=True)
#wifi_en = GPIO(GPIO.GPIO0, GPIO.OUT)
#wifi_en.value(0)

#fm.register(20,fm.fpioa.I2S0_IN_D0, force=True)
#fm.register(19,fm.fpioa.I2S0_WS, force=True)
#fm.register(18,fm.fpioa.I2S0_SCLK, force=True)

#rx = I2S(I2S.DEVICE_0)
#rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode=I2S.STANDARD_MODE)
#rx.set_sample_rate(sample_rate)
#print(rx)

## init audio
#recorder = audio.Audio(path="/sd/record.wav", is_create=True, samplerate=sample_rate)

#queue = []

#frame_cnt = record_time*sample_rate     //sample_points

#for i in range(frame_cnt):
    #tmp = rx.record(sample_points*wav_ch)
    #if len(queue) > 0:
        #ret = recorder.record(queue[0])
        #queue.pop(0)
    #rx.wait_record()
    #queue.append(tmp)
    #print(str(i) + ":" + str(time.ticks()))

#recorder.finish()

#import image,lcd,time
#import audio
#from Maix import I2S, GPIO
#from fpioa_manager import fm

#sample_rate = 16000
#record_time = 10

#sample_points = 2048
#wav_ch = 2

#fm.register(8, fm.fpioa.GPIO0, force=True)
#wifi_en = GPIO(GPIO.GPIO0, GPIO.OUT)
#wifi_en.value(0)

#fm.register(20,fm.fpioa.I2S0_IN_D0)
#fm.register(19,fm.fpioa.I2S0_WS)
#fm.register(18,fm.fpioa.I2S0_SCLK)

#rx = I2S(I2S.DEVICE_0)
#rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
#rx.set_sample_rate(sample_rate)
#print(rx)

#recorder=audio.Audio(path="/sd/record.wav", is_create=True, samplerate=sample_rate)

#queue = []

#frame_cnt = record_time*sample_rate

#for i in range(frame_cnt):
    #tmp = rx.record(sample_points*wav_ch)
    #if len(queue) > 0:
        #ret = recorder.record(queue[0])
        #queue.pop(0)
    #rx.wait_record()
    #queue.append(tmp)
    #print(str(i) + ":" + str(time.ticks()))

#record.finish()

#from Maix import I2S
#import time
#from fpioa_manager import fm

#fm.register(20,fm.fpioa.I2S0_IN_D0)
#fm.register(19,fm.fpioa.I2S0_WS)
#fm.register(18,fm.fpioa.I2S0_SCLK)
#fm.register(34,fm.fpioa.I2S2_OUT_D1)
#fm.register(35,fm.fpioa.I2S2_SCLK)
#fm.register(33,fm.fpioa.I2S2_WS)

#sample_rate = 44*1000

#rx = I2S(I2S.DEVICE_0)
#rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
#rx.set_sample_rate(sample_rate)

#while True:
    #audio = rx.record(256)
    #print(audio)

#from Maix import MIC_ARRAY as mic
#import lcd

#lcd.init()
#mic.init()

#b = [0,0,0,0,0,0,0,0,0,0,0,0]
#index = 0
#while True:
    #imga = mic.get_map()
    #b = mic.get_dir(imga)
    #mic.set_led(b, (255,0,0))
    #imgb = imga.resize(160,160)
    #lcd

#mic.deinit()

#from Maix import MIC_ARRAY as mic
#import lcd

#lcd.init()
#mic.init()

#while True:
    #imga = mic.get_map()
    #b = mic.get_dir(imga)
    #mic.set_led(b, (0,255,0))
    #imgb = imga.resize(160,160)
    #imgc = imgb.to_rainbow(1)
    #lcd.display(imgc)

#mic.deinit()

#import nes, lcd

#lcd.init(freq=15000000)
#nes.init(nes.KEYBOARD)
#nes.load("/sd/Super Mario Bros (E).nes")

#while True:
    #nes.loop()

#class Person:
    #def __init__(self,name,money):
        #self.name=name
        #self.money=money
    #def getmoney(self,amount):
        #self.money=self.money + amount
    #def losemoney(self,amount):
        #self.money=self.money - amount
    #def checkmoney(self):
        #print(self.money)

#per1 = Person("John",30)
#per1.losemoney(20)
#per1.checkmoney()
#per1.getmoney(50)
#per1.checkmoney()

#class Student:
    #def __init__(self,name,age,grade):
        #self.name = name
        #self.age = age
        #self.grade = grade

    #def hello(self):
        #print("Hi, my name is " + self.name)
        #print("I am " + self.age)
        #print("I am in " + grade + " grade")

#stu1 = Student("Bob", 11, "6th")
#stu2 = Student("Eric", 9, "4th")
#stu1.hello()
#stu2.hello()
#from machine import Timer
#import utime

#def on_timer(timer):
    #timer.callback_arg()
    #print(timer.callback_arg())

#tim = Timer(Timer.TIMER0,Timer.CHANNEL0,mode=Timer.MODE_PERIODIC,period=1000,unit=Timer.UNIT_MS,callback=on_timer,arg="Hello",start=True,priority=1, div=0)
#utime.sleep_ms(5500)
#tim.stop()
#print("Stopped")
#utime.sleep_ms(5500)
#tim.restart()
#print("Restarted")
#utime.sleep_ms(5500)
#tim.stop()
#del tim
#print("Deleted")

#from machine import WDT
#import utime

#def on_wdt0(self):
    #print("Watchdog 1 is angry")
#def on_wdt1(self):
    #print("Watchdog 2 is angry")

#wdt0 = WDT(id = 0, timeout = 3000, callback = on_wdt0, context={})
#wdt1 = WDT(id = 1, timeout = 5000, callback = on_wdt1, context={})

#utime.sleep_ms(2500)
#wdt0.feed()
#wdt1.feed()

#from machine import WDT
#import lcd, utime
#from Maix import GPIO
#from Maix import FPIOA
#from board import board_info

#fpioa = FPIOA()
#fpioa.set_function(board_info.BOOT_KEY, fpioa.GPIOHS0)
#key = GPIO(GPIO.GPIOHS0,GPIO.IN)

#lcd.init()

#def on_wdt(self):
    #print("Boot key stopped")

#wdt0 = WDT(id = 0, timeout = 5000, callback = on_wdt, context={})

#while True:
    #if key.value()==0:
        #wdt0.feed()



#from machine import WDT
#import lcd, utime

#lcd.init()

#def on_wdt(self):
    #print("Hello")
    #lcd.draw_string(0, 0, "Hello")
    #utime.sleep(2)

#wdt0 = WDT(id = 0, timeout = 3000, callback = on_wdt, context={})


#import sensor, image, lcd, utime
#from Maix import GPIO
#from Maix import FPIOA
#from board import board_info

#fpioa = FPIOA()
#fpioa.set_function(board_info.BOOT_KEY, fpioa.GPIOHS0)
#key = GPIO(GPIO.GPIOHS0,GPIO.IN)

#lcd.init()
#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time=2000)

#x = False
#y = 0
#z = False

#while z == False:
    #img = sensor.snapshot()
    #qrcode_list = img.find_qrcodes()
    #lcd.display(img)
    #lcd.draw_string(0,0,"Go scan the QR code!")
    #if len(qrcode_list) != 0:
        #print("Found QR Code")
        #for i in range(len(qrcode_list)):
            #a = qrcode_list[i].payload()
            #print(a)
            #lcd.display(img)
            #utime.sleep(3)
            #if a != "Good Job! You completed the first part of the task.":
                #z = False
            #if a == "Good Job! You completed the first part of the task.":
                #z = True

#while x == False:
    #if key.value() == 0:
        #if y > 0:
            #img2 = sensor.snapshot()
            #img2.save("/flash/img2.jpg")
            #lcd.display(img2)
            #utime.sleep(2)
            #x = True
        #if y <= 0:
            #img1 = sensor.snapshot()
            #img1.save("/flash/img1.jpg")
            #lcd.display(img1)
            #utime.sleep(2)
            #y = y + 1
    #if key.value() == 1:
        #img = sensor.snapshot()
        #lcd.display(img)
        #lcd.draw_string(0,0,"Go take a picture of a laptop")
        #lcd.draw_string(0,15," and a keyboard.")
        #lcd.draw_string(0,30,"To take a picture, Press the boot key!")

#if x == True:
    #img1_read = image.Image("/flash/img1.jpg")
    #img2_read = image.Image("/flash/img2.jpg")
    #lcd.display(img1_read)
    #lcd.draw_string(0,0,"This is a laptop")
    #utime.sleep(2)
    #lcd.display(img2_read)
    #lcd.draw_string(0,0,"This is a keyboard")
    #utime.sleep(2)
    #lcd.draw_string(0,0,"If you got the right pictures,")
    #lcd.draw_string(0,15,"then Congratulations!")
    #print("If you got the right pictures, then Congratulations!")



#while True:
    #img = sensor.snapshot()
    #qrcode_list = img.find_qrcodes()
    #lcd.display(img)

    #if len(qrcode_list) != 0:
        #print("Found QR Code")
        #for i in range(len(qrcode_list)):
            #print(qrcode_list[i].payload())

            #lcd.display(img)


#import sensor, image, lcd
#from Maix import GPIO
#from Maix import FPIOA
#from board import board_info

#fpioa = FPIOA()
#fpioa.set_function(board_info.BOOT_KEY, fpioa.GPIOHS0)
#key = GPIO(GPIO.GPIOHS0,GPIO.IN)

#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(5000)

#x = False
#y = 0

#while x == False:
    #if key.value() == 0:
        #print("Boot Key Pressed")
        #if y > 0:
            #img2 = sensor.snapshot()
            #img2.save("/sd/img2.jpg")
            #lcd.display(img2)
            #utime.sleep(2)
            #x = True
        #if y <= 0:
            #img1 = sensor.snapshot()
            #img1.save("/sd/img1.jpg")
            #lcd.display(img1)
            #utime.sleep(2)
            #y = y + 1
    #if key.value() == 1:
        #print(y)
        #print(x)
        #img = sensor.snapshot()
        #icd.display(img)
#if x == True:
    #print("Congratulations")



#v = video.open("/sd/myVideo.avi", record = True, interval = 50000, quality = 80)
#for i in range(100):
    #img = sensor.snapshot()
    #v.record(img)
#v.record_finish()

#lcd.init()

#v = video.open("/sd/myVideo.avi")
#print(v)
#while True:
    #if v.play() == 0:
        #break
