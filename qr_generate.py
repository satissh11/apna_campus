import qrcode

# Latest Render URL
url = "https://smart-campus-rw8h.onrender.com"

# QR code generate
img = qrcode.make(url)

# Save image
img.save("campus_qr.png")

print("✅ QR code updated with latest URL!")
