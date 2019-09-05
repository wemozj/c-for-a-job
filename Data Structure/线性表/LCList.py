class LinkedListUnderflow(ValueError):
    def __init__(self, Error_info):
        super().__init__(self) # 初始化父类
        self.Error_info = Error_info
    
    def __str__(self):
        return self.Error_info

class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LCList:
    def __init__(self):
        self._rear = None
    
    def is_empty(self):
        return self._rear is None
    
    def prepend(self, elem): # head insert
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
    
    def append(self, elem): # tail insert
        self.prepend(elem)
        self._rear = self._rear.next
    
    def pop(self): # head pop
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem
    
    def printall(self):
        if self.is_empty():
            return 
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next
            
