def fibonacci(n: int):
    if n == 0:
        return 0

    if n == 1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_list(input: int):
    list = []
    count = 0
    while True:
        list.append(fibonacci(count))
        if list[count] > input:
            break
        count += 1

    return list



print(fibonacci_list(4))