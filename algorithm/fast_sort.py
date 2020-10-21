"""
快速排序
思路:
该方法的基本思想是：

1．先从数列中取出一个数作为基准数。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。 (使用递归)

"""

class Sort:

    # 返回调整基准数的位置索引
    @staticmethod
    def adjust_list(l:list,i:int,r:int)->None:
        i = i
        j = r
        # 给定基准
        x = l[i]
        # 方法一直接编写，有点缺陷
        # while i<j:
        #     #从j开始向后找
        #     while True:
        #         if i == j:
        #             list[i] = x
        #             break
        #         # 小于基准的数，填到前面挖出的坑list[i]
        #         if list[j] <= x:
        #             list[i] = list[j]
        #             break
        #         j -= 1
        #     # 从i开始向前找，找到大于基准的数，填到前面挖的坑list[j]
        #     while True:
        #         if i == j:
        #             list[i] = x
        #             break
        #         if list[i] > x:
        #             list[j] = list[i]
        #             break
        #         i += 1
        # #返回调整基准数的位置索引
        while i<j:
            #后面往前找，比x大，j往前走
            while l[j] > x and j > i:
                j -= 1
            l[i] = l[j] #比x小的往前甩
            #前面往后找，比x小，i往前走
            while l[i] <= x and i <j:
                i += 1
            l[j] = l[i] #比x大的，往前甩
        l[i] = x # 最终的插入位置

        return i

    #分治法(关键点递归)
    @staticmethod
    def fast_sort(l,i,r):
        # 给一个基准调整数组
        # def quick(l: list, low: int, high: int) -> None:
        #     if low < high:
        #         key = sub_sort(l, low, high)
        #         quick(l, low, key - 1)
        #         quick(l, key + 1, high)
        # if l<r:
        if i<r:
            key = Sort.adjust_list(l,i,r)
            Sort.fast_sort(l,i,key-1)
            Sort.fast_sort(l,key+1,r)

            # Sort.fast_sort(list,l,key-1)
            # Sort.fast_sort(list, key + 1, r)





if __name__ == '__main__':
    l = [4,2,3,8,7]
    fast_sort = Sort()
    fast_sort.fast_sort(l,0,len(l)-1)
    print(l)
