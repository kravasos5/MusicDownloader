import os
import re
from concurrent.futures import ThreadPoolExecutor

import ffmpeg
import yt_dlp

from src.config.config import Settings, settings


class MusicCutter:
    def __init__(self, settings: Settings):
        self.settings = settings

    @staticmethod
    def make_threads(urls: list[str], threads_count: int, functor):
        max_threads = threads_count
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = [executor.submit(functor, url) for url in urls]

            for future in futures:
                future.result()

    def cut_playlists(self) -> None:
        urls = self.fetch_urls_from_file(self.settings.URLS_FILE_PATH)

        self.make_threads(urls, self.settings.DEFAULT_THREADS_COUNT, self.download_music)

        print("Все плейлисты обработаны")

    def download_songs(self) -> None:
        urls = self.fetch_urls_from_file(self.settings.SINGLE_SONG_URLS_FILE_PATH)

        self.make_threads(urls, self.settings.DEFAULT_THREADS_COUNT, self.download_song)

        print("Все треки обработаны")

    @staticmethod
    def fetch_urls_from_file(urls_file_path: str):
        with open(urls_file_path, "r") as file:
            return file.readlines()

    def download_song(self, url: str):
        with yt_dlp.YoutubeDL(self.settings.YDL_OPTIONS_FOR_SONGS) as ydl:
            ydl.download(url)

    def download_music(self, url: str):
        with yt_dlp.YoutubeDL(self.settings.YDL_OPTIONS_FOR_PLAYLIST) as ydl:
            info = ydl.extract_info(url, download=True)
            if "description" in info:
                chapters = info.get("chapters")
                if chapters:
                    self.save_songs(
                        chapters,
                        ydl.prepare_filename(info),
                        os.path.join(self.settings.MUSIC_PATH, info.get("id")),
                        self.settings.SONG_FORMAT
                    )
                else:
                    print("Таймкоды не найдены.")

    @staticmethod
    def save_songs(songs: list, parent_file_path: str, destination: str, song_format: str) -> None:
        for song in songs:
            start_time = song.get("start_time")
            end_time = song.get("end_time")
            title = song.get("title")

            output_filename = os.path.join(destination, f"{MusicCutter.sanitize_filename(title)}.{song_format}")

            input_stream = ffmpeg.input(parent_file_path)
            stream = (
                input_stream
                .filter("atrim", start=start_time, end=end_time)
                .output(output_filename, format=song_format)
            )

            ffmpeg.run(stream)

    @staticmethod
    def sanitize_filename(filename: str):
        return re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z0-9_\-.а-яА-Я]+', '', filename.strip())).strip()


if __name__ == "__main__":
    print("MUSIC CUTTER")
    music_cutter = MusicCutter(settings=settings)
    music_cutter.download_songs()
