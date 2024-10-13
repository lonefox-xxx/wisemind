from PIL import Image, ImageDraw, ImageFont
import textwrap
from io import BytesIO

def create_quote_image(quote, author):
    with Image.open('temp2.png') as img:
        width = img.width
        height = img.height

        draw = ImageDraw.Draw(img)

        quote_font = ImageFont.truetype("././Montserrat-SemiBold.ttf", 56)
        author_font = ImageFont.truetype("Montserrat-Regular.ttf", 17)

        line_spacing = 1.4

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
        
        return img_byte_arr
