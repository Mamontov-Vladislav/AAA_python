class CountVectorizer:
"""
Преобразует текстовые данные в числовую матрицу по принципу составления терм-документой матрицы.
"""
    def __init__(self):
        self._features = {}

    def fit_transform(self, text: list) -> list:
        term_matr = []
        for line in text:
            for word in line.lower().split(' '):
                self._features[word] = None
        for line in text:
            line_term = []
            for elem in self._features:
                line_term.append(line.lower().count(elem))
            term_matr.append(line_term)
        return term_matr

    def get_feature_names(self) -> list:
        return list(self._features)


if __name__ == '__main__':
