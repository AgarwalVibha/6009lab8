scraps

def helper(tokens, i = 0):
        parsed = []
        # for i in range(len(tokens)):
        print ("len",len(tokens))
        while i < len(tokens):
            print ("leggooo")
            print ("idex", i, tokens[i])
            if tokens[i] == "(":
                # print(tokens[i+1],"open")
                toadd, i = helper(tokens, i+1)
                print("add to list", toadd, i)
                parsed.append(toadd)
                # parsed.append(helper(tokens, i+1))
                # parsed.append(helper(tokens[i+1:]))
            if tokens[i] == ")":
                # print (parsed, i+1)
                return (parsed, i+1)
            if type(tokens[i]) == int:
                parsed.append(int(tokens[i]))
            else:
                parsed.append(tokens[i])
            i += 1
            print ("!!!",parsed)
        print ("returning", parsed)
        return parsed, i

    if not parentheses_match(tokens):
        raise SyntaxError
    parse_result, extra = helper(tokens)
    print("it did a thing", parse_result)
    return parse_result


 def helper(tokens):
        nonlocal i
        parsed = []
        # for i in range(len(tokens)):
        print ("len",len(tokens))
        while i < len(tokens):
            print ("idex", i, tokens[i])
            i += 1
            if tokens[i] == "(":
                # print(tokens[i+1],"open")
                # toadd, i = helper(tokens, i+1)
                # parsed.append(toadd)
                # parsed.append(helper(tokens, i+1))
                # parsed.append(helper(tokens[i+1:]))
                parsed.append(helper(tokens))
            if tokens[i] == ")":
                # print (parsed, i+1)
                return (parsed)
            if type(tokens[i]) == int:
                parsed.append(int(tokens[i]))
            else:
                parsed.append(tokens[i])
        if len(parsed) == 1:
        	return parsed[0]
        return parsed
            

    if not parentheses_match(tokens):
        raise SyntaxError
    # parse_result, extra = helper(tokens)
    return helper(tokens)