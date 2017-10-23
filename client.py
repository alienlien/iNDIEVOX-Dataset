#!/usr/bin/env python
import json
import requests

PROFILE_URL = 'https://www.indievox.com/api/mir/song/profile/'
FEATURE_URL = 'https://www.indievox.com/api/mir/song/feature/'
APP_ID = 'P300000045'
APP_SECRET = '9bdecdb004682865260c9d2a5cc71f0d'
SONG_ID = '33156'


class IndievoxClient(object):
    def __init__(self,
                 app_id=APP_ID,
                 app_secret=APP_SECRET,
                 profile_url=PROFILE_URL,
                 feature_url=FEATURE_URL):
        self.app_id = app_id
        self.app_secret = app_secret
        self.profile_url = profile_url
        self.feature_url = feature_url

    def get_profile(self, song_id):
        return get(song_id, self.app_id, self.app_secret, self.profile_url)

    def get_feature(self, song_id):
        return get(song_id, self.app_id, self.app_secret, self.feature_url)


def get(song_id, app_id, app_secret, url):
    params = {
        'app_id': app_id,
        'app_secret': app_secret,
    }
    # TODO: Add error handling for http requests.
    result = requests.get('{}/{}'.format(url, song_id), params=params)
    return result.json()


if __name__ == '__main__':
    client = IndievoxClient(
        app_id=APP_ID,
        app_secret=APP_SECRET,
        profile_url=PROFILE_URL,
        feature_url=FEATURE_URL)

    prof = client.get_profile(SONG_ID)
    print(json.dumps(prof, indent=2, ensure_ascii=False))
    feature = client.get_feature(SONG_ID)
    print(json.dumps(feature, indent=2, ensure_ascii=False))
