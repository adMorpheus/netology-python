import yandex_disk_creds

# yandex_disk_creds.OAUTH_TOKEN
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader(yandex_disk_creds.OAUTH_TOKEN)
    result = uploader.upload('c:\my_folder\file.txt')