# Содержание
1. [Installation](#installation)
1. [Configuration](#configuration)
1. [Example](#example)

---

# Installation <a id="installation"></a>
  
1. `git clone https://github.com/kravasos5/MusicDownloader`
2. Создать виртуальную среду
    1. `python3 -m venv ./venv`
    2. Активировать виртуальную среду командой
    `venv\Scripts\activate.bat` для Windows
    Или `source venv/bin/activate` для Linux и MacOS.
3. `pip install -r requirements.txt`
4. В корне создать **.env** файл с настройками, например:
```
      SONG_FORMAT=mp3
      YDL_FORMAT=bestaudio/best
      YDL_EXTRACTAUDIO=True
      YDL_AUDIOFORMAT=mp3
      DEFAULT_THREADS_COUNT=10
```

   Где `SONG_FORMAT` это формат сохраняемых аудиозаписей

   `YDL_FORMAT` это формат скачиваемого ресурса

   `YDL_EXTRACTAUDIO` эта настройка говорит скачивать только аудио

   `YDL_AUDIOFORMAT` это формат скачиваемого с ютуба видео, в данном случае качается только аудио, так что выбран формат **.mp3**

   `DEFAULT_THREADS_COUNT` это количество потоков

--- 

# Последние штрихи <a id="configuration"></a>
Для работы необходимо занести ссылки на ютуб плейлисты в файлы `single_song_urls.txt` и `urls.txt`.
Эти файлы должны находиться в директории `...\MusicDownloader\dest`.
---

# Пример <a id="example"></a>
Занесём в файл `...\MusicDownloader\dest\single_song_urls.txt` несколько ссылок.
Должно быть примерно так:

```
http://youtube.com/watch?v=CogOs2jMnGI
http://youtube.com/watch?v=rMnXhAFW0vc
```

Теперь запускаем `download_songs.py`, чтобы скачать эти 2 песни, они будут доступны в директории `...\MusicDownloader\dest\music\songs`

Если нужно скачать треки из плейлистов, то добавляем ссылки в файл `...\MusicDownloader\dest\urls.txt`

После этого запускаем `playlists_cutter.py`. И всё. Однако песни сохранятся в директории `...\MusicDownloader\dest\music\{playlist_id}\{track_name}`

Где `playlist_id` это id youtube-видео, а `track_name` это название трека, оно будет сохранено без специальных символов.