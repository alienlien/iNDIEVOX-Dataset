#!/usr/bin/env python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

TRAIN_DATASET_FILE = './dataset/emotion_combine_song_train.dataset'
TEST_DATASET_FILE = './dataset/emotion_combine_song_test.dataset'

if __name__ == '__main__':
    train_data = np.loadtxt(TRAIN_DATASET_FILE)
    test_data = np.loadtxt(TEST_DATASET_FILE)
    train_data_in, train_data_out = np.split(train_data, [-1], axis=1)
    test_data_in, test_data_out = np.split(test_data, [-1], axis=1)

    classifier = DecisionTreeClassifier(criterion='entropy')
    classifier.fit(train_data_in, train_data_out)
    score = classifier.score(train_data_in, train_data_out)
    print('>> Score:', classifier.score(test_data_in, test_data_out))
    print('>> Accuracy:',
          accuracy_score(test_data_out, classifier.predict(test_data_in)))
