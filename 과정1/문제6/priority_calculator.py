import calculator

def main():
    expr=list(input("수식 입력(띄어쓰기):").split())
    
    def precedence(op):
        if op=="+" or op=="-":  return 1
        if op=="*" or op=="/":  return 2
        else: return -1
    
    s=[]
    output=[]
    
    for term in expr:
        if term in "+-/*":
            while s and precedence(s[-1]) >= precedence(term):
                output.append(s.pop())
            s.append(term)
        else:
            output.append(term)
    
    while s:
        output.append(s.pop())
    
    stack=[]
    
    for token in output:
        if token not in "+-*/":
            stack.append(float(token))
        else:
            b=stack.pop()
            a=stack.pop()
            
            if token=="+":
                result=calculator.add(a,b)
            elif token=="-":
                result=calculator.subtract(a,b)
            elif token=="*":
                result=calculator.multiply(a,b)
            elif token=="/":
                result=calculator.divide(a,b)
            else:
                raise ValueError
            stack.append(result)
    print(stack[0])
if __name__ =="__main__":
    main()