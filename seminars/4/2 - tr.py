"""Translate symbols from the file using substitution table.

By default the data is read from standard input and written to standard
output.

"""


import argparse
import sys


class TableError(Exception):
    pass


def build_translate_table(symbols_from, symbols_to):
    if len(symbols_from) != len(symbols_to):
        raise TableError("'from' and 'to' lists must have the same length.")

    if len(set(symbols_from)) != len(symbols_from):
        raise TableError("Symbols in 'from' list must be unique.")

    return dict(zip(symbols_from, symbols_to))


def translate(input_text, translate_dict, delete_symbols):

    """Translate symbols in the text using substitution table.

    Arguments:
        input_text - the text to translate
        translate_dict - the dictionary to use for translation
        delete_symbols - the set of symbols to delete comletely
    Return the resulting text as string.

    Note: the symbols in translate_dict and delete_symbols may
    intersect, but the deletion is applied first.

    """

    delete_symbols = set(delete_symbols)

    result_symbols = []
    for symbol in input_text:
        if symbol in delete_symbols:
            continue
        result_symbols.append(translate_dict.get(symbol, symbol))

    return ''.join(result_symbols)


def translate_files(input_file, output_file, translate_dict, delete_symbols):

    """Translate input file to the output file.

    'translate_dict' and 'delete_symbols' are passed to the 'translate'
    function.

    """

    for line in input_file:
        result = translate(line, translate_dict, delete_symbols)
        output_file.write(result)


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__.strip()
    parser.add_argument('-d', '--delete', dest='delete_symbols', default='',
                        metavar='TABLE', help='Symbols to remove completely' +
                                              ' (done before translation)')
    parser.add_argument('symbols_from')
    parser.add_argument('symbols_to')

    args = parser.parse_args()

    try:
        translate_table = build_translate_table(args.symbols_from,
                                                args.symbols_to)
    except TableError as e:
        parser.error(e.message)
        return

    translate_files(sys.stdin, sys.stdout, translate_table,
                    args.delete_symbols)


if __name__ == '__main__':
    main()
