import keyword


class DictToAtr:
    def __init__(self, _dict):
        if 'location' in _dict:
            self.location = DictToAtr(_dict['location'])
            _dict.pop('location')
        keys = list(_dict.keys())
        for key in keys:
            if keyword.iskeyword(key):
                _dict[key + '_'] = _dict.pop(key)
        self.__dict__.update(_dict)


class ColorizeMixin:
    def __str__(self):
        adv_str = self.__repr__()
        color_str = '\033[1;{};1m'
        out = color_str + adv_str
        return out.format(self.repr_color_code, self.title, self.price)


class Advert(ColorizeMixin, DictToAtr):

    repr_color_code = 33

    def __init__(self, _dict):
        if 'price' not in _dict:
            _dict['price'] = 0
        if _dict['price'] < 0:
            raise ValueError('Price must be >= 0')
        super().__init__(_dict)

    def __repr__(self):
        return '{} | {} ₽'.format(self.title, self.price)
