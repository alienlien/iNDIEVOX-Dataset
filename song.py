#!/usr/bin/env python
import json
import requests

SONG_PROFILE_URL = 'https://www.indievox.com/api/mir/song/profile/'
APP_ID = 'P300000045'
APP_SECRET = '9bdecdb004682865260c9d2a5cc71f0d'
SONG_ID = '110740'


def get_profile(song_id,
                profile_url=SONG_PROFILE_URL,
                app_id=APP_ID,
                app_secret=APP_SECRET):
    params = {
        'app_id': app_id,
        'app_secret': app_secret,
    }
    # TODO: Add error handling for http requests.
    result = requests.get('{}/{}'.format(profile_url, song_id), params=params)
    return result.json()


if __name__ == '__main__':
    prof = get_profile(SONG_ID)
    print(json.dumps(prof, indent=2, ensure_ascii=False))
