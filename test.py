def fun(l):

    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    print(l)

if __name__ == '__main__':
    l = [1, 2, 3, 8, 10, 89, 56, 23, 8]
    fun(l)