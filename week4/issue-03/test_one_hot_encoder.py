from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_empty(self):
        """
        прверка граничного случая.
        """
        corpus = []
        expected = []
        actual = fit_transform(corpus)
        self.assertEqual(expected, actual)

    def test_In(self):
        """
        хороший тест, если есть большой корпус слов,
        и нужно проверитьпорядок записи слов при трансформе:
        и нет необходимости самому придумывать ожидаемый ответ целиком,
        достаточно проверить одну строчку.
        """
        corpus = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(corpus)
        expected_line = ('Moscow', [0, 0, 1])
        self.assertIn(expected_line, actual)

    def test_corpus(self):
        """
        обычный тест с правильным ответом.
        """
        corpus = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(corpus)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertTrue(actual == expected)

    def test_raise(self):
        corpus = 'Moscow'
        self.assertRaises(TypeError, fit_transform(corpus))
