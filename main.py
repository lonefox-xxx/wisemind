from quote import create_quote_image
from getQuote import getQuote
from uploadToTelegram import uploadToTelegram
from postToInstagram import upload_photo_to_instagram
import schedule
import time

print('auto post started...')


def start():
    quote_and_explanation = getQuote()
    quote = quote_and_explanation['quote']
    explanation = quote_and_explanation['explanation']

    quote_image = create_quote_image(quote, 'wisemindxyz')
    uploadToTelegram(quote_image, explanation)
    upload_photo_to_instagram(quote_image, explanation)


schedule.every().day.at("10:00").do(start)
schedule.every().day.at("18:00").do(start)

while True:
    schedule.run_pending()
    time.sleep(60)
