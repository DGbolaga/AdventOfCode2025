
def  get_rolls(arr_2d):
    # arr_2d contains string of paper rolls.
    ans = 0
    n = len(arr_2d)
    m = len(arr_2d[0])
    
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr_2d[i][j] == '@':
                adj_roll_paper = 0
                if arr_2d[i-1][j-1] == "@": #top_left
                    adj_roll_paper += 1
                if arr_2d[i-1][j] == "@": #up
                    adj_roll_paper += 1
                if arr_2d[i-1][j+1] == "@": #top right
                    adj_roll_paper += 1
                if arr_2d[i][j+1] == '@': # right 
                    adj_roll_paper += 1
                if arr_2d[i+1][j+1] == '@': #bottom right
                    adj_roll_paper += 1
                if arr_2d[i+1][j] == '@': #down
                    adj_roll_paper += 1
                if arr_2d[i+1][j-1] == '@': #bottm left
                    adj_roll_paper += 1
                if arr_2d[i][j-1] == '@': #left
                    adj_roll_paper += 1

                if adj_roll_paper < 4:
                    ans += 1
    return ans
    



if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.readlines()
        size = len(input[0])
        top_string = "." * (size+1)
        arr_2d = [top_string]
        for ch in input:
            new_string = '.' + ch.rsplit().pop() + '.'
            arr_2d.append(new_string)
        arr_2d.append(top_string)


    print(get_rolls(arr_2d))
