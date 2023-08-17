from pprint import pprint

import yandex_disk_creds
import requests


# yandex_disk_creds.OAUTH_TOKEN
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        headers = {'Authorization': self.token}
        params = {'path': '/sticker.jpg'}
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        upload_link = resp.json()['href']
        with open(file_path, 'rb') as src_file:
            resp = requests.put(upload_link, src_file.read())
            resp.raise_for_status()

            return 'File loaded successfuly'


if __name__ == '__main__':
    uploader = YaUploader(yandex_disk_creds.OAUTH_TOKEN)
    result = uploader.upload('c:\sticker.jpg')
