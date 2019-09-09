class LinkedListUnderflow(ValueError):
    def __init__(self, Error_info):
        super().__init__(self) # 初始化父类
        self.Error_info = Error_info
    
    def __str__(self):
        return self.Error_info

class LNode:
    """
    一个结点对象
    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_ # 避免和next重名
        
class Linked_List:
    """
    单向链表对象
    """
    def __init__(self):
        self._head = None # 定义链表的首结点
    
    def is_empty(self):
        return self._head is None
    
    def prepend(self, elem):
        # 前端插入结点
        self._head = LNode(elem, self._head)
        
    def pop(self):
        # 弹出首结点中的元素
        if self._head is None:
            # 无结点，引发异常
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
    
    def append(self, elem):
        # 后端（末尾）添加结点元素
        if self._head is None:
            self.prepend(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        # 弹出最后一个元素
        """
        pop last elem
        """
        if self._head is None: # 空表
            raise LinkedListUnderflow(" in pop_last")
        p = self._head
        if p.next is None: # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None: # 直到p.next是最后结点
            p = p.next
        e = p.next.elem
        p.next = None
        return e
    
    def find(self, pred):
        """
        找到满足给定条件的表元素
        Args:
            pred ([type]): 条件函数
        """
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
    
    def filter(self, pred):
        """
        定义成一个可迭代的函数
        yield 
        
        Args:
            pred (condition): [description]
        """
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next
    
    def printall(self):
        # # version 1.0
        # p = self._head
        # while p is not None:
        #     print(p.elem, end='')
        #     if p.next is not None:
        #         print(', ', end='')
        #     p = p.next
        # print('') # 输出一个换行符
        
        # # version 2.0 将遍历操作定义为对象的一个迭代器
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

class LList1(Linked_List):
    def __init__(self):
        Linked_List.__init__(self)
        self._rear = None # 尾结点
        
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
    
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
            



if __name__ == "__main__":
    mlist1 = Linked_List()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    # mlist1.printall()
    for x in mlist1.printall():
        print(x)