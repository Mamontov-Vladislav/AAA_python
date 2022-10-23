import keyword


class DictToAtr:
    def __init__(self, lib):
        keys = list(lib.keys())
        for key in keys:
            if isinstance(lib[key], dict):
                setattr(self, key, DictToAtr(lib[key]))
            elif keyword.iskeyword(key):
                setattr(self, key + '_', lib[key])
            else:
                setattr(self, key, lib[key])


class ColorizeMixin:
    def __str__(self):
        adv_str = self.__repr__()
        color_str = '\033[1;{};1m'
        out = color_str + adv_str
        return out.format(self.repr_color_code, self.title, self.price)


class Advert(ColorizeMixin, DictToAtr):

    repr_color_code = 33

    def __init__(self, lib):
        if 'price' not in lib:
            lib['price'] = 0
        if lib['price'] < 0:
            raise ValueError('Price must be >= 0')
        super().__init__(lib)

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

    print(corgi_ad.location)

    print(corgi_ad)
