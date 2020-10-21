"""
二叉树类
提供操作二叉树方法
思路分析:
1. 使用链式存储, Node表达一个节点(值,左链接,右链接)
2. 分析遍历过程
"""

#二叉树节点
from data_struct.queue import LQueue


class Node:
    def __init__(self,val,left=None,right=None):
        self._val = val
        self._left = left
        self._right = right


class Bitree:
    #传入树根
    def __init__(self,root):
        self._root = root

    #先序遍历
    def proOder(self,node):
        if node is None:
            return
        print(node._val,end='')
        self.proOder(node._left)
        self.proOder(node._right)
    # 中序遍历
    def mOder(self,node):
        if node is None:
            return
        self.mOder(node._left)
        print(node._val,end='')
        self.mOder(node._right)

    # 后序遍历
    def endOrder(self,node):
        if node is None:
            return
        self.endOrder(node._left)
        self.endOrder(node._right)
        print(node._val, end='')

    # 层次遍历
    def order(self,node):
        #建立一个队列
        queue = LQueue()
        queue.rear(node)
        #队列不为空，一直循环
        while not queue.is_emtpy():
            #拿出一个父点
            qnode = queue.front()
            print(qnode._val)
            #放入两个子节点
            if node._left:
                queue.rear(node._left)
            if node._right:
                queue.rear(node._right)


if __name__ == '__main__':
    # B F G D H I E C A
    # 构建起一个二叉树
    b = Node('B')
    f = Node('F')
    g = Node("G")
    d = Node('D', f, g)
    h = Node('H')
    i = Node('I')
    e = Node('E', h, i)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 树根

    bt = Bitree(a)
    bt.order(bt._root)