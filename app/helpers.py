import os

from PIL import Image, ImageDraw, ImageFont
from django.core.mail import send_mass_mail

from config.settings import MEDIA_ROOT, EMAIL_HOST


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


def send_mail_to_matched(client1: tuple[str, str], client2: tuple[str, str]):
    mail_subject = 'Message from DATING_APP'
    mail_text = 'Вы понравились %s! Почта участника: %s'

    message1 = (
        mail_subject,
        mail_text % client2,
        EMAIL_HOST,
        [client1[1]]
    )
    message2 = (
        mail_subject,
        mail_text % client1,
        EMAIL_HOST,
        [client2[1]]
    )

    send_mass_mail((message1, message2), fail_silently=False)

