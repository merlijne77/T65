from machine import Pin, Timer
import time


#SETUP:Rood --> GPIO 15
#SETUP: Blauw ---> GPIO 12
#SETUP: Geel ----> GRND


SIGNAL_PIN = 15  # Gebruik GPIO15 
BLUE_PIN = 12 #Gebruik GPIO12
  
pulse_count = 0
stopped = False

#teller
def pulse_detect(pin):
    global pulse_count
    pulse_count += 1
    print(f'{pulse_count}')
   
#If blue Pin is high finished = True
def finished_dialing(pin):
    global stopped
    stopped= True
      
    
# Instellen van de pin en interrupt
signal = Pin(SIGNAL_PIN, Pin.IN, Pin.PULL_UP)
signal.irq(trigger=Pin.IRQ_RISING, handler=pulse_detect)
#Instellen van de blue pin
signal = Pin(BLUE_PIN, Pin.IN, Pin.PULL_UP)
signal.irq(trigger=Pin.IRQ_RISING, handler=finished_dialing)

print("Ready to count! Turn the turntable!")

try:
    while True:
        time.sleep(0.01)
        if stopped:#:reset variables
            pulse_count = 0
            stopped = False
            print('stopped')
except KeyboardInterrupt:
    print("Gestopt.")