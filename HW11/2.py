import argparse
import requests
from bs4 import BeautifulSoup

if name == 'main':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', action="store")
    parser.add_argument('-w', '--word', action='store', type=str)
    parser.add_argument('-a', '--addres', action='store')
    args = parser.parse_args()
    page = requests.get(f"{args.url}")
    soup = BeautifulSoup(page.content, "html.parser")
    h1s = soup.find_all(f"{args.word}")
    res = str(list(h1.text for h1 in h1s))
    with open(f"{args.addres}", 'w') as f:
        f.write(res)