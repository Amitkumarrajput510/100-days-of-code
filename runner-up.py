if __name__ == '__main__':
    n = int(input())
    arrr = map(int, input().split())
    arr=list(arrr)
    b=max(arr)
    while max(arr)==b:
        arr.remove(max(arr))
    print(max(arr))
