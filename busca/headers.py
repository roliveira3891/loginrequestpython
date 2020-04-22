import os
def header():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'origen': os.getenv('ORIGEM'),
        'referer': os.getenv('REFERER'),
        'sec-fetch-mode' : 'cors',
        'sec-fetch-site' : 'cross-site'
    }

    return headers