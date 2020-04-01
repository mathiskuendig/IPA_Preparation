 ###############################################################################
# Temp_Measure.py
#
# Contacts: Mathis Kündig
# DATE: Juni 2019
###############################################################################

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

class LCDDisplay:
    
    def __init__ (self,UID_LCD,ipcon: IPConnection):
        self.display = BrickletLCD128x64(UID_LCD, ipcon)
        
    def LCDDisplay_WriteTextToPosition(self,line,position,text):
        self.display.write_line(line,position,text)
        
        
    def LCDDisplay_ClearDisplay(self):
        self.display.clear_display()