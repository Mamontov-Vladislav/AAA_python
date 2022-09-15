class CountVectorizer:

    def __init__(self):
        self._features = set()

    def fit_transform(self, text):
        term_matr = []
        for line in text:
            for word in line.lower().split(' '):
                if word not in self._features:
                    self._features.add(word)
        for line in text:
            line_term = []
            for elem in self._features:
                line_term.append(line.lower().count(elem))
            term_matr.append(line_term)
        return term_matr

    def get_feature_names(self):
        return list(self._features)
