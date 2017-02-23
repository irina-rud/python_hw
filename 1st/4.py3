p = int(input())

for k in range(p):
    flag = True
    s = input()
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(1)
        elif s[i] == ")"  :
            if (len(stack) > 0) and (stack[-1] == 1):
                stack.pop()
            else:
                flag = False
                break
        elif s[i] == "{":
            stack.append(2)
        
        elif s[i] == "}" :
            if (len(stack) > 0) and (stack[-1] == 2):
                stack.pop()
            else:
                flag = False
                break
        elif s[i] == "[":
            stack.append(3)
            
        elif s[i] == "]":
            if((len(stack) > 0) and(stack[-1] == 3)):
                stack.pop()
            else:          
                flag = False
                break
    if (len(stack) == 0) and (flag):
        print("yes")
    else:
        print("no")