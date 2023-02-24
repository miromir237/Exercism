def answer(question):
    # Parse the question
    OPEARTIONS = ['plus', 'minus', 'multiplied', 'divided']
    question = question.replace('?', '')
    question = question.replace('by', '')
    literals = question.split()
    print(literals)

    # Check if question has2 or more operands
    if len(literals) < 3:
        raise ValueError('syntax error')

    # Check if the question is valid
    if literals[0] != 'What' or literals[1] != 'is':
        raise ValueError('unknown operation')

    # Check if the question is a simple number
    if len(literals) == 3:
        try:
            return int(literals[2])
        except ValueError:
            raise ValueError('syntax error')
    
    if len(literals) == 4:
        # Check if operation is supported
        if literals[3] not in OPEARTIONS:
            raise ValueError('unknown operation')
        else:
            raise ValueError('syntax error')
        
    # Check if the question is a simple operation of addition or substraction
    if len(literals) == 5:
        print("simple operation")
        try:
            if literals[3] in OPEARTIONS:
                if literals[3] == 'plus':
                    return int(literals[2]) + int(literals[4])
                elif literals[3] == 'minus':
                    return int(literals[2]) - int(literals[4])
                elif literals[3] == 'multiplied':
                    return int(literals[2]) * int(literals[4])
                elif literals[3] == 'divided':
                    return int(literals[2]) / int(literals[4])
            else:
                raise ValueError('unknown operation')
        except ValueError:
            raise ValueError('syntax error')

    # Check if the question is a multiple operation
    if len(literals) >= 6:
        result = int(literals[2])
        for i in range(3, len(literals), 2):

            # Check if i+1 is less than length of literals
            if i+1 >= len(literals):
                raise ValueError('syntax error')

            # Check if 1st operand is number
            try: 
                x = int(literals[i+1])
            except:
                raise ValueError('syntax error')

            print("Iterator: " + str(i))
            print(literals[i] + " " + literals[i+1])
            # Check if 2nd operand is operation
            if literals[i] not in OPEARTIONS:
                raise ValueError('unknown operation')
            else:
                if literals[i] == 'plus':
                    result += x
                elif literals[i] == 'minus':
                    result -= x
                elif literals[i] == 'multiplied':
                    result *= x
                elif literals[i] == 'divided':
                    result /= x
                else:
                    raise ValueError('syntax error')
        
        return result
        