import argparse


parser = argparse.ArgumentParser(description="Average")
parser.add_argument('-g', '--grades', action='store',  help=' Your score', type=float, nargs="*")
parser.add_argument('-f', '--float', type=int, default=2)
args = parser.parse_args()
average = sum(args.grades) / len(args.grades)
print(round(average, args.float))
