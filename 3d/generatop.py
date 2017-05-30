#!/usr/bin/env python3
import random
import re
from sys import stdin
import argparse

TOKEN_EXPRESSION = r'(\d+|[^\W\d_]+|\s+|\W)'

WORDS_EXPRESSION = r'([^\W\d_]+)'


def tokenize(line):
    tokens = [token for token in re.split(TOKEN_EXPRESSION, line) if token != '']
    return tokens


def words(line):
    return re.findall(WORDS_EXPRESSION, line)


class Chain:
    def __init__(self, text_tokens, depth):
        self.depth = depth
        self.chain = dict()
        self.text_tokens = text_tokens
        if depth == 0:
            self.make_zero_chain()
        else:
            self.make_chain()

    def make_zero_chain(self):
        dictionary = dict()
        number_of_words = 0
        for i in range(len(self.text_tokens)):
            for word in self.text_tokens[i]:
                if word not in dictionary.keys():
                    dictionary[word] = 0
                dictionary[word] += 1
                number_of_words += 1
        self.chain[''] = dict()
        for word in dictionary.keys():
            self.chain[''][word] = float(dictionary[word]) / number_of_words

    def make_chain(self):
        for line in self.text_tokens:
            for j in range(self.depth, len(line)):
                sub_string = ' '.join(line[j - self.depth:j])
                regular_expression = ' ' + sub_string + ' ([^\W\d_]+)'
                words_after_pattern = re.findall(regular_expression, ' ' + ' '.join(line))
                if len(words_after_pattern) != 0:
                    if sub_string not in self.chain.keys():
                        self.chain[sub_string] = dict()
                    for word in words_after_pattern:
                        if word not in self.chain[sub_string].keys():
                            self.chain[sub_string][word] = 0
                        self.chain[sub_string][word] += 1
            for pattern in self.chain.keys():
                for word in self.chain[pattern]:
                    self.chain[pattern][word] = (float(self.chain[pattern][word]) /
                                                 len(self.chain[pattern]))

    def __str__(self):
        result = list()
        pattern = '  %s: %.3f'
        for sub_string in sorted(self.chain.keys()):
            result.append(sub_string)
            for word in sorted(self.chain[sub_string]):
                probability = self.chain[sub_string][word]
                result.append(pattern % (word, probability))
        return '\n'.join(result)


class Generator:
    def __init__(self, text, max_depth):
        self.depth = 0
        self.max_depth = max_depth
        self.chains = list()
        self.text = text
        self.is_fitted = False

    def fit(self):
        self.is_fitted = True
        for i in range(self.depth, self.max_depth + 1):
            self.next_chain()

    def next_chain(self):
        assert self.is_fitted, "Not Fitted"
        self.chains.append(Chain(self.text, self.depth))
        self.depth += 1

    def __str__(self):
        assert self.is_fitted, "Not Fitted"
        concatenation = dict(self.chains[0].chain)
        for i in range(1, self.depth):
            concatenation.update(self.chains[i].chain)
        result = list()
        pattern = '  %s: %.2f'
        for sub_string in sorted(concatenation.keys()):
            result.append(sub_string)
            for word in sorted(concatenation[sub_string]):
                probability = concatenation[sub_string][word]
                result.append(pattern % (word, probability))
        return '\n'.join(result)

    def generate_next(self, prefix):
        assert self.is_fitted, "Not Fitted"
        depth = min(len(prefix), self.max_depth)
        previous_words = ' '.join(prefix[-depth:])
        if previous_words in self.chains[depth].chain.keys():
            after_words = self.chains[depth].chain[previous_words].keys()
            return self.choose_world(after_words, depth, previous_words)
        else:
            return None

    def choose_world(self, after_words, depth, previous_words):
        choice = random.uniform(0, 1)
        cumulative_summ = 0
        for word in after_words:
            cumulative_summ += self.chains[depth].chain[previous_words][word]
            if choice <= cumulative_summ:
                return word

    def generate(self, length):
        assert self.is_fitted, "Not Fitted"
        result = list()
        for i in range(length):
            begin = max(0, i - self.depth)
            next = self.generate_next(result[begin:])
            if next is None:
                break
            result.append(next)
        return ' '.join([result[0].title()].__add__(result[1:])) + '.'


class Test:
    def __init__(self):
        print(self.test_tokenize())
        print(self.test_generate())
        print(self.test_probabilities())

    def test_tokenize(self):
        tokenized = ['Hello', ',', ' ', 'world', '!']
        if tokenize('Hello, world!') != tokenized:
            print(tokenize('Hello, world!'))
            return False
        return True

    def test_probabilities(self):
        text = [['First', 'test', 'sentence'],
                ['Second', 'test', 'line']]
        result = '\n  First: 0.17\n' \
                 + '  Second: 0.17\n' \
                 + '  line: 0.17\n' \
                 + '  sentence: 0.17\n' \
                 + '  test: 0.33\n' \
                 + 'First\n' \
                 + '  test: 1.00\n' \
                 + 'Second\n' \
                 + '  test: 1.00\n' \
                 + 'test\n' \
                 + '  line: 0.50\n' \
                 + '  sentence: 0.50'
        chain = Generator(text, 1)
        chain.fit()
        if str(chain) != result:
            print(chain)
            print()
            print(result)
            return False
        return True

    def test_generate(self):
        text = [['First', 'test', 'sentence'],
                ['Second', 'test', 'line']]
        chain = Generator(text, 1)
        chain.fit()
        results = ['First test.', 'Test sentence.',
                   'Second test.', 'Test line.',
                   'Line.', 'Sentence.']
        generated = chain.generate(2)
        if generated not in results:
            print(generated)
            return False
        return True


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='which')

    tokenize_parser = subparsers.add_parser('tokenize')

    test_parser = subparsers.add_parser('test')

    probabilities_parser = subparsers.add_parser('probabilities')
    probabilities_parser.add_argument('--depth', nargs='?', type=int, default=0)

    generate_parser = subparsers.add_parser('generate')
    generate_parser.add_argument('--depth', nargs='?', type=int, default=0)
    generate_parser.add_argument('--size', nargs='?', type=int, default=0)

    args = parser.parse_args(input().split())

    if args.which == 'tokenize':
        line = input()
        tokens = tokenize(line)
        print('\n'.join(tokens))
    elif args.which == 'probabilities':
        text = list()
        for line in stdin:
            text.append(words(line))
        chain = Generator(text, args.depth)
        chain.fit()
        print(chain)
    elif args.which == 'generate':
        text = list()
        for line in stdin:
            text.append(words(line))
        chain = Generator(text, args.depth)
        chain.fit()
        print(chain.generate(args.size))
    elif args.which == 'test':
        Test()


if __name__ == '__main__':
    main()
