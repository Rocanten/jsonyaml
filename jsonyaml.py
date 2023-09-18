# jsonyaml.py v1

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='A program that converts json to yaml and vice versa')

parser.add_argument('command')
parser.add_argument('-i', '--input', help='input file, should contain text with json or yaml structure')

args = parser.parse_args()

print(f'command: {args.command}')
print(f'input: {args.input}')