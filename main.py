import re
import AST
import testCode

def tokenize(code):
    tokens = []

    lines = [line.strip() for line in code.splitlines() if line.strip()]
    print(lines)
    for line in lines:
        for token_type, pattern in AST.TOKENS.items():
            if re.match(pattern, line.lower()):
                tokens.append(AST.UDMLtoken(token_type, line))
                break

    return tokens

def parse(tokens):
    root = AST.Node("Test")
    curr_if = None

    # TODO - подумать 
    # не правильно строятся веточки
    for token in tokens:
        if token.type == "IF":
            curr_if = AST.Node("IF", token.value)
            root.add_node(curr_if)
        elif token.type == "CONDITION" and curr_if:
            condition_node = AST.Node("CONDITION", token.value)
            curr_if.add_node(condition_node)
        elif token.type == "THEN" and curr_if:
            then_node = AST.Node("THEN")
            curr_if.add_node(then_node)
        elif token.type == "TRUE" and curr_if:
            true_node = AST.Node("TRUE", token.value)
            curr_if.children[-1].add_node(true_node)
        elif token.type == "ELSE" and curr_if:
            else_node = AST.Node("ELSE")
            curr_if.add_node(else_node)
        elif token.type == "FALSE" and curr_if:
            false_node = AST.Node("FALSE", token.value)
            curr_if.children[-1].add_node(false_node)

    return root

def main():
    # Запускаем линтер
    tokens = tokenize(testCode.code)
    ast = parse(tokens)

    print(ast)

    obj = {"asdfasd":[1,2,3], "asd":[4,5,6]}
    arr = [1,2,3,4]
    print(arr.sum())
    print("Вот сюда смотри ",obj["asd"][1])

main()