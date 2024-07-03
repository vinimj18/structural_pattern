class Singleton(type):
    _instance: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = 'Tema Escuro'
        self.font_size = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)
    as2 = AppSettings()
    print(as2.tema)
    as3 = AppSettings()
    print(as3.tema)

    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
