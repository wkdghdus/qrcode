from django.shortcuts import render
#Allows returning HTTP responses from your view functions.
from django.http import HttpResponse
#The library installed for generating QR codes.
import qrcode
#A module to handle binary data in memory (like a buffer), 
#which is useful for creating in-memory file-like objects to store images temporarily.
from io import BytesIO

from django.core.files.storage import FileSystemStorage

from django.shortcuts import render

def qr_form(request):
    #renders the qr_form.html template when the qr_form view is called
    return render(request, 'qr_generator/qr_form.html')

def generate_qr_code(request):
    if request.method == 'POST':
        wifi_ssid = request.POST.get('ssid')
        wifi_password = request.POST.get('password')
        menu_file = request.FILES.get('menu_file')

        # Validate inputs
        if not wifi_ssid:
            return HttpResponse("Error: Wi-Fi SSID is required.", status=400)
        if not wifi_password:
            return HttpResponse("Error: Wi-Fi Password is required.", status=400)

        # If a file is uploaded, save it and create the file URL
        if menu_file:
            fs = FileSystemStorage()
            filename = fs.save(menu_file.name, menu_file)
            file_url = fs.url(filename)
        else:
            file_url = request.POST.get('menu_url')  # If no file, use the URL

        if not file_url:
            return HttpResponse("Error: Either a file or a menu URL is required.", status=400)

        # Construct the QR code data (you may want to customize this)
        qr_data = f"WIFI:T:WPA;S:{wifi_ssid};P:{wifi_password};;URL:{file_url}"
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

    return HttpResponse("Only POST requests are allowed.", status=405)