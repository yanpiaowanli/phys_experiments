from PIL import Image, ImageEnhance


def enhance_image(path):
    # Open the image file
    img = Image.open(path)

    # Enhance the image
    enhancer = ImageEnhance.Contrast(img)
    enhanced_img = enhancer.enhance(1.0)

    # Save the enhanced image
    enhanced_img.save(path)
