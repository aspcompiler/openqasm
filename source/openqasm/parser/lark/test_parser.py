import logging

from lark import (
        Lark,
        Transformer,
        v_args,
        logger)

logger.setLevel(logging.DEBUG)

class ASTGenerator(Transformer):
    """
    Class for generating OpenQASM3 reference Python AST.
    """
    
    def index_identifier(self, items):
        return list(items)
    
with open("test.lark", "r") as grammar_file:
    test_grammar = grammar_file.read()

test_parser = Lark(test_grammar,
                   parser='lalr',
                   start="index_identifier",
                   propagate_positions=False,
                   maybe_placeholders=False,
                   regex=True,
                   debug=True)
                   # transformer=ASTGenerator())

with open("test_file.txt") as test_file:
    source = test_file.read()

test_parser.parse(source)
