from quote import create_quote_image
from getQuote import getQuote
import requests

quote_and_explanation = getQuote()

quote = quote_and_explanation['quote']
explanation = quote_and_explanation['explanation']

quote_image = create_quote_image(quote, 'wisemindxyz')

bot_token = "5193295271:AAG_wzFr4UfhVthRbSH_V2tMrzaeyZ9eyac"
chat_id = "@wisemindxyz"

url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
files = {'photo': ('quote.png', quote_image, 'image/png')}
data = {'chat_id': chat_id, 'caption': '"' + explanation + '"'}

response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    print("Image sent successfully to Telegram channel")
else:
    print(f"Failed to send image. Status code: {response.status_code}")
    print(f"Response: {response.text}")
