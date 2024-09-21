from django.shortcuts import render
#Allows returning HTTP responses from your view functions.
from django.http import HttpResponse
#The library installed for generating QR codes.
import qrcode
#A module to handle binary data in memory (like a buffer), 
#which is useful for creating in-memory file-like objects to store images temporarily.
from io import BytesIO

from django.shortcuts import render

def qr_form(request):
    #renders the qr_form.html template when the qr_form view is called
    return render(request, 'qr_generator/qr_form.html')


def generate_qr_code(request):
    # Get the data from the query parameters (URL)
    wifi_ssid = request.GET.get('ssid', 'DefaultSSID')  # DefaultSSID is used if no input is provided
    wifi_password = request.GET.get('password', 'DefaultPassword')  # DefaultPassword is used if no input is provided
    menu_url = request.GET.get('menu_url', 'https://example.com/menu')

    # Construct the data for the QR code (Wi-Fi and URL)
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