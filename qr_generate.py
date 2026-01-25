import qrcode

url = "http://172.20.10.3:5000"  # laptop ka local IP

img = qrcode.make(url)
img.save("campus_qr.png")
print("QR code generated successfully!")

