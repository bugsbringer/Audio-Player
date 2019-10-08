import web_music
from random import randint


def d_print(d):
    print("{")
    for key, value in d.items():
        print(f'    "{key}": "{value}"')
    print("}")

if __name__ == '__main__':
    items = list(web_music.search('music'))
    print(len(items))

    # shows 5 random items
    for _ in range(5):
        d_print(items[randint(0, len(items))])
