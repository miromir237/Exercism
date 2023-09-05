def is_paired(input_string):
    stack = []
    for char in input_string:
        if char == "(":
            stack.append(char)
        elif char == "[":
            stack.append(char)
        elif char == "{":
            stack.append(char)
        
        if len(stack) > 0:
            if char == ")":
                if stack.pop() != "(":
                    return False
            elif char == "]":
                if stack.pop() != "[":
                    return False
            elif char == "}":
                if stack.pop() != "{":
                    return False            
        else:
            if char == ")":
                return False
            elif char == "]":
                return False
            elif char == "}":
                return False
    
    return len(stack) == 0

