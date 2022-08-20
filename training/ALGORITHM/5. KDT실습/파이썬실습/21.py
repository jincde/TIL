def reverse(n):
    if n <= 0:
        return
    print(n%10, end = '')
    reverse(n//10)

num = int(input())
reverse(num)