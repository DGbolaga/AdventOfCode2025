



if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        input = file.readlines()
        val = [x.split() for x in input]
        ans = 0
        n = len(val[-1])
        m = len(val)
        result = 0
        for x in range(n-1, -1, -1): 
            sign = val[-1].pop()
            ans = 1 if sign == '*' else 0
            for y in range(m-2, -1, -1):
                if sign == '+':
                    ans += int(val[y].pop())
                elif sign == '-':
                    ans -= int(val[y].pop())
                elif sign == '*':
                    ans *= int(val[y].pop())

            result += ans
        print(result)
        print(val)

       
