def recursion(n):
    if n <= 1:
        return 1

    return n*recursion(n-1)


if __name__ == '__main__':
    print(recursion(100))