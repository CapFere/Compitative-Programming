from math import trunc
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(left_operand + right_operand)
            elif token == "-":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(left_operand - right_operand)
            elif token == "*":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(left_operand * right_operand)
            elif token == "/":
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(trunc(left_operand / right_operand))
            else:
                stack.append(int(token))
        return stack.pop()
def main():
    test = Solution()
    print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
main()