from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont

def change_brightness(image, factor):
    return ImageEnhance.Brightness(image).enhance(factor)

def change_contrast(image, factor):
    return ImageEnhance.Contrast(image).enhance(factor)

def main():
    overlay_image = Image.open("asset/img/gambar.jpg")
    background_image = (
        Image.open("asset/img/background.jpg")
        .convert("L")
        .rotate(30)
        .filter(ImageFilter.BoxBlur(4))
    )
    

    brightness_factor = 1.27  # Nim 327
    contrast_factor = 1.27  


    transformations = [
        lambda img: change_brightness(img, brightness_factor),
        lambda img: change_contrast(img, contrast_factor),
        lambda img: img.resize((200, 200)),
    ]

    # Apply transformations using map
    for transformation in transformations:
        overlay_image = transformation(overlay_image)

    x_center = (background_image.width - overlay_image.width) // 2
    y_center = (background_image.height - overlay_image.height) // 2

    background_image.paste(overlay_image, (x_center, y_center))

    draw = ImageDraw.Draw(background_image)

    text = "Informatika JOSSS!"
    font = ImageFont.truetype("asset/font/static/Montserrat-Bold.ttf", 24)

    _, _, text_width, text_height = draw.textbbox((0, 0), text, font=font)

    text_x = (background_image.width - text_width) // 2
    text_y = (background_image.height - text_height) // 2

    draw.text((text_x, text_y), text, font=font, fill="black")

    background_image.save("asset/result/tugas_praktikum_enam.jpg")
    background_image.show()

if __name__ == "__main__":
    main()
