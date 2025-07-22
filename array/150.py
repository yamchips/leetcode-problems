def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in {'+', '-','*', '/'}:
            second = int(stack.pop())
            first = int(stack.pop())
            res = 0
            if token == '+':
                res = first + second
            elif token == '-':
                res = first - second
            elif token == '*':
                res = first * second
            else:
                res = int(first / second)
            stack.append(res)
        else:
            stack.append(token)
    return int(stack.pop())

# // trunctuates towards -inf, int(a/b) trunctuates towards 0

if __name__=='__main__':
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(evalRPN(["4","13","5","/","+"]))
    