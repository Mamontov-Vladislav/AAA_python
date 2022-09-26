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


if __name__ == '__main__':
    corgi = {
        'title': 'Вельш-корги',
        'price': 1000,
        'class': 'dogs',
        'location': {
            'address': 'город Москва, Лесная, 7',
            'metro_stations': ['Белорусская']
        }
    }

    negative_price_ad = {
        'title': 'Ничего не делаю',
        'price': -1,
        }

    try:
        bad_ad = Advert(negative_price_ad)
    except ValueError:
        print('выбросислось исключение ValueError')

    corgi_ad = Advert(corgi)

    print(corgi_ad.location.address)

    print(corgi_ad.class_)

    print(corgi_ad)
