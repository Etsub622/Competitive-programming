
def insertionSort1(n, arr):
    # Write your code here
    for i in range(1,n):
        current = arr[i]
           
        while (i > 0 and arr[i- 1] > current):
            arr[i] = arr[i- 1]
            print(*arr)
            i-= 1
            arr[i] = current
    print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
