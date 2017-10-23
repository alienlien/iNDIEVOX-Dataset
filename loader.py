#!/usr/bin/env python
import json
import logging
import os
import os.path
import leveldb
from client import IndievoxClient

DB_DIR = './data.db'


class Loader(object):
    def __init__(self, db_dir):
        if not os.path.exists(db_dir):
            os.mkdir(db_dir)

        db = leveldb.LevelDB(db_dir)
        self.db = db

    def set(self, sid, data):
        self.db.Put(sid, json.dumps(data))

    def get(self, sid):
        try:
            data = self.db.Get(sid)
            return json.loads(data)
        except Exception as e:
            logging.error('No song data for ID {}: {}'.format(sid, e))
            return {}


if __name__ == '__main__':
    loader = Loader(db_dir=DB_DIR)
    client = IndievoxClient()
    sid = '33156'
    profile = client.get_profile(sid)
    feature = client.get_feature(sid)
    data = {
        'profile': profile,
        'feature': feature,
    }
    loader.set(sid, data)
    data_2 = loader.get(sid)
    print(json.dumps(data_2, indent=2, ensure_ascii=False))
    print(loader.get('no_such_song_id'))
