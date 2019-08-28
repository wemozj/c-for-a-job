class SeqList(object):
    def __init__(self, max=0):
        self.max = max
        self.num = 0 # 当前顺序表中元素的数量
        self.data = [None] * self.max # 初始化顺序表数组
    
    def is_empty(self):
        return self.num is 0
    
    def is_full(self):
        return self.num is self.max
    
    def __getitem__(self, i):
        """
        取出位置i的元素
        
        Args:
            i ([type]): [description]
        """
        if not isinstance(i, int):
            raise TypeError
        if 0<= i < self.num:
            return self.data[i]
        else:
            raise IndexError
    
    def __setitem__(self, key, value):
        """
        修改key位置的值为value
        
        Args:
            key ([type]): [description]
            value ([type]): [description]
        """
        if not isinstance(key, int):
            raise TypeError
        if 0<= key < self.num:
            self.data[key] = value
        else:
            raise IndexError
    
    def getLoc(self, value):
        """
        返回值为value的索引；若找不到，返回-1
        
        Args:
            value ([type]): [description]
        """
        for i in range(self.num):
            if self.data[i] == value:
                return i
        return -1
    
    def Count(self):
        """
        统计线性表中元素的个数
        """
        return self.num
    
    def appendLast(self, value):
        """
        表末尾插入操作
        
        Args:
            value ([type]): [description]
        """
        if self.num >= self.max:
            print("The list is full")
            return
        else:
            self.data[self.num] = value
            self.num += 1
    
    def insert(self, i, value):
        """
        表任意位置插入
        
        Args:
            i ([type]): [description]
            value ([type]): [description]
        """
        if not isinstance(i, int):
            raise TypeError
        if i < 0 and i > self.num:
            raise IndexError
        for j in range(self.num,i,-1):
            self.date[j] = self.date[j-1]
        self.date[i] = value
        self.num += 1
    
    def remove(self, i):
        """
        移除索引i的元素
        
        Args:
            i ([type]): [description]
        """
        if not isinstance(i,int):
            raise TypeError
        if i < 0 and i >=self.num:
            raise IndexError
        for j in range(i,self.num):
            self.date[j] = self.date[j+1]
        self.num -= 1
    
    def printList(self):
        """
        打印线性表中所有元素
        """
        for i in range(0,self.num):
            print self.date[i]
        pass
    
    def destroy(self):
        """
        销毁线性表
        """
        self.__init__()
        pass