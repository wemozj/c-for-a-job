def josephus_A(n, k, m):
    people = list(range(1, n+1))
    i = k - 1
    for num in range(n): # 遍历包含n个人的表
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1 # 计数，报到第几个数
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i + 1) % n # 维护people数组的下标
        if num < n-1:
             print(", ", end="")
        else:
            print("")
    return

def josephus_L(n, k, m):
    people = list(range(1, n+1))
    
    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i),
              end=(', ' if num > 1 else '\n'))
    return 

class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next
    
    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(),
                  end=('\n' if self.is_empty() else ", "))

# josephus_A(10, 2, 7)
josephus_L(10, 2, 7)

