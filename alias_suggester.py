import sys
from collections import defaultdict

import argparse

parser = argparse.ArgumentParser(description='Suggests aliases from bash history.\n'
                                             'Usage:\n'
                                             '\n'
                                             'cat .bash_history | python3 alias_suggester.py')

parser.add_argument('-o', '--min_occurences', type=int, help='Take only history entries which have at least so many occurences in history. Default 3',
                    default=3)
parser.add_argument('-l', '--max_length', type=int, help='Take only history entries that are no longer than so many characters long. Default 20.', default=20)

args = parser.parse_args()

cost = 4
proposals = defaultdict(int)
occurences = defaultdict(int)

for line in sys.stdin:
    current = ""
    for word in line.split():
        current = current + " " + word
        if len(current) < args.max_length:
            proposals[current] += len(current) - cost
            occurences[current] += 1

for k, v in sorted(proposals.items(), key=lambda p: p[1]):
    if occurences[k] >= args.min_occurences:
        print(v, k)
