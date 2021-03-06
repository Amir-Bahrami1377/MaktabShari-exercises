import os
from abc import ABC, abstractmethod
from typing import NoReturn


class Morse(ABC):
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', '\n': '|', ' ': '/',
        ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
    }

    def __init__(self, data: str) -> None:
        self._data = data
        assert self._check()

    @abstractmethod
    def process(self) -> str:
        """
        Tabdil mikne data ro be codinge morede nazar!
        """
        pass

    @abstractmethod
    def _check(self) -> bool:
        """
        Check mikne ke data qabele estefade baraie ma hast!!!
        :param data:
        """
        pass

    def save_file(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.process())

    @classmethod
    def from_file(cls, file_path):
        """
        Sakhtane yek nemoone ba estefade az file!
        :param file_path:
        :return:
        """
        with open(file_path) as f:
            data = f.read()
            return cls(data)  # MorseEncoder / MorseDecoder

    def str(self):
        return self.process()


class MorseEncoder(Morse):

    def __init__(self, data: str) -> None:
        super().__init__(data)

    def process(self) -> str:
        res = ""
        for c in self._data.replace('  ', ' '):
            res += self.MORSE_CODE_DICT[c.upper()] + ' '
        return res

    def _check(self):
        return all(
            map(
                lambda s: s.isalnum() and s.isascii(),
                self._data.split()
            )
        )

    def play(self):
        morse = self.process()
        for i in morse:
            if i == "-":
                os.system("(speaker-test -t sine -f 1000 ) & pid=$! ; sleep 0.5 ;kill -9 $pid")
            elif i == ".":
                os.system("(speaker-test -t sine -f 200 ) & pid=$! ; sleep 0.5 ;kill -9 $pid")
            os.system("clear")


class MorseDecoder(Morse):
    def __init__(self, data: str) -> NoReturn:
        super().__init__(data)

    def process(self) -> str:
        res = ""
        for i in self._data.split():
            for j in Morse.MORSE_CODE_DICT.keys():
                if Morse.MORSE_CODE_DICT[j] == i:
                    res += j
        return res

    def _check(self) -> bool:
        return all(
            map(
                lambda x: x in self.MORSE_CODE_DICT.values(),
                self._data.split()
            )
        )


e = MorseEncoder("Salam Akbar\nReza")
text = e.process()
print(text)
