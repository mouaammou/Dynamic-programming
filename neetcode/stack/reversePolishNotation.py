from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = set("*/+-")
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(int(tokens[i]))
            elif len(stack) >= 2:
                opera = tokens[i]
                elment_2 = stack[-1]
                elment_1 = stack[-2]

                stack.pop()
                stack.pop()
                
                if opera == "+":
                    stack.append(elment_1 + elment_2)
                elif opera == "-":
                    stack.append(elment_1 - elment_2)
                elif opera == "*":
                    stack.append(elment_1 * elment_2)
                else:
                    if elment_2 != 0:
                        stack.append(int(elment_1 / elment_2) )

        return stack[-1]
    

    def evalRPN(self, tokens: List[str]) -> int:
        operations = set("*/+-")
        def dfs():
            token = tokens.pop()
            if token not in operations:
                return int (token)

            right = dfs()
            left = dfs()

            if token == "+":
                return int (left + right)
            elif token == "-":
                return int (left - right)
            elif token == '*':
                return int (left * right)
            elif token == '/':
                return int (left / right)
            
        return dfs()

if __name__ == "__main__":
    # tokens = ["1","2","+","3","*","4","-"]  # Example input
    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    sol = Solution()
    result = sol.evalRPN(tokens)
    print(result)

