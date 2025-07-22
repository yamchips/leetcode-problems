# class MinStack:
#     def __init__(self) -> None:
#         self.stack = []
#         self.min = []

#     def push(self, val: int):
#         self.stack.append(val)
#         if not self.min:
#             self.min.append((val, 1))
#         else:
#             if val < self.min[-1][0]:
#                 self.min.append((val, 1))
#             elif val == self.min[-1]:
#                 self.min[-1] = (val, self.min[-1][1] + 1)

#     def pop(self):
#         deleted = self.stack.pop()
#         if deleted == self.min[-1][0]:
#             self.min[-1] = (deleted, self.min[-1][1] - 1)
#             if self.min[-1][1] == 0:
#                 self.min.pop()
    
#     def top(self):
#         return self.stack[-1]
    
#     def getMin(self):
#         return self.min[-1][0]
class MinStack:
    def __init__(self) -> None:
        self.stack = []


    def push(self, val: int):
        if not self.stack:
            self.stack.append((val, val))
        else:
            currMin = self.stack[-1][1]
            if currMin > val:
                currMin = val
            self.stack.append((val, currMin))
 

    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]