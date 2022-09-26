#! python3
# downloadXkcd.py - Downloads every single Xkcd comic.

import requests, bs4, os

url = 'https://xkcd.com'                # starting URL
os.makedirs('xkcd', exist_ok = True)   # store comics in ./xkcd
while not url.endswith('#'):

    # Download the page.
    print('Downloading page %s...' % url)       # %s stoji za string
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print(f'Something went wrong when fetching the website: {exc}')
    # Create a Beautiful Soup object
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the url of the comic image.
    imageElem = soup.select('div #comic > img')
    if imageElem == []:
        print('Could not find comic image.')
    else:
        imageUrl = 'https:' + imageElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (imageUrl))
        res = requests.get(imageUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # TODO: Get the previous button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
