if _name_ == '_main_':
    n = int(input())
    arrr = map(int, input().split())
    arr=list(arrr)
    b=max(arr)
    while max(arr)==b:
        arr.remove(max(arr))
    print(max(arr))
