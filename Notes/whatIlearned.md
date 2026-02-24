## what is EXIF
exif = exchangable image file format
It is hidden metadata stord inside images (mostly JPEGs)
**when you take a photo, your phone secretly stores:**
- Date taken
- GPS location
- Software used to edit it 
- Resolution
- ISO , aperture, exposure

So EXIF is basicallyL: "hidden information about how and where this image was created or modified."
**Why would we need to care about exif in ETHIO-VERIFY**

Cuz if someone edits a screenshot using adobe photoshop, canva, Some editing tool
It sometimes leaves traces in EXIF like:
    Software:   Adobe Photoshop 2023

That's suspicious for a bank payment screenshot.

**PIL = python imaging library**
Modern verison is called pillow
- open images
- read metadata
- later also manipulate pixels

**easyocr**
user for:
- reading text form images
- Extracting Transaction Id
- Extracting Amount
- Extracting Date

**python-multipart**
required for file uploads in fastapi:

**opencv-python**
used for:
- Pixel diffrence (ELA)
- Blur detectin
- Texture analysis

**numpy**
This one is used by opencv: It allows
- Matrix math
- pixel calcutaions
- Image diffrence computaion
