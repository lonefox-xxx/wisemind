import requests


def uploadToTelegram(image, explanation):
    bot_token = "5193295271:AAG_wzFr4UfhVthRbSH_V2tMrzaeyZ9eyac"
    chat_id = "@wisemindxyz"

    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    data = {'chat_id': chat_id, 'photo': image,
            'caption': '"' + explanation + '"'}

    response = requests.post(url,  data=data)

    if response.status_code == 200:
        print("Image sent successfully to Telegram channel")
    else:
        print(f"Failed to send image. Status code: {response.status_code}")
        print(f"Response: {response.text}")
