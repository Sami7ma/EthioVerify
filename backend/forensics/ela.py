from PIL import Image, ImageChops, ImageEnhance
import os

def perform_ela(image_path: str, save_path: str = None, quality: int = 95) -> Image.Image:
    """
    Performs Error Level Analysis on an image and returns a heatmap image.
    :param image_path: Path to original image
    :param save_path: Optional path to save the ELA image
    :param quality: JPEG recompression quality
    :return: PIL Image (ELA heatmap)
    """

    original = Image.open(image_path).convert('RGB')

    # Save a recompressed version in memory
    temp_path = "temp_ela.jpg"
    original.save(temp_path, 'JPEG', quality=quality)
    compressed = Image.open(temp_path)

    # Compute difference
    diff = ImageChops.difference(original, compressed)

    # Amplify difference for visibility
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1  # Avoid division by zero

    factor = 255.0 / max_diff
    diff = ImageEnhance.Brightness(diff).enhance(factor)

    # Save if requested
    if save_path:
        diff.save(save_path)

    # Clean up temp
    if os.path.exists(temp_path):
        os.remove(temp_path)

    return diff