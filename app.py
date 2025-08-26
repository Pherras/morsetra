from itertools import chain

from dicts import rus_to_morse, nums_to_morse, other_to_morse


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


def main():

    tmp_1 = encode("Привет, мир! 11", rus_to_morse)
    tmp_2 = decode(tmp_1, rus_to_morse)
    print(tmp_1)
    print(tmp_2)


if __name__ == '__main__':
    main()