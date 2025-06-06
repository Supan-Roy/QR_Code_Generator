import qrcode
import re
from datetime import datetime

data = input("Enter Text: ")

safe_data = re.sub(r'\W+', '_', data[:10])

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"qr_{current_time}.png"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=2
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save(filename)

print(f"QR Code generated and saved as {filename}")
