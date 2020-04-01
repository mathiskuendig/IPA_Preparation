import devices
import loans
import myDatabase
import users
import tinkerforge
import time
from tinkerforge.ip_connection import IPConnection
import lcddisplay
import csv
from panda import pd



HOST = "localhost"
PORT = 4223

UID_LCD = 'MXY'

ipcon = IPConnection() # Create IP connection
ipcon.connect(HOST, PORT) # Connect to brick

#with open('usersImport.csv') as csvfile:
    #readCSV = csv.reader(csvfile, delimiter=';')
    #for row in readCSV:
        #print(row)
        #print(row[0])
        #print(row[0], row[1], row[2], )


#with open('usersImport.csv', 'r') as csvfile:
    #csv_dict_reader = csv.DictReader(csvfile, delimiter=';')
    #for row in csv_dict_reader:
        #print(row['surname'], row['tagId'])
        #break


#with open('usersImport.csv', 'r') as csvfile:
    #csv_dict_reader = csv.DictReader(csvfile, delimiter=';')
    #column_names = csv_dict_reader.fieldnames
    #print(column_names)

#f = open("usersImport.csv", skiprows=2)
#csv_reader = csv.reader(f)
#print(next(csv_reader))


# Skip 2 rows from top in csv and initialize a dataframe
usersDf = pd.read_csv('users.csv', skiprows=2)
print(usersDf)

LCD_display = lcddisplay.LCDDisplay(UID_LCD, ipcon)

LCD_display.LCDDisplay_WriteTextToPosition(1,2,'text1')
LCD_display.LCDDisplay_WriteTextToPosition(3,2,"text2")

time.sleep(3)

LCD_display.LCDDisplay_ClearDisplay()