import aiohttp
import asyncio
import unicodedata
import os


def save(filepath, data):
    # remove bad path characters from file name
    *path, file = filepath.split('/')

    bad_pat = r'<>:"/\|?*'
    for item in bad_pat:
        file = file.replace(item, '')

    filepath = '/'.join([*path, file])

    # protects files from rewriting
    if os.path.exists(f"{filepath}.mp3"):
        i = 1
        while os.path.exists(f"{filepath} ({i}).mp3"):
            i += 1
        filepath = f"{filepath} ({i})"

    with open(f"{filepath}.mp3", 'wb') as file:
        file.write(data)


async def download(filepath, url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        save(filepath, data)


async def downloader(info_list, directory):
    tasks = []

    async with aiohttp.ClientSession() as session:
        for data in info_list:
            url = data['url']
            title = unicodedata.normalize('NFC', data['title'])
            filepath = directory + '/' + title
            tasks.append(asyncio.create_task(download(filepath, url, session)))

        await asyncio.gather(*tasks)


def start(info_list, directory = '.'):
    """fast async downloader"""
    asyncio.run(downloader(info_list, directory))
