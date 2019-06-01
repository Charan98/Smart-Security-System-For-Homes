from gpiozero import LED
from signal import pause
import RPi.GPIO as GPIO
import time
import os

IR_PIN = 15
buzzer = 18
LED_PIN = 27
indicator = LED(LED_PIN)
Flame = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(Flame, GPIO.IN)

GPIO.output(buzzer,False)
print "IR Sensor Ready....."
print " "

count = 0

def callback(channel):
    print("Flame detected")
	GPIO.output(buzzer,True)
	

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

try: 
   while True:
      if GPIO.input(IR_PIN):
          count += 1
          indicator.on()
          os.system("sudo service motion restart")
          print("Video streaming is live on -- 192.168.132.216")
          print("{:>3} Got something".format(count))
          GPIO.output(buzzer,True)
          print "Object Detected"
          while GPIO.input(IR_PIN):
              time.sleep(0.2)
      else:
          indicator.off()
          print("{:>3} Nothing detected".format(count))
          GPIO.output(buzzer,False)
      
      time.sleep(0.2)


except KeyboardInterrupt:
    GPIO.cleanup()


   
  
   
    

    
  

