import sys
from enum import Enum
import math

class TokenType(Enum):
    COMMAND = 1
    VALUE = 2


class Token:
    def __init__(self, tokenType, nameCharacters):
        self.tokenType = tokenType
        self.nameCharacters = nameCharacters

    def getString(self):
        return "".join(self.nameCharacters)


code = """
PUSH 5
PUSH 6
EXP
PRINT
"""

# tokenize
offset = 0
tokens = []
currentToken = None
while offset < len(code):
    char = code[offset]
    if char == ' ' or char == '\n' or char == '\r':
        if currentToken is not None:
            tokens.append(currentToken)
            currentToken = None
    elif char.isalpha() and char.isupper():
        if currentToken is None:
            currentToken = Token(TokenType.COMMAND, [])
        currentToken.nameCharacters.append(code[offset])
    elif char.isnumeric:
        if currentToken is None:
            currentToken = Token(TokenType.VALUE, [])
        currentToken.nameCharacters.append(code[offset])

    offset += 1

stack = []

for i in range(len(tokens)):
    token = tokens[i]
    if token.tokenType == TokenType.COMMAND:
        if token.getString() == "PUSH":
            value = tokens[i + 1]
            print(value.getString())
            stack.append(int(value.getString()))  # convert to int
            i += 1  # we visited the push token and the value token, so increment again
        elif stack.__len__() > 1:
            if token.getString() == "ADD":
                # grab two values off the stack, add them, push the result back on the stack
                stack.append(stack.pop() + stack.pop())
                print(stack)
            elif token.getString() == "SUB":
                stack.append(stack.pop() - stack.pop())

            elif token.getString() == "MUL":
                stack.append(stack.pop() * stack.pop())

            elif token.getString() == "DIV":
                stack.append(stack.pop() / stack.pop())

            elif token.getString() == "MOD":
                stack.append(stack.pop() % stack.pop())

            elif token.getString() == "EXP":
                stack.append(math.pow(stack.pop(), stack.pop()))
                print(stack)

    i += 1  # go to the next token
