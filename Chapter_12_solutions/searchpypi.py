#! python3

# searchpypi.py - Opens several search results

import requests, bs4, webbrowser, sys

print('Searching...')   # Display text while downloading the search results

# res stands for response
res = requests.get('https://pypi.org/search?q=' + \
' '.join(sys.argv[1:]))

try:
    res.raise_for_status()  # Check if status is ok (200)
except Exception as exc:
    print(f'There was a problem fetching the website: {exc}')

# Retrieve top search results links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

