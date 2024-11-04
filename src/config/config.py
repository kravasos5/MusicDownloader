import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    SONG_FORMAT: str
    YDL_FORMAT: str
    YDL_EXTRACTAUDIO: bool
    YDL_AUDIOFORMAT: str
    DEFAULT_THREADS_COUNT: int

    @property
    def MUSIC_PATH(self) -> str:
        return os.path.join(str(BASE_DIR), "dest", "music")

    @property
    def URLS_FILE_PATH(self) -> str:
        return os.path.join(str(BASE_DIR), "dest", "urls.txt")

    @property
    def SINGLE_SONG_URLS_FILE_PATH(self) -> str:
        return os.path.join(str(BASE_DIR), "dest", "single_song_urls.txt")

    @property
    def YDL_OPTIONS_FOR_PLAYLIST(self) -> dict:
        return {
            "format": self.YDL_FORMAT,
            "extractaudio": self.YDL_EXTRACTAUDIO,
            "audioformat": self.YDL_AUDIOFORMAT,
            "outtmpl": os.path.join(self.MUSIC_PATH, "%(id)s", f"%(id)s.{self.YDL_AUDIOFORMAT}")
        }

    @property
    def YDL_OPTIONS_FOR_SONGS(self) -> dict:
        return {
            "format": self.YDL_FORMAT,
            "extractaudio": self.YDL_EXTRACTAUDIO,
            "audioformat": self.YDL_AUDIOFORMAT,
            "outtmpl": os.path.join(self.MUSIC_PATH, "songs", f"%(title)s.{self.YDL_AUDIOFORMAT}")
        }

    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"), extra='ignore')


settings = Settings()
