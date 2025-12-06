
from collections import deque

def fresh_ingredient_count(ranges, values):
    ans = 0
    fresh_id = []
    unfresh_id = []
    for range in ranges:
        start, end = range # 3, 5 - 10, 14 -16, 20 - 12
        while values and values[0] < start <= end:
            #unfresh_id.append(values.popleft())
            values.popleft()
        while values and start <= values[0] <= end:
            #fresh_id.append(values.popleft())
            values.popleft()
            ans += 1
    return ans              


if __name__ == '__main__':
    with open("input.txt", 'r') as file:
        input = file.readlines()

        ranges = [] #list of tuples
        values = []
        start_idx = 0
        for i, line in enumerate(input):
            if start_idx == 0:
                y = line.rsplit("\n")
                x = y[0]
                if x:
                    a, b = x.split('-')
                    ranges.append((int(a), int(b)))
                else:
                    start_idx = i
            else:
                x = line.rsplit("\n")
                values.append(int(x[0]))
        ranges.sort()
        values.sort()
        #print(ranges)
        #print(values)
        print(fresh_ingredient_count(ranges, deque(values)))

        
        
