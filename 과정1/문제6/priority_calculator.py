import calculator

def main():
    expr=list(input("수식 입력(띄어쓰기):").split())
    
    # 연산 우선순위 부여
    def precedence(op):
        if op=="+" or op=="-":  return 1
        if op=="*" or op=="/":  return 2
        else: return -1
    
    s=[]
    output=[]
    
    try:
        # 후위 표기식 변형
        # 입력이 없을 경우 오류
        if not expr:
            raise ValueError
        
        for term in expr:
            if term in "+-/*":
                while s and precedence(s[-1]) >= precedence(term):
                    output.append(s.pop())
                s.append(term)
            # 숫자가 아닐경우 오류
            else:
                try:
                    float(term)
                except:
                    raise ValueError
                output.append(term)
    
        while s:
            output.append(s.pop())
        if output[-1] not in "+-/*":
            raise ValueError
        # 계산기 계산
        stack=[]
    
        for token in output:
            if token not in "+-*/":
                stack.append(float(token))
            else:
                # 사칙연산 연산이 잘못된 경우 오류 (1 +)
                if len(stack)<2:
                    raise ValueError
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
        # 숫자가 하나만 들어온 경우
        if len(stack)==1 and len(output)==1:
            raise ValueError
        # 3 3 + 3과 같은 경우 오류
        if len(stack) !=1:
            raise ValueError
        print(stack[0])
    
    except ValueError:
        print("Invalid Input")
    
if __name__ =="__main__":
    main()