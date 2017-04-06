#!/usr/bin/env python3
from sys import stdin


def main():
    dictionary = dict()
    is_dict = True
    languages = set()
    for line in stdin:
        if is_dict:
            if len(line.strip()) == 0:
                is_dict = False
            else:
                lang, chars = line.split()[:2]
                languages.add(lang)
                for ch in chars:
                    dictionary[ch] = lang
        else:
            if (len(line.strip()) != 0) and (len(languages) != 0):
                res = set()
                for word in line.split():
                    word = word.lower()
                    counter = dict()
                    for lang in languages:
                        counter[lang] = 0
                    for ch in word:
                        if ch in dictionary.keys():
                            counter[dictionary[ch]] += 1
                    max_ch = 0
                    max_lang = ''
                    for lang in languages:
                        if counter[lang] > max_ch:
                            max_ch = counter[lang]
                            max_lang = lang
                        elif counter[lang] == max_ch:
                            if max_lang > lang:
                                max_lang = lang
                    res.add(max_lang)
                print(' '.join([w for w in sorted(res) if len(w) != 0]))

if __name__ == '__main__':
    main()
