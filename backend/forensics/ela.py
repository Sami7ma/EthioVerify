from PIL import Image, ImageChops, ImageEnhance
import os
import numpy as np

def perform_ela(image_path: str, save_path: str = None, quality: int = 95) -> Image.Image:
    """
    Performs Error Level Analysis on an image and returns a heatmap image.
    :param image_path: Path to original image
    :param save_path: Optional path to save the ELA image
    :param quality: JPEG recompression quality
    :return: PIL Image (ELA heatmap)
    """
    #open the original image
    original = Image.open(image_path).convert('RGB')
    # create a comparsion image
    temp_path = "temp_ela.jpg"
    original.save(temp_path, 'JPEG', quality=quality)
    compressed = Image.open(temp_path)

    # Finding the diffrence between the original and compressed image
    diff = ImageChops.difference(original, compressed)

    # Amplify difference for visibility
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1  # Avoid division by zero

    factor = 255.0 / max_diff
    diff = ImageEnhance.Brightness(diff).enhance(factor)

    # Save the ELA image if a path is provided
    if save_path:
        diff.save(save_path)
    # Clean up temporary file
    if os.path.exists(temp_path):
        os.remove(temp_path)

    return diff

def analyze_ela_intensity(ela_image: Image.Image) -> float:
    """
    Analyzes the intensity of the ELA heatmap to compute a score.
    Higer intesity = more likely to be manipulated
    """
    gray = ela_image.convert('L')  # Convert to grayscale
    
    #conver the image to numpy array for analysis
    pixels = np.array(gray)
    # calculate the mean intensity of the ELA image
    mean_intensity = np.mean(pixels)

    ela_score = (mean_intensity / 255.0) * 100  # Normalize to 0-100
    return round(float(ela_score), 2)