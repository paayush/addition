'''# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "https://www.facebook.com/manchester.dhakal.7"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
'''

from genericpath import exists
from venv import create
import qrcode 
#id = "100069506107795"

import random

for i in range(1,9+1):
    
    num = random.randint(1,9)
    last_num = id[14]
    last_num = f"{id[0:14]+str(num)}"
    new_fb_url = f"https://www.facebook.com/{last_num}"
    
    #if new_fb_url is exists:
    qrcode.make(new_fb_url).save(f"{i}.png")

'''else:
    print("person not exist")''' 

        
'''import qrcode
fb_id = "https://www.facebook.com/nischal.khatiwada.773"
#import png
qrcode.make(fb_id).save("fbook.png")'''