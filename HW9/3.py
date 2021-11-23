import translators as ts


text = input("type your text: \n")


def translator(func):

    def inner(item):
        f = func(item)
        translated = ts.google(f, to_language="fa")
        return translated
    return inner


@translator
def begir(txt):
    return f"{txt}"


print(begir(text))
