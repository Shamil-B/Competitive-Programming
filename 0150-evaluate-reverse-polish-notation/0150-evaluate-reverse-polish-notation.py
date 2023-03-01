class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        #if element is an operator pop the previous two elements and do the operations on them and
        #then store the value in the stack

        for ele in tokens:
            if ele == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                stack.append(int(operand1)+int(operand2))
                
            elif ele == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                stack.append(int(operand1)-int(operand2))
                
            elif ele == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                stack.append(int(operand1)*int(operand2))
                
            elif ele == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                stack.append(int(operand1)/int(operand2))
                
            else:
                stack.append(ele)
                
        return int(stack[0])
            