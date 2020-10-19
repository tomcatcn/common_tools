"""

lstack.py 栈的链式结构
重点代码

思路:
1. 源于节点存储数据,建立节点关联
2. 封装方法 入栈 出栈 栈空 栈顶元素
3. 链表的开头作为栈顶(不需要每次遍历)

"""

class StackError(Exception):
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

    # def __str__(self):
    #     return "数据{}:next({})".format(self.val,self.next)

class LStack:
    def __init__(self):
        #标记栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        #不需要判断是不是None
        # node = Node(val)
        # node.next = self.top
        # self.top = node
        # 简写
        self._top = Node(val, self._top)

    def pop(self):
        if self._top is None:
            raise StackError('栈为空')
        value = self._top.val
        self._top = self._top.next
        return value

    def show(self):
        while self._top.next is not None:
            print(self._top.val)
            self._top = self._top.next
    @property
    def top(self):
        if self._top is None:
            raise StackError('栈为空')
        return self._top.val



if __name__ == '__main__':
    stack = LStack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(1)
    # stack.show()
    print(stack.pop())
    print(stack.top)



