"""
Copyright 2016, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import argparse
import os

import numpy as np
from matplotlib import pyplot


def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'output',
        help='output file path for created plot(s).'
    )
    parser.add_argument(
        '-s', '--samples',
        nargs='?',
        type=int,
        default=8000,
        help='Number of points on the scatter plot.'
    )
    parser.add_argument(
        '--a4',
        dest='dimensions',
        action='store_const',
        const='a4',
        default='us',
        help='use A4 dimensions instead of US Letter.'
    )
    args = parser.parse_args()
    args.output = os.path.abspath(os.path.expanduser(args.output))

    return args


def main():
    args = command_line_args()

    x_dim, y_dim = (
        (8.5, 11.0)
        if args.dimensions == 'us' else
        (8.27, 11.69)  # A4 dimensions in inches (yuck!).
    )
    samples = args.samples

    x = np.random.rand(1, samples) * x_dim
    y = np.random.rand(1, samples) * y_dim

    fig = pyplot.figure(None, figsize=(x_dim, y_dim), dpi=150)
    axes = fig.add_subplot(111)
    axes.set_xlim([0, x_dim])
    axes.set_ylim([0, y_dim])
    axes.set_axis_off()
    axes.plot(x, y, color='black', marker='o')
    fig.savefig(args.output, bbox_inches='tight')
    print('Scatter plot saved to {dest}'.format(dest=args.output))


if __name__ == '__main__':
    main()
