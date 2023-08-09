from design import MainUi
from pygame import mixer
from vk_api.audio import VkAudio
from track import Track
from dialog_window import Dialog
import re


class Program(MainUi):

    api = None

    def __init__(self):
        super().__init__()

        dialog = Dialog(self)

        mixer.init()

        self.btn_load._command = self.get_track
        self.run()

    def get_track(self):
        vk_audio = VkAudio(self.api)
        your_audio = vk_audio.get()
        index = 0
        tracks = []

        # создает список с классами Track
        for track in your_audio:
            artist = track.get('artist')
            name = track.get('title')
            url = track.get('url')

            tr = Track(artist, name, url)
            tracks.append(tr)
            RE_M3U8_TO_MP3 = re.compile(r'/[0-9a-f]+(/audios)?/([0-9a-f]+)/index.m3u8')
            
        # заполняет listbox из списка
        for track in tracks:
            author = track.author
            name = track.name
            tr = f'{author}: {name}'
            self.listbox.insert(index, tr)
            index += 1
