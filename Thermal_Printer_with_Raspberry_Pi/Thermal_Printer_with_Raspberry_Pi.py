from escpos.printer import Serial
from time import *
from datetime import date
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%b/%d/%Y %H:%M:%S")
print("Today's date:", dt_string)
""" 9600 Baud, 8N1, Flow Control Enabled """
p = Serial(devfile='/dev/serial0',
           baudrate=9600,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=1.00,
           dsrdtr=True
           )
p.set(
        underline=0,
        align="left",
        font="a",
        width=2,
        height=2,
        density=3,
        invert=0,
        smooth=False,
        flip=False, 
    )
p.text("\n")
p.set(
        underline=0,
        align="center",
        font="a",
        width=2,
        height=2,
        density=2,
        invert=0,
        smooth=False,
        flip=False,       
    )
#Printing the image
p.image("/home/pi/ proj on pi0/CD_new_Logo_black.png",impl="bitImageColumn")
#printing the initial data
p.set(
        underline=0,
        align="left",
     )
p.textln("CIRCUIT DIGEST\n")
p.text("AIRPORT ROAD\n")
p.text("LOCATION : JAIPUR\n")
p.text("TEL : 0141222585\n")
p.text("GSTIN : \n")
p.text("Bill No. : \n\n")
p.set(
        underline=0,
        align="left",
        font="a",
        width=2,
        height=2,
        density=2,
        invert=0,
        smooth=False,
        flip=False,       
    )
p.text("DATE : ")
p.text(dt_string)
p.textln("\n")
p.textln("CASHIER : ")
p.textln(" ===========================")
p.textln("      ITEM   QTY  PRICE    GB")
p.textln(" --------------------------")
p.textln("IR SENSOR  2  30   60")
p.textln("ULTRASONIC  2  80   160")
p.textln("RASPBERRY  1  3300   3300")
p.textln("ADOPTOR  2  120   240")
p.textln(" --------------------------")
p.textln("     SUBTOTAL:  3760")
p.textln("     DISCOUNT:  0.8")
p.textln("     VAT @ 18%: 676.8")
p.textln(" ===========================")
p.textln("    BILL TOTAL: 4436.8")
p.textln("     TENDERD:  0.8")
p.textln("     BALANCE: 676.8")
p.textln(" --------------------------")
p.textln("          THANK YOU")
p.textln(" ===========================")
p.set(
        underline=0,
        align="center",
        font="a",
        width=2,
        height=2,
        density=2,
        invert=0,
        smooth=False,
        flip=False,       
    )
p.qr("Circuit Digest",native=True,size=12)
p.textln("")
p.barcode('123456', 'CODE39')
#if your printer has a paper-cutting facility, then you can use this function
p.cut()
print("done")
