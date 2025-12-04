import sys

def find_max_2_digit_num(num):
    ans = 0
    arr = [0,0]
    n = len(num)-1
    for i in range(n):
        int_x = int(num[i])
        if i in (0, 1):
            arr[i] = int_x
        else:
            if int_x > arr[0] and i != n-1:
                arr[0] = int_x
                arr[1] = 0
            elif int_x > arr[1]:
                arr[1] = int_x
                
        ans = max(ans, 10*arr[0] + arr[1])
    return ans



if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        x = file.readlines()

    total = 0
    for item in x:
        # item contains newline character.
        total += find_max_2_digit_num(item)
    print(total)
