from data_struct.stack import *


class QueueError(Exception):
    pass

class StackQueue:
    """
    两个链表完成队列功能
    """
    def __init__(self):
        #入队列链表
        self._inqueue = LStack()
        #出队列链表
        self._outqueue = LStack()

    #入队
    def inqueue(self,val):
        while True:
            # 如果出队链表为空，把数据进栈入队链表，
            if self._outqueue.is_empty():
                self._inqueue.push(val)
                break
            # 如果不为空，就把出队链表的数据全部入栈到入队链表
            else:
                value = self._outqueue.pop()
                self._inqueue.push(value)

    #出队
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
    queue = StackQueue()
    queue.inqueue(1)
    queue.inqueue(2)
    queue.inqueue(5)
    queue.inqueue(9)
    print(queue.outqueue())
    print(queue.outqueue())
    print(queue.outqueue())
    print(queue.outqueue())
    print(queue.outqueue())




