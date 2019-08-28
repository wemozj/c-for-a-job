class SeqList(object):
    def __init__(self, max=0):
        self.max = max
        self.num = 0 # 当前顺序表中元素的数量
        self.data = [None] * self.max # 初始化顺序表数组
    
    def is_empty(self):
        pass
    
    def is_full(self):
        pass
    
    def __getitem__(self, i):
        """
        取出位置i的元素
        
        Args:
            i ([type]): [description]
        """
        pass
    
    def __setitem__(self, key, value):
        """
        修改key位置的值为value
        
        Args:
            key ([type]): [description]
            value ([type]): [description]
        """
        pass
    
    def getLoc(self, value):
        """
        返回值为value的索引；若找不到，返回-1
        
        Args:
            value ([type]): [description]
        """
        pass
    
    def Count(self):
        """
        统计线性表中元素的个数
        """
        pass
    
    def appendLast(self, value):
        """
        表末尾插入操作
        
        Args:
            value ([type]): [description]
        """
        pass
    
    def insert(self, i, value):
        """
        表任意位置插入
        
        Args:
            i ([type]): [description]
            value ([type]): [description]
        """
        pass
    
    def remove(self, i):
        """
        移除索引i的元素
        
        Args:
            i ([type]): [description]
        """
        pass
    
    def printList(self):
        """
        打印线性表中所有元素
        """
        pass
    
    def destroy(self):
        """
        销毁线性表
        """
        pass