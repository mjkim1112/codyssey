def add(a,b):
        return a+b

def subtract(a,b):
        return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Error:Division by zero")
    else:
        return a/b

if __name__=="__main__":

    a,b = map(int, input("실수형 숫자 2개 입력").split())
    op=input("연산자 입력")
    
    if op not in ('+', '-', '*', '/'):
        print("Invalid operator")
    if op=='+':
        c=add(a,b)
        print("Result:", c)
    elif op=="-":
        c=subtract(a,b)
        print("Result:", c)
    elif op=="*":
        c=multiply(a,b)
        print("Result:", c)
    elif op=="/":
        c=divide(a,b)
        print("Result:", c)