#!/usr/bin/env python3
from mask_gpu import __version__
import argparse

from mask_gpu import get_available_gpus
from mask_gpu import mask_unused_gpus


def main():
    parser = argparse.ArgumentParser(prog='mask-gpu', description='Mask GPUs and expose only necessary GPUs so tensorflow will not use them')
    sp = parser.add_mutually_exclusive_group()
    sp.add_argument('-i', '--info', action='store_true', help='show free gpu with minimum available specified memory')
    sp.add_argument('-e', '--expose', default=1, type=int, help='number of free GPUs to expose (or leave unmasked)', metavar='')
    parser.add_argument('-m', '--min-memory', default=1024, type=int, help='minimum memory to consider a GPU free', metavar='')
    parser.add_argument('-v', '--version', action='version',
                                version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()

    if(args.info): get_available_gpus(min_memory=args.min_memory)
    else: mask_unused_gpus(expose=args.expose, min_memory=args.min_memory)


if __name__ == '__main__':
    main()
