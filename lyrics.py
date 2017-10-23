#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from gensim import corpora, models, similarities
import jieba

DATA_FILE = './dataset/lyrics.dataset'
DICT_FILE = './lyrics.dict'
CORPUS_FILE = './lyrics.mm'
NUM_TOPICS = 100
NUM_FEATURES = 500
TOP_N = 10

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    doc = "望著 滿天星斗 的 塗鴉 好像 看見 自己 童年 的 模樣 總是 說 著 淘氣 浪漫 的 願望 夢想 能夠 飛往 燦爛 的 天堂 而 那天 真的 心願 正 溫柔 地 對 我 說 當你 陷入 絕望 中請 記得 我 用 美麗 的 幻想 讓 真心 永遠 純真 而 不變 當你 寂寞 的 時候 請 想念 我 用 單純 的 信仰 給 自己 溫暖 的 回答 閉上 雙眼 靜靜地 徜徉 彷彿 穿越時空 回到 了 過往 以為 銀河 就 在 不遠 的 前方 星星 月亮 都 在 我 面前 玩耍 而 那 微小 的 喜悅 正 溫柔 地 對 我 說 當你 陷入 絕望 中請 記得 我 用 美麗 的 幻想 讓 真心 永遠 純真 而 不變 當你 寂寞 的 時候 請 想念 我 用 單純 的 信仰 給 自己 溫暖 的 回答 ( 和 童 年時 無邪 的 希望 ) 親愛 的 我 親愛 的 我 願 你 永遠 像 我 一樣 帶著 勇氣 和 倔強 歲月 改變 你 的 模樣 無法 改變 你 的 去向"

    if '\n' in doc or '\r' in doc:
        doc = ' '.join(
            jieba.cut(doc.replace(u'\u3000', ' ').replace(u'\u2028', ' ')))
    print('Doc:', doc)

    dictionary = corpora.Dictionary.load(DICT_FILE)
    corpus = corpora.MmCorpus(CORPUS_FILE)

    tfidf_model = models.TfidfModel(corpus)
    corpus_tfidf = tfidf_model[corpus]

    lsi = models.LsiModel(
        corpus_tfidf, id2word=dictionary, num_topics=NUM_TOPICS)
    corpus_lsi = lsi[corpus_tfidf]
    #     lsi.print_topics(10)

    doc_bow = dictionary.doc2bow(doc.lower().split())
    doc_lsi = lsi[tfidf_model[doc_bow]]

    index = similarities.MatrixSimilarity(
        corpus_lsi, num_features=NUM_FEATURES)

    sims = index[doc_lsi]
    sims = sorted(enumerate(sims), key=lambda item: item[1], reverse=True)
    print(sims[:TOP_N])
