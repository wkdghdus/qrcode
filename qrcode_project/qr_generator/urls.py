#Imports the path function for URL routing.
from django.urls import path
from . import views


# A list of URL patterns that maps a URL path to a view.
# path('generate_qr/', views.generate_qr_code, name='generate_qr_code'): 
# Maps the URL path generate_qr/ to the generate_qr_code view function. 
# When this URL is accessed, Django will call generate_qr_code to handle the request.
urlpatterns = [
    path('generate_qr/', views.generate_qr_code, name='generate_qr_code'),
    path('form/', views.qr_form, name='qr_form'),
]