import sys

def check(a):
    n = len(a)
    
    # only factors of n can produce a pattern (excluding n)
    for length in range(1, n//2 + 1):
        if n % length == 0:
            unqiue = a[:length]
            pattern = unqiue * (n//length)
            if pattern == a:
                return True
    return False
    

def count_id_sum_at_least_2(id_list):
    ans = 0
    n = len(id_list)
    for i in range(0, n, 2):
        x, y = int(id_list[i]), int(id_list[i+1])
        for num in range(x, y+1):
            value = str(num)
            if check(value):
                ans += num
    return ans


if __name__ == "__main__":
    with open("a.txt", 'r') as file:
        input = file.readline().strip()
    id_list = []
    x = input.split(',')
    for item in x:
        a, b = item.split('-')
        id_list.append(a)
        id_list.append(b)
    
    print(count_id_sum_at_least_2(id_list))
