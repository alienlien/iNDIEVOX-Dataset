#!/usr/bin/env python
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

TRAIN_DATASET_FILE = './dataset/emotion_combine_song_train.dataset'
TEST_DATASET_FILE = './dataset/emotion_combine_song_test.dataset'

if __name__ == '__main__':
    train_data = np.loadtxt(TRAIN_DATASET_FILE)
    test_data = np.loadtxt(TEST_DATASET_FILE)
    train_data_in, train_data_out = np.split(train_data, [-1], axis=1)
    test_data_in, test_data_out = np.split(test_data, [-1], axis=1)

    classifier = SVC(C=1000.0, kernel='rbf')

    num_samples = train_data.shape[0]
    classifier.fit(train_data_in, train_data_out.reshape(num_samples, ))
    scores = cross_val_score(
        classifier, train_data_in, train_data_out.reshape(
            num_samples, ), cv=5)
    print('>> [Train] Scores:', scores)
    print('>> [Train] Accuracy: %0.3f (+/- %0.3f)' % (scores.mean(),
                                                      scores.std() * 2))
    print('>> [Test] Accuracy:',
          accuracy_score(test_data_out, classifier.predict(test_data_in)))
