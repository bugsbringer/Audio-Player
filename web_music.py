import requests
from bs4 import BeautifulSoup


def download(url):
    response = requests.get(url)
    return response.content


def search_old(keywords):
    '''yields {"title": title, "author": author, "url": url}'''

    site = "https://megapesni.com"

    params = {
        "do": "search",
        "subaction": "search",
        "story": f"{keywords}"
    }

    response = requests.get(site, params=params)

    soup = BeautifulSoup(response.text, features='html.parser')

    track_div = soup.findAll("div", {"class": "music-popular-wrapper"})
    for item in track_div:
        url = item.find("a", {"class": "popular-play__item"})['href']
        author = item.find("a", {"class": "popular-play-composition"}).text
        title = item.find("a", {"class": "popular-play-author"}).text
        yield {"title": title, "author": author, "url": url}


def search(keywords):
    '''yields {"title": title, "author": author, "url": url}'''
    site = 'https://ru-music.com'

    keywords = keywords.replace(' ', '%20')
    url = f'{site}/search/{keywords}/'

    response = requests.get(url)
    body = BeautifulSoup(response.text, features='html.parser').find("body")

    tracks = body.findAll("li", {"class": "track"})
    for track in tracks:
        info = track.find('h2')
        if info:
            author, title = info.text.replace('\n','').split('–')

            if "https://" not in track['data-mp3']:
                yield {"title": title.strip(), "author": author.strip(), "url": site + track['data-mp3']}

    # worse relevance tracks (just for ru-music.com)
    for track in tracks:
        if "https://" not in track['data-mp3']:
            break

        info = track.find('h2')
        if info:
            author, title = info.text.replace('\n','').split('–')

            yield {"title": title.strip(), "author": author.strip(), "url": track['data-mp3']}
