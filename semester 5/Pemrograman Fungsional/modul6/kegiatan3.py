from PIL import Image, ImageEnhance


image_path = "image/umm.jpg"
original_image = Image.open(image_path)

brightness_factor = 1.5
contrast_factor = 1.2

brightness_enhancer = ImageEnhance.Brightness(original_image)
brightened_image = brightness_enhancer.enhance(brightness_factor)

contrast_enhancer = ImageEnhance.Contrast(brightened_image)
final_image = contrast_enhancer.enhance(contrast_factor)
final_image = final_image.convert("RGB")


output_path = "percobaan_tiga.jpg"
final_image.save(output_path)

final_image.show()