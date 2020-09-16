import argparse
from time import sleep
from string import ascii_lowercase
from string import digits
import requests
import urllib.parse
from datetime import datetime
from http import client
from google.cloud import datastore


class GoogleAutoComplete:
    def __init__(self, test_mode=False, recurse_mode=False):
        self.base_url = 'https://www.google.co.jp/complete/search?'\
                        'hl=ja&output=toolbar&ie=utf-8&oe=utf-8&'\
                        'client=firefox&q='
        self.test_mode = test_mode
        self.recurse_mode = recurse_mode

    def get_suggest(self, query):
        buf = requests.get(self.base_url +
                           urllib.parse.quote_plus(query)).json()
        suggests = [ph for ph in buf[1]]
        print("query: [{0}]({1})".format(query, len(suggests)))
        for ph in suggests:
            print(" ", ph)
        sleep(1)
        return suggests

    def get_suggest_with_one_char(self, query):
        # キーワードそのものの場合のサジェストワード
        ret = self.get_suggest(query)
        return self.get_uniq(ret)

    # 重複を除く
    def get_uniq(self, arr):
        uniq_ret = []
        for x in arr:
            if x not in uniq_ret:
                uniq_ret.append(x)
        return uniq_ret

if __name__ == "__main__":
    phrase = input('検索ワード ---> ')
    # Google Suggest キーワード取得
    gs = GoogleAutoComplete(recurse_mode = "--recure")
    ret = gs.get_suggest_with_one_char(phrase + " ")

    # ファイルに保存する
    #fname = "suggest.csv"
    #with open(fname, 'a') as fs:
    #    for key in ret:
    #        fs.write(key + "\n")
    #    fs.write("------------\n")


# データ追加
def insert(things, check):
    client = datastore.Client()
    key = client.key("Fish")
    entity = datastore.Entity(key=key)
    entity["ans0"]
    entity["ans1"]
    entity["ans2"]
    #for i in range(0,10):
    #    entity["word{i}"] = 
    entity["word0"]
    entity["word1"]
    entity["word2"]
    entity["word3"]
    entity["word4"]
    entity["word5"]
    entity["word6"]
    entity["word7"]
    entity["word8"]
    entity["word9"]
    entity["created"] = datetime.now()
    client.put(entity)
    entity['id'] = entity.key.id
    return entity

# データ取得
def get_all():
    client = datastore.Client()
    query = client.query(kind='TodoList')
    query.order = '-created'
    data = list(query.fetch())
    for entity in data:
        entity['id'] = entity.key.id
    return data

# 指定データの取得
def get_by_id(key_id):
    client = datastore.Client()
    key = client.key('TodoList', int(key_id))
    entity = client.get(key=key)
    if entity:
        entity['id'] = entity.key.id
    return entity

# データの更新
def update(entity):
    if 'id' in entity:
        del entity['id']
    client = datastore.Client()
    client.put(entity)
    entity['id'] = entity.key.id
    return entity

# データの削除
def delete(key_id):
    client = datastore.Client()
    key = client.key('TodoList', int(key_id))
    client.delete(key)