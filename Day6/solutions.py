# 20. Valid Parenthesis
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = { ")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if stack and c in closeToOpen:
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

# 155.Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

# 150. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        symbol = ["+", "-", "*", "/"]
        res = 0
        stack = []
        for i in tokens:
            if i in symbol: 
                op2 = stack.pop() #3
                op1 = stack.pop() #3
                if i == "+":
                    res = op1 + op2
                    stack.append(res)
                elif i == "-":
                    res = op1 - op2
                    stack.append(res)
                elif i == "*":
                    res = op1 * op2
                    stack.append(res)
                else:
                    res = int(float(op1) / op2)
                    stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]
