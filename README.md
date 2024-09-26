# QR Code Generator for Wi-Fi and Menus

## Overview
This Django project generates QR codes that encode Wi-Fi credentials and either a menu URL or an uploaded menu file (PDF or image).

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-directory>
```


### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up the database
```bash
python manage.py migrate
```

### 4. Run the server
```bash
python manage.py runserver
```

### 5. Access the App
- Open your browser and visit `http://127.0.0.1:8000/qr/form/` to fill out the form and generate a QR code.

## Features
- **Generate QR Codes**: The QR code can include Wi-Fi credentials (SSID, password) and either a URL to an existing menu or an uploaded menu (PDF or image).
- **Form Submission**: Users can either provide a URL to their menu or upload a PDF/image directly.
- **Responsive**: The application validates user input and provides error messages if necessary fields are missing.

## File Upload
- Uploaded menus are stored in the `/media/` folder and served at `/media/<filename>`.
- Menu files can be PDFs or images (JPEG, PNG, etc.).

## Project Structure
```
qrcode_project/
├── qr_generator/
│   ├── templates/
│   │   └── qr_generator/
│   │       └── qr_form.html
│   ├── views.py
│   └── urls.py
├── media/               # Uploaded media files
├── qrcode_project/      # Project settings and configurations
├── manage.py
└── requirements.txt     # Python package dependencies
```
