
from itertools import chain

from dicts import rus_to_morse, nums_to_morse, other_to_morse, eng_to_morse
from txt import read_file, write_file

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'

def encode(text, lang_dict):
    result = []
    for char in chain.from_iterable(text.lower()):
        if char in lang_dict:
            result.append(lang_dict[char])
        elif char in nums_to_morse:
            result.append(nums_to_morse[char])
        elif char in other_to_morse:
            result.append(other_to_morse[char])
        else:
            result.append(char)
        result.append(' ')
    return ''.join(result)

def decode(code, lang_dict):
    result = []
    lang_reversed = {v: k for k, v in lang_dict.items()}
    nums_reversed = {v: k for k, v in nums_to_morse.items()}
    other_reversed = {v: k for k, v in other_to_morse.items()}

    for el in code.split(' '):
        if el in lang_reversed:
            result.append(lang_reversed[el])
        elif el in nums_reversed:
            result.append(nums_reversed[el])
        elif el in other_reversed:
            result.append(other_reversed[el])
        else: result.append(el)

    return ''.join(result)

def choice(mode_conv: str, lang: str, input = INPUT_FILE, output = OUTPUT_FILE):
    """Выбрать режим и язык, дополнительно можно указать входной и выходной файлы.
    Подходящие режимы: 'encode', 'decode'.
    Подходящие языки: 'rus', 'eng'."""
    code = None
    text = read_file(input)
    if mode_conv == "encode":
        if lang == "rus":
            code = encode(text, rus_to_morse)
        else: code = encode(text, eng_to_morse)
    else:
        if lang == "rus":
            code = decode(text, rus_to_morse)
        else: code = decode(text, eng_to_morse)

    write_file(code, output)



def main():
    choice(mode_conv = 'encode', lang = 'rus')



if __name__ == '__main__':
    main()