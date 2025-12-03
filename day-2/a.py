import sys

def check(a):
     i = 0
     mid = len(a) // 2
     if len(a) % 2 != 0:
         return False
     is_valid = True
     while i < mid:
         if a[i] != a[mid+i]:
             is_valid = False
             break
         i+=1
     return is_valid

def count_id_sum(id_list):
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
    
    print(count_id_sum(id_list))
