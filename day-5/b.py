

if __name__ == '__main__':
    with open("input.txt", 'r') as file:
        input = file.readlines()

    ranges = [] #list of tuples
    start_idx = 0
    for i, line in enumerate(input):
        if start_idx == 0:
            y = line.rsplit("\n")
            x = y[0]
            if x:
                a, b = x.split('-')
                ranges.append((int(a), int(b)))
            else:
                break
                start_idx = i

    ranges.sort()
    #compress overlapping results.
    stack = []
    for item in ranges:
        start, end = item
        if not stack:
            stack.append(item)
        else:
            prev_start, prev_end = stack[-1]
            if prev_end >= start:
                stack.pop()
                stack.append((min(start, prev_start), max(prev_end, end)))
            else:
                stack.append(item)

    #print(ranges)
    #print(stack)
    print(sum(b - a + 1 for a, b in stack))
