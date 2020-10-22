"""
本模块提供建立单链表的类

链表适合插入删除多的操作
"""

#节点类
class Node:
    """
    包含一个简单数据作为数据
    next 构建关系
    """
    def __init__(self,val,next=None):
        self.val = val
        #指向下一个节点
        self.next = next

    def __repr__(self):
        return  '<Node:{},,{}>'.format(self.val,self.next)


#单链表类
class LinkList:
    """
    生成一个对象表示一个单链表对象，
    通过对象调用可以完成对单链表的各种操作
    """
    def __init__(self):
        self.head = Node(None)


    def init(self,iter):
        """
        遍历可迭代对象，并使用next链接起来
        """
        # p 相当于一个中间节点，用完即可销毁
        # p指向self.head,self.head是一个对象,
        #通过p可以操作改变对象属性
        p = self.head
        for i in iter:
            node = Node(i)
            # p.next相当于self.head = next
            # 相当于self.head.next属性指向 node节点
            p.next = node
            # p = node ,p变量解开与self.head的链接
            # 但是self.head对象中的next已经修改了
            # 但是self中已经新添加了next 的指向
            # p 指向node,建立新的指向
            # 第二步 就是重复上面步骤
            p = node

    #遍历打印
    def show(self):
        """
        遍历打印单链表
        p作为一个移动的节点，先获取self.head的next（节点）
        进入循环，打印val
        然后在把p指向下一个节点
        然后再打印

        """
        p = self.head.next # 第一个有效节点
        while p is not None:
            print(p.val,end=',')
            p = p.next #p相当于向后移动
        print('\n')

    #判断是否为空
    def is_empey(self):
        # if self.head.next is None:
        #     return False
        # return True
        return self.head.next is None

    #清空链表
    def clear(self):
        self.head.next = None

    #尾部插入
    def append(self,val):
        # p = self.head.next
        # 要考虑极限情况，比如是个空链表
        p = self.head
        while  p.next is not None:
            p = p.next
        #跳出循环，P已经移动到最后一个节点
        p.next = Node(val)

    #头部插入
    def head_insert(self,val):
        """
        头部插入的新节点，可以直接指向第一个有效节点
        然后，初始节点直接链接新节点就可以了
        这样就不会断开了
        """
        node = Node(val)
        #新节点链接第一个有效节点
        node.next = self.head.next
        #初始节点链接新节点
        self.head.next = node

    #指定位置插入
    def index_insert(self,index,val):
        """
        指定位置插入值
        @param index:指定位置
        @param val: 值
        @return: None
        """
        #找位置,考虑极限情况

        #方法1
        # p = self.head.next
        # while p.next is not None:
        #     if p.val == index:
        #         break
        #     p = p.next
        #建立节点，链接
        #方法二
        p = self.head
        for i in range(index):
            #超出最大范围报错
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    #删除节点（删除第一个val值）
    def delete(self,val):
        """
        删除节点
        @param val:删除的值
        @return: None
        """
        p = self.head
        #确定p停留在待删除点的前一位
        while True:
            if p.next is None:
                raise ValueError('不是值')
            if p.next.val == val :
                break
            p = p.next
        #链接
        p.next = p.next.next

    #获取节点值
    def get_value(self,index):
        if index < 0:
            raise IndexError('超出索引')
        p = self.head
        # range(0)不会执行，所以需要加1
        for i in range(index+1):
            #临界问题
            if p.next is None:
                raise IndexError('超出索引范围')
            p = p.next
        return p.val

    #两个链表链接
    def extend(self,link):
        """
        链表合并
        @param link:需要合并的链表
        @return: None
        """
        #本身链表遍历到尾部,找到尾部节点
        p = self.head
        while p.next is not None:
            p = p.next
        #第二个链表的头部,第一个有效节点
        link_head = link.head.next
        p.next = link_head

    #合并两个链表（变成有序）







if __name__ == '__main__':

    link1 = LinkList()
    # link_list.init(range(5))
    link1.init([1,1,2,3,4,5,6])
    link2 = LinkList()
    link2.init(range(10))
    link1.show()
    link2.show()
    link1.extend(link2)
    link1.show()
    print(dir(link1))


