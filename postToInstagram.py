import requests
import json


def upload_photo_to_instagram(image_url, caption):
    access_token = "EAAIq18VnnYEBOyWZCWNLV6xQLXcUoYVKkxRyMa5gg3sSP7WDARVwftVbv4u8lpVo9xs6R4fXsZBgIxaCPOLGQbGNVbjY2VpJDZBnZAW0qFCZAydBW1XTRJPEZBeu0TemZCFXBFm3F6IpEPMGdxURAcfqVG0hctWLo1mocHZAaGJx23gdnGD5tI60JVxRsxeetoUg"
    instagram_account_id = 17841469612650516

    url = f"https://graph.facebook.com/v18.0/{instagram_account_id}/media"

    payload = {
        'image_url': image_url,
        'caption': caption,
        'access_token': access_token
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        creation_id = response.json()['id']

        url = f"https://graph.facebook.com/v18.0/{instagram_account_id}/media_publish"
        payload = {
            'creation_id': creation_id,
            'access_token': access_token
        }

        response = requests.post(url, data=payload)
        response.raise_for_status()
        print('post updated on instagram')
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        if response.text:
            print(f"Error details: {response.text}")
        return None
