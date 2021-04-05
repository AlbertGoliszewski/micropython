from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import utime
import time
#joystick
xAx = ADC(Pin(27))
yAx = ADC(Pin(26))
button = Pin(16,Pin.IN, Pin.PULL_UP)
WIDTH = 128
HEIGHT = 64
i2c = I2C(0)
print("I2C adres : "+hex(i2c.scan()[0]).upper())
print("I2C konfiguracja : "+str(i2c))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()
while True:
  oled.fill(0)
  oled.rect(0,0,127,63,1)
  oled.rect(0,0,127,16,1)
  xValue = xAx.read_u16()
  yValue = yAx.read_u16()
  wspol = 546.125
  xFloat = (32767.5-xValue)/wspol
  yFloat = (32767.5-yValue)/wspol
  buttonValue = button.value()
  xStatus = "centrum x "
  yStatus = "centrum y "
  buttonStatus = "wycisniety"
  if xValue <= 600:
    xStatus = "lewo      "
    if yValue >= 60000:
      yStatus = "dol       "
    if yValue <= 600:
      yStatus = "gora      "
  elif xValue >= 60000:
    xStatus = "prawo     "
    if yValue >= 60000:
      yStatus = "dol       "
    if yValue <= 600:
      yStatus = "gora      "
  elif yValue <= 600:
    yStatus = "gora      "
  elif yValue >= 60000:
    yStatus = "dol       "
  if buttonValue == 0:
    buttonStatus = "wcisniety "
  oled.text("Test joystika",3 ,4)
  oled.text("x :"+xStatus,3 ,18)
  oled.text("y :"+yStatus,3 ,28)
  oled.text("fire:"+buttonStatus,5 ,38)
  oled.rect(0,48,127,15,1)
  if int(xFloat)>=0:
    oled.fill_rect(63,50,1+int(xFloat),4,1)
  elif int(xFloat)<0:
    oled.fill_rect(63+int(xFloat),50,abs(int(xFloat)),4,1)
  if int(yFloat)>=0:
    oled.fill_rect(63,56,1+int(yFloat),4,1)
  elif int(yFloat)<0:
    oled.fill_rect(63+int(yFloat),56,abs(int(yFloat)),4,1)
  oled.show()
