import sys

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorStrategy import DefaultErrorStrategy

from MicroCLexer import MicroCLexer
from MicroCParser import MicroCParser

class MyErrorStrategy(DefaultErrorStrategy):
    def reportError(self, _recognizer, _exception):
        print("Not Accepted")
        exit(1)
    def recoverInline(self, _recognizer):
        print("Not Accepted")
        exit(1)

def main():
    try:
        input_stream = FileStream(sys.argv[1])
        lexer = MicroCLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MicroCParser(token_stream)
        parser._errHandler = MyErrorStrategy()
        _parse_tree = parser.program()
        print("Accepted")
    except FileNotFoundError:
        print("File not found")
        return 1
    return 0
    

if __name__ == "__main__":
    exit(main())