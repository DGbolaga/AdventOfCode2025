from collections import deque

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        input = file.readlines()
    n = len(input[0])-1 # excluding '\n'
    m = len(input)

    sign = deque(input[-1].split())
    store = []
    result = deque([])
    for i in range(n):
        number = 0
        for j in range(m-1):
            char = input[j][i]
            if char.isdigit():
                if number == 0:
                    number = int(char)
                else:
                    number = (number * 10) + int(char)
            elif char == ' ':
                continue
           
        if number:
            store.append(number)
        else:
            result.append(store)
            store = []
    result.append(store) # last 

    ans = 0
    while result:
        current_sign = sign.popleft()
        arr = result.popleft()
        if current_sign == "*":
            s = 1
            for i in arr:
                s *= i
            ans += s
        else:
            ans += sum(arr)
    print(ans)
        



