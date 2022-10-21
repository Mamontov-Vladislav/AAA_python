from one_hot_encoder import fit_transform

def test_mpt():
    corpus = []
    expected = []
    actual = fit_transform(corpus)
    assert expected == actual


def test_in():
    corpus = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(corpus)
    expected_line = ('Moscow', [0, 0, 1])
    assert expected_line in actual


def test_corpus():
    corpus = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(corpus)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_raise():
    corpus = 'Moscow'
    try:
        fit_transform(corpus)
    except TypeError as e:
        assert e
