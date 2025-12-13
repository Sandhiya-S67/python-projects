import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
textOrUrl = input("Enter the text or URL: ").strip()
qr.add_data(textOrUrl)
qr.make(fit=True)

filename = input("Enter the filename: ").strip()

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)
print(f"QR code saved as {filename}")
