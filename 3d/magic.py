#!/usr/bin/env python3
from sys import stdin
import argparse

colors = '@%#*+=-:. '


def to_str(pic):
    res = list()
    for i in range(len(pic)):
        str = ''.join(pic[i])
        res.append(str)
    return '\n'.join(res)


def chop_right(pic, x):
    for i in range(len(pic)):
        pic[i] = pic[i][:-x]
    return pic


def chop_top(pic, x):
    return pic[x:]


def chop_bottom(pic, x):
    return pic[:-x]


def chop_left(pic, x):
    for i in range(len(pic)):
        pic[i] = pic[i][x:]
    return pic


def rotate(pic, x):
    x %= 4
    for rot in range(x):
        res = list()
        for i in range(len(pic[0])):
            line = list()
            for j in range(len(pic)):
                line.append(pic[j][-1-i])
            res.append(line)
        pic = res
    return pic


def expose(pic, x):
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            y = colors.find(pic[i][j])
            pic[i][j] = colors[min(y + x, len(colors) - 1)]
    return pic


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    crop_parser = subparsers.add_parser("crop")
    crop_parser.set_defaults(which='crop')
    crop_parser.add_argument("-l", "--left", nargs='?', type=int, default=0)
    crop_parser.add_argument("-r", "--right", nargs='?', type=int, default=0)
    crop_parser.add_argument("-t", "--top", nargs='?', type=int, default=0)
    crop_parser.add_argument("-b", "--bottom", nargs='?', type=int, default=0)

    expose_parser = subparsers.add_parser("expose")
    expose_parser.set_defaults(which='expose')
    expose_parser.add_argument("power", type=int, default=0)

    rotate_parser = subparsers.add_parser("rotate")
    rotate_parser.set_defaults(which='rotate')
    rotate_parser.add_argument("angle", type=int, default=0)

    args = parser.parse_args(input().split())
    picture = list()
    for line in stdin:
        if line[-1] == '\n':
            line = line[:-1]
        next_str = list(line)
        picture.append(next_str)

    if args.which == 'crop':
        if args.left > 0:
            picture = chop_left(picture, args.left)
        if args.right > 0:
            picture = chop_right(picture, args.right)
        if args.top > 0:
            picture = chop_top(picture, args.top)
        if args.bottom > 0:
            picture = chop_bottom(picture, args.bottom)
    elif args.which == 'expose':
        if args.power != 0:
            picture = expose(picture, args.power)
    elif args.which == 'rotate':
        if args.angle > 0:
            picture = rotate(picture, args.angle // 90)

    print(to_str(picture))

if __name__ == '__main__':
    main()
