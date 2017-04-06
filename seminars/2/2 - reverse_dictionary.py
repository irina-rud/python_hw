import sys


def reverse_dictionary(dictionary):
    result = {}
    for key, values in dictionary.items():
        for value in values:
            if value not in result:
                result[value] = [key]
            else:
                result[value].append(key)
    return result


def parse_dictionary(text):
    result = {}
    for line_raw in text.split('\n'):
        line = line_raw.strip()
        if len(line) == 0:
            continue

        key_str, values_str = line.split('-')

        key = key_str.strip()
        values = [val_str.strip() for val_str in values_str.split(',')]

        result[key] = values
    return result


def print_dictionary(dictionary):
    for key in sorted(dictionary):
        print key + ' - ' + ', '.join(dictionary[key])


def main():
    text = sys.stdin.read()
    base_dictionary = parse_dictionary(text)
    reversed_dictionary = reverse_dictionary(base_dictionary)
    print_dictionary(reversed_dictionary)


main()
