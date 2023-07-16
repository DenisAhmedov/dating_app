import os

from PIL import Image, ImageDraw, ImageFont

from config.settings import MEDIA_ROOT


def add_watermark(image_path: str):
    """
    Добавление водяного знака на изображение
    """

    image = Image.open(image_path)
    drawing = ImageDraw.Draw(image)

    black = (3, 8, 12)
    font = ImageFont.truetype("arial.ttf", 40, encoding="unic")
    drawing.text((0, 0), 'dating app', fill=black, font=font)

    image.save(os.path.join(MEDIA_ROOT, str(image_path)))


