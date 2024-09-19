from django.shortcuts import render
#Allows returning HTTP responses from your view functions.
from django.http import HttpResponse
#The library installed for generating QR codes.
import qrcode
#A module to handle binary data in memory (like a buffer), 
#which is useful for creating in-memory file-like objects to store images temporarily.
from io import BytesIO

def generate_qr_code(request):
    # Example data for QR code (replace with actual data from user input later)
    wifi_ssid = 'YourNetworkSSID'
    wifi_password = 'YourNetworkPassword'
    menu_url = 'https://example.com/menu'

    # Construct the data for the QR code (this can include Wi-Fi credentials and menu URL)
    qr_data = f"WIFI:T:WPA;S:{wifi_ssid};P:{wifi_password};;URL:{menu_url}"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image in a BytesIO stream to send it as an HTTP response
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(buffer, content_type='image/png')
