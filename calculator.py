#by you know who kkkkkkkk

import interpreter

print("Enter your expressions to be calculated.'Exit' to exit.")
expression = ""
tokenizer = interpreter.Tokenizer()
parser= interpreter.parseTree()
interpr = interpreter.interpreter()
while True:
    expression = input('> ')
    if expression != "Exit":
        try:
            result = interpr.evaluate(parser.buildParseTree(tokenizer.tokenize(expression)))
            print(result)
            print(result)
        except Exception as e:
            print(e)
    else:
        break

print("Good calculator!")