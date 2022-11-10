import schedule
import time
#from tkinter import *
import requests
import json
import alsaaudio
import os

try:
    
    def Main_cal():
        from prayer_times_calculator import PrayerTimesCalculator
        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d")
        # required parameters
        lat = 3.078622497747135
        long = 101.5206969400765
        calc_method = 'karachi'
        date = str(dt_string)
        # optional parameters
        school = "shafi"
        midnightMode = "jafari"
        latitudeAdjustmentMethod = "middle of the night"
        # If tune = True, then you can tune the timings by adding the tune parameter
        # (denoting addition / substraction in minutes)
        # Please NOTE that tuning one prayer will not change another.
        # So adding 3 mins to Maghrib will NOT automatically add 3 mins to Isha
        tune = True
        imsak_tune = 0
        fajr_tune = 2
        sunrise_tune = 0
        dhuhr_tune = 2
        asr_tune = 0
        maghrib_tune = 1
        sunset_tune = 0
        isha_tune = 0
        midnight_tune = 0
        # If calc_method="custom", then you can override some of these variables
        fajr_angle = 0
        maghrib_angle = 0
        isha_angle = 0
        
        calc = PrayerTimesCalculator(
            latitude=lat,
            longitude=long,
            calculation_method=calc_method,
            date=date,
            school=school,
            midnightMode=midnightMode,
            latitudeAdjustmentMethod=latitudeAdjustmentMethod,
            tune=tune,
            imsak_tune=imsak_tune,
            fajr_tune=fajr_tune,
            sunrise_tune=sunrise_tune,
            dhuhr_tune=dhuhr_tune,
            asr_tune=asr_tune,
            maghrib_tune=maghrib_tune,
            sunset_tune=sunset_tune,
            isha_tune=isha_tune,
            fajr_angle=fajr_angle,
            maghrib_angle=maghrib_angle,
            isha_angle=isha_angle,
        )
        
        
        
        
        times = calc.fetch_prayer_times()
        return times
    
    
    
        {'Fajr': '05:31',
         'Sunrise': '06:53',
         'Dhuhr': '11:38',
         'Asr': '14:03',
         'Sunset': '16:22',
         'Maghrib': '16:22',
         'Isha': '17:44',
         'Imsak': '05:21',
         'Midnight': '22:57',
         'date': {'readable': '26 Nov 2018',
          'timestamp': '1543276800',
          'hijri': {'date': '17-03-1440',
           'format': 'DD-MM-YYYY',
           'day': '17',
           'weekday': {'en': 'Al Athnayn', 'ar': 'الاثنين'},
           'month': {'number': 3, 'en': 'Rabīʿ al-awwal', 'ar': 'رَبيع الأوّل'},
           'year': '1440',
           'designation': {'abbreviated': 'AH', 'expanded': 'Anno Hegirae'},
           'holidays': []},
          'gregorian': {'date': '26-11-2018',
           'format': 'DD-MM-YYYY',
           'day': '26',
           'weekday': {'en': 'Monday'},
           'month': {'number': 11, 'en': 'November'},
           'year': '2018',
           'designation': {'abbreviated': 'AD', 'expanded': 'Anno Domini'}}}}
       

    def fajr():
        txt = str(Main_cal())
        #print(txt)
        x = txt.split(",")
        y = x[0].split("'")
        print('Fjir : '+str(y[3]))
        return (y[3])
    def Dhuhr():
        txt = str(Main_cal())
        #print(txt)
        x = txt.split(",")
        y = x[2].split("'")
        print('Dhuhr : '+str(y[3]))
        return (y[3])
    def Asr():
        txt = str(Main_cal())
        #print(txt)
        x = txt.split(",")
        y = x[3].split("'")
        print('Asr : '+str(y[3]))
        return (y[3])
    def Maghrib():
        txt = str(Main_cal())
        #print(txt)
        x = txt.split(",")
        y = x[5].split("'")
        print('Maghrib : '+str(y[3]))
        return (y[3])
    def Isha():
        txt = str(Main_cal())
        #print(txt)
        x = txt.split(",")
        y = x[6].split("'")
        print('Isha : '+str(y[3]))
        return (y[3])
    
