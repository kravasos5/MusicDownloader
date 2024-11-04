from src.config.config import settings
from src.music_cutter import MusicCutter

if __name__ == "__main__":
    music_cutter = MusicCutter(settings=settings)
    music_cutter.download_songs()
