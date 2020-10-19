from stack import LStack


class QueueError(Exception):
    pass


class Node:
    """
    包含一个简单数据作为数据
    next 构建关系
    """
    def __init__(self,val,next=None):
        self.val = val
        #指向下一个节点
        self.next = next


class LQueue:
    def __init__(self):
        # 标记队头和队尾，让他们指向同一个空节点对象
        self._head = self._rear = Node(None)

    def init(self,iter):
        # 初始化，只需要把队尾标记移动，队头不变即可
        for i in iter:
            node = Node(i)
            self._rear.next = node
            self._rear = node #队尾移动

    # 是否空队列
    def is_emtpy(self):
        # 如果两个标记一样，则为空队列
        return self._head == self._rear

     #出队列一个元素
    def front(self):
        if self.is_emtpy():
            raise QueueError('队列为空')
        # 队头所标记的节点为出队列的数据，并不是真正的断开，断开的是前一位
        self._head = self._head.next # 向右移动一位
        return self._head.val

    #入队一个元素
    def rear(self,val):
        # 队尾标记，直接指向新节点即可
        node = Node(val)
        self._rear.next = node

    def show(self):
        while self._head.next is not None:
            print(self._head.val)


class StackQueue:
    """
    两个链表完成队列功能
    """

    def __init__(self):
        # 入队列链表
        self._inqueue = LStack()
        # 出队列链表
        self._outqueue = LStack()

    # 入队
    def inqueue(self, val):
        while True:
            # 如果出队链表为空，把数据进栈入队链表，
            if self._outqueue.is_empty():
                self._inqueue.push(val)
                break
            # 如果不为空，就把出队链表的数据全部入栈到入队链表
            else:
                value = self._outqueue.pop()
                self._inqueue.push(value)

    # 出队
    def outqueue(self):
        while True:
            # 如果入队链表为空，直接出队数据
            if self._inqueue.is_empty():
                return self._outqueue.pop()
            # 如果两个链表都为空，则队列为空
            elif self._inqueue.is_empty() and self._outqueue:
                raise QueueError('队列为空')
            # 如果入队链表不为空，把全部入队数据压到出队链表
            value = self._inqueue.pop()
            self._outqueue.push(value)

if __name__ == '__main__':
    queue = LQueue()
    queue.init(range(10))
    print(queue.front())
    print(queue.front())
    print(queue.front())
    print(queue.front())
    queue.rear('ni')
    print(queue.is_emtpy())
    for i in range(12):
        queue.front()



