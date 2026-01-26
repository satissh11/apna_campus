import qrcode

# Tumhare Render ka live URL
url = "https://smart-campus-rw8h.onrender.com"

# QR code generate karo
img = qrcode.make(url)

# Image save karo
img.save("campus_qr.png")

print("QR Code generated successfully!")
