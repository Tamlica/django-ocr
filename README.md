# django-ocr
Implementing simple OCR on django framework

# Before Run
```bash
- sudo apt-get install libleptonica-dev tesseract-ocr libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
- pip install --upgrade pip
- pip install -r requirements.txt

```

# Migrate
```bash
- python manage.py makemigrations 
- python manage.py migrate
```

# Start the program
```bash
python3 manage.py runserver
```