from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path: str) -> dict:
    # extract metadata from an image file
    metadata = {}
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag,tag)
                metadata[decoded_tag] = value
    except Exception as e:
        metadata["error"] = str(e)
    return metadata

def check_editing_software(metadata: dict) -> bool:
    suspicious_keywords = ["Adobe", "Photoshop", "GIMP", "Paint.NET", "CorelDRAW", "Affinity Photo","Lightroom", "Capture One", "Inkscape", "Pixlr", "Canva", "Krita","Snapseed", "Facetune", "PicsArt", "ExifTool", "ImageMagick", "Layers"]
    for value in metadata.values():
        if isinstance(value,str):
            for keyword in suspicious_keywords:
                if keyword.lower() in value.lower():
                    return True
    return False

        