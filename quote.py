from PIL import Image, ImageDraw, ImageFont
import textwrap
from io import BytesIO
import base64
import requests


def create_quote_image(quote, author):
    try:
        # Open the image template
        with Image.open('temp2.png') as img:
            width, height = img.size
            draw = ImageDraw.Draw(img)

            # Load fonts
            quote_font = ImageFont.truetype("Montserrat-SemiBold.ttf", 56)
            author_font = ImageFont.truetype("Montserrat-Regular.ttf", 17)

            # Wrapping text and positioning
            wrapped_text = textwrap.wrap(quote, width=27)
            y_text = height // 2 - int(0.037 * height)
            line_spacing = 1.4

            for line in wrapped_text:
                bbox = quote_font.getbbox(line)
                line_width, line_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
                draw.text(((width - line_width) / 2, y_text),
                          line, font=quote_font, fill='white')
                y_text += line_height * line_spacing

            # Draw author text
            draw.text((width - 40, height - 40),
                      f"@{author}", font=author_font, fill='white', anchor='rb')

            # Convert image to bytes and encode as base64
            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)

        base64_image = base64.b64encode(
            img_byte_arr.getvalue()).decode('utf-8')

        # Upload image to freeimage.host
        url = "https://freeimage.host/api/1/upload"
        params = {
            'key': '6d207e02198a847aa98d0a2a901485a5',
            'action': 'upload',
            'source': base64_image,
            'format': 'json'
        }

        response = requests.post(url, data=params)
        response.raise_for_status()  # Raise error if request fails

        result = response.json()
        return result.get('image', {}).get('url')

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
