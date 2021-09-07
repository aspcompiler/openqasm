import sys
import timeit

from open_node.parser.antlr.qasm_parser import parse

def parse_file(file_name):
    with open(file_name, 'r') as f:
        return parse(f.read())

if __name__ == "__main__":
    file_name = sys.argv[1]
    t = timeit.Timer(lambda: parse_file(file_name))

    print("Parsing {} took {} seconds".format(file_name, t.timeit(1)))