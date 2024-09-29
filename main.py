import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, long_url):
    url = 'https://api.vk.ru/method/utils.getShortLink'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params={"v":5.199, "url":long_url}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['response']['short_url']


def count_clicks(token, short_url):
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params={"v":5.199, "key":short_url, "extended":0, "interval":"forever"}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['response']


def main():
    load_dotenv()
    token=os.environ['VK_TOKEN']
    link=input("Введите ссылку: ")
    parsed_link=urlparse(link)
    try:
        if parsed_link.netloc=="vk.cc":
            print("Количество кликов по ссылке",count_clicks(token, parsed_link.path[1:]))
        else:
            print('Сокращенная ссылка: ', shorten_link(token, link))
    except requests.exceptions.HTTPError:
        print("Проверьте вашу ссылку")

        
if __name__ == "__main__":
    main()
    

    
