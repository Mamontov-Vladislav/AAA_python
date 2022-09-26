class CountVectorizer:

    def __init__(self):
        self._features = dict()

    def fit_transform(self, text):
        term_matr = []
        for line in text:
            for word in line.lower().split(' '):
                if word not in self._features:
                    self._features[word] = None
        for line in text:
            line_term = []
            for elem in self._features.keys():
                line_term.append(line.lower().count(elem))
            term_matr.append(line_term)
        return term_matr

    def get_feature_names(self):
        return list(self._features)


if __name__ == '__main__':
    empty_corpus = []

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(empty_corpus)

    true_count_matrix = []

    features = vectorizer.get_feature_names()

    true_features = []

    if features == true_features:
        print('get_features method, test 1: OK')
    else:
        print('get_features method, test 1: FAILED')

    if count_matrix == true_count_matrix:
        print('transform method,    test 1: OK')
    else:
        print('transform methodtest, test 1: FAILED')

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    true_count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    features = vectorizer.get_feature_names()

    true_features = ['crock', 'pot', 'pasta', 'never',
                     'boil', 'again', 'pomodoro', 'fresh',
                     'ingredients', 'parmesan', 'to', 'taste']

    if features == true_features:
        print('get_features method, test 2: OK')
    else:
        print('get_features method, test 2: FAILED')

    if count_matrix == true_count_matrix:
        print('transform method,    test 2: OK')
    else:
        print('transform methodtest 2: FAILED')
