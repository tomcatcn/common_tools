"""
二分查找实现
"""
#从l中找到key的索引
def search(l:list,key:int):
    low,high = 0,len(l) - 1
    while low <= high:
        #中间索引
        mid = (low+high) // 2
        if l[mid] < key:
            low = mid+ 1
        elif l[mid] > key:
            high = mid-1

        else:
            return mid



l = [1,2,3,4,5,6,7,8,9,10,11]
print("Key index:",search(l,))