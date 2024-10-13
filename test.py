from PIL import Image, ImageDraw, ImageFont
import textwrap
from io import BytesIO
import requests

def create_and_send_quote_image(quote, author, bot_token, chat_id):
    
    with Image.open('temp2.png') as img:
        width = img.width
        height = img.height

        draw = ImageDraw.Draw(img)

        quote_font = ImageFont.truetype("././Montserrat-SemiBold.ttf", 56)
        author_font = ImageFont.truetype("Montserrat-Regular.ttf", 17)

        line_spacing = 1.4
        text_box_width = 748.1

        wrapped_text = textwrap.wrap(quote, width=27)
        y_text = height//2 - 0.037*height

        for line in wrapped_text:
            bbox = quote_font.getbbox(line)
            line_width = bbox[2] - bbox[0]
            line_height = bbox[3] - bbox[1]

            draw.text(((width - line_width) / 2, y_text), line, font=quote_font, fill='white')
            y_text += line_height * line_spacing

        draw.text((width - 40, height - 40), f"@{author}", font=author_font, fill='white', anchor='rb')

        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

    # Send image to Telegram
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    files = {'photo': ('quote.png', img_byte_arr, 'image/png')}
    data = {'chat_id': chat_id}
    
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        print("Image sent successfully to Telegram channel")
    else:
        print(f"Failed to send image. Status code: {response.status_code}")
        print(f"Response: {response.text}")

# Usage
quote = "In the middle of every difficulty lies opportunity."
author = "wisemind"
bot_token = "5193295271:AAG_wzFr4UfhVthRbSH_V2tMrzaeyZ9eyac"
chat_id = "@httpswisemindxyz"

create_and_send_quote_image(quote, author, bot_token, chat_id)