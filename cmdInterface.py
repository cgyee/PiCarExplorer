import argparse

parse = argparse.ArgumentParser(prog='cmdInterface')
parse.add_argument('-s')
print(parse.parse_args())