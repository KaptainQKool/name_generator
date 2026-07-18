from __init__ import generate
import argparse

parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument('-c', '--count')
parser.add_argument('-s', '--save', action='store_true')
parser.add_argument('-p', '--print', action='store_true')
args = parser.parse_args()
count: int = int(args.count)
save_output: bool = args.save
print_output: bool = args.print

generate(n=count, save_output=save_output, print_output=print_output)