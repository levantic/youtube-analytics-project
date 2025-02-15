import build
import requests
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json

#from helper.youtube_api_manual import printj
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окруженияapi_key: str = 'AIzaSyCED6SCagD1Z3aCrHuM6XxWu2BA0jDRUG8'
api_key: str = os.getenv('YOUTUBE_API_KEY')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Python\youtube-api-445222-6abe3d21edc9.json"
#os.getenv('YOUTUBE_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        #Выводит в консоль информацию о канале.
        #channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(channel)
