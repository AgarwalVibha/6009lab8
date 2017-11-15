"""6.009 Lab 8A: carlae Interpreter"""

import sys


class EvaluationError(Exception):
    """Exception to be raised if there is an error during evaluation."""
    pass


def tokenize(source):
    """
    Splits an input string into meaningful tokens (left parens, right parens,
    other whitespace-separated values).  Returns a list of strings.

    Arguments:
        source (str): a string containing the source code of a carlae
                      expression
    """
    # print ("original",source)
    result = []
    lines = source.splitlines()
    for line in lines: 
        uncomment = line.split(";")[0]
        # print ("uncommented", uncomment)
        elem = "" #build each word/symbol
        token = False #when true, append to the result list
        for char in uncomment:
            if char == "(" or char == ")":
                if elem:
                    result.append(elem)
                result.append(char)
                # token = False
                elem = ""
            elif char == " ":
                token = True
            else:
                elem +=char
            if token == True:
                if elem: #is not an empty string
                    result.append(elem)
                token = False #reset
                elem = ""
        if elem:
            result.append(elem)
    # print ("result",result)
    return result
# i = 0
def parse(tokens):
    """
    Parses a list of tokens, constructing a representation where:
        * symbols are represented as Python strings
        * numbers are represented as Python ints or floats
        * S-expressions are represented as Python lists

    Arguments:
        tokens (list): a list of strings representing tokens
    """
    i = 0

    def parentheses_match(tokens):
        counter = 0
        for item in tokens:
            if item == "(":
                counter += 1
            if item == ")":
                counter -= 1
                if counter < 0:
                    return False
        return (counter == 0)
    
    def helper(tokens):
        nonlocal i
        parsed = []
        length = len(tokens)
        if len(tokens) == 1:
            i = -1
            length -=1
        while i < length:
            i += 1
            # print (i)
            if tokens[i] == "(":
                parsed.append(helper(tokens))
            elif tokens[i] == ")":
                return (parsed)
            else:
                try:
                    parsed.append(int(tokens[i]))
                except:
                    try:
                        parsed.append(float(tokens[i]))
                    except:
                        parsed.append(tokens[i])
            # elif type(tokens[i]) == int:
            #     parsed.append(int(tokens[i]))
            # else:
            #     parsed.append(tokens[i])
        if len(parsed) == 1:
            return parsed[0]
        return parsed
            
    if not parentheses_match(tokens):
        raise SyntaxError
    # parse_result, extra = helper(tokens)
    return helper(tokens)


carlae_builtins = {
    '+': sum,
    '-': lambda args: -args[0] if len(args) == 1 else (args[0] - sum(args[1:])),
    '*': lambda args: args[0] if len(args) == 1 else (args[0] * carlae_builtins['*'](args[1:])),
    '/': lambda args: args[0] if len(args) == 1 else (args[0] / carlae_builtins['/'](args[1:])),
}


def evaluate(tree):
    """
    Evaluate the given syntax tree according to the rules of the carlae
    language.

    Arguments:
        tree (type varies): a fully parsed expression, as the output from the
                            parse function
    """
    if isinstance(tree, int) or isinstance(tree, float):
        return tree
    elif isinstance(tree, list):
        branch = []
        for item in tree:
            print (item)
            branch.append(evaluate(item))
            print ("branch",branch)
        return branch[0](branch[1:])
    elif tree in carlae_builtins:
        print ("hell ya", tree)
        return carlae_builtins[tree]

    # raise NotImplementedError


if __name__ == '__main__':
    # code in this block will only be executed if lab.py is the main file being
    # run (not when this module is imported)
    do = ""
    while do != "QUIT":
        do = input(">>")
        if do == "QUIT":
            break
        else:
            t = tokenize(do)
            print ("tokenize",t)
            p = parse(t)
            print ("parse",p)
            e = evaluate(p)
            print ("evaluate",e)