except:
    print('error')
    

def vol(v):

    m = alsaaudio.Mixer()
    vol = m.getvolume()
    m.setvolume(v)
    vol = m.getvolume()

def Azan_fajir():
    import  vlc
    import time
    vol(50)
    p = vlc.MediaPlayer("azan_fajir.mp3")
    p.play()
    time.sleep(245)
    p.stop()
    
def Azan_zohar():
    import  vlc
    import time
    vol(100)
    p = vlc.MediaPlayer("azan_zohar.mp3")
    p.play()
    time.sleep(135)
    p.stop()
    
    p = vlc.MediaPlayer("Dua-after-adhan.mp3")
    p.play()
    time.sleep(35)
    p.stop()
    

def Azan_asar():
    import  vlc
    import time
    vol(100)
    p = vlc.MediaPlayer("azan_asar.mp3")
    p.play()
    time.sleep(235)
    p.stop()
    
    p = vlc.MediaPlayer("Dua-after-adhan.mp3")
    p.play()
    time.sleep(35)
    p.stop()
    

def Azan_maghrib():
    import  vlc
    import time
    vol(100)
    p = vlc.MediaPlayer("azan_maghrib.mp3")
    p.play()
    time.sleep(205)
    p.stop()
    
    p = vlc.MediaPlayer("Dua-after-adhan.mp3")
    p.play()
    time.sleep(35)
    p.stop()


def Azan_isha():
    import  vlc
    import time
    vol(100)
    p = vlc.MediaPlayer("azan_isha.wma")
    p.play()
    time.sleep(235)
    p.stop()
    
    p = vlc.MediaPlayer("Dua-after-adhan.mp3")
    p.play()
    time.sleep(35)
    p.stop()

# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")
 
def good_luck():
    print("Good Luck for Test")
 
def work():
    print("Study and work hard")
 
def bedtime():
    print("It is bed time go rest")
     
def geeks():
    print("Shaurya says Geeksforgeeks")
 
def blutoothcon():
     output_stream = os.popen('pulseaudio --start')
     print (str(output_stream.read()))
     time.sleep(2)
     output_stream = os.popen('bluetoothctl')
     print (output_stream.read())
     time.sleep(2)
     output_stream = os.popen('connect 33:C1:68:AB:C2:A3')
     print (output_stream.read())
     time.sleep(5)
     output_stream = os.popen('quit')
     print (output_stream.read())
     time.sleep(2)
# Task scheduling
#After every 10mins blutoothcon() is called.
schedule.every(10).minutes.do(blutoothcon)
 
# After every hour geeks() is called.
#schedule.every().hour.do(geeks)
 
# Every day at 12am or 00:00 time bedtime() is called.
#Prayertimings()
#Azan_zohar()
vol(100)
#blutoothcon()
#schedule.every().day.at("20:17").do(Azan_maghrib)
schedule.every().day.at(str(fajr())).do(Azan_fajir)
schedule.every().day.at(str(Dhuhr())).do(Azan_zohar)
schedule.every().day.at(str(Asr())).do(Azan_asar)
schedule.every().day.at(str(Maghrib())).do(Azan_maghrib)
schedule.every().day.at(str(Isha())).do(Azan_isha)
#schedule.every().day.at("23:18").do(Azan_maghrib)



 
# After every 5 to 10mins in between run work()
#schedule.every(5).to(10).minutes.do(work)
 
# Every monday good_luck() is called
#schedule.every().monday.do(good_luck)
 
# Every tuesday at 18:00 sudo_placement() is called
#schedule.every().tuesday.at("18:00").do(sudo_placement)
 
# Loop so that the scheduling task
# keeps on running all time.
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)













