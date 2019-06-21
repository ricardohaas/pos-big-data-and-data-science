import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png'}

#cliente-id
#809d8748bb54bfc7d4804e8876f37bc51b196bec88df98a070b492298ca0fb4b
#secret
#8c5d98cd478c609d574e9a697c6190629608c6264bea020b446818159f4f98fd

def get_links(client_id):
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    req = Request('https://api.unsplash.com/photos/random/', headers=headers, method='GET')
    with urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    return [item['link'] for item in data['data'] if 'type' in item and item['type'] in types]


def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir