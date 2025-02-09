from PIL import Image, ImageDraw, ImageFont
import textwrap
from io import BytesIO
import requests
import base64


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

            draw.text(((width - line_width) / 2, y_text),
                      line, font=quote_font, fill='white')
            y_text += line_height * line_spacing

        draw.text((width - 40, height - 40),
                  f"@{author}", font=author_font, fill='white', anchor='rb')

        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return img_byte_arr


def upload_to_freeimage(image_bytes, api_key):
    """
    Upload an image to freeimage.host
    
    Parameters:
    image_bytes (BytesIO): Image in BytesIO format
    api_key (str): The freeimage.host API key
    
    Returns:
    dict: API response containing upload details
    """
    # Convert image to base64
    base64_image = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

    # API endpoint
    url = "https://freeimage.host/api/1/upload"

    # Prepare parameters
    params = {
        'key': api_key,
        'action': 'upload',
        'source': base64_image,
        'format': 'json'
    }

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        if response.text:
            print(f"Error details: {response.text}")
        return None


# Example usage
if __name__ == "__main__":
    API_KEY = "6d207e02198a847aa98d0a2a901485a5"

    # Create a quote image
    quote = "Be yourself; everyone else is already taken."
    author = "Oscar Wilde"

    # Generate the image
    img_bytes = create_quote_image(quote, author)

    # Upload to freeimage.host
    result = upload_to_freeimage(img_bytes, API_KEY)

    if result:
        print("Image uploaded successfully!")
        print(f"Image URL: {result.get('image', {}).get('url')}")
        print(f"Delete URL: {result.get('image', {}).get('delete_url')}")
        print(
            f"Thumbnail URL: {result.get('image', {}).get('thumb', {}).get('url')}")
    else:
        print("Failed to upload image")
