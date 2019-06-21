from redis import Redis
from rq import Queue
import json
from pathlib import Path
from urllib.request import urlopen, Request
import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def main():
    q = Queue(connection=Redis(host='localhost', port=6379))
    result = q.enqueue(
        count_words_at_url, 'http://nvie.com')

if __name__ == '__main__':
    main()