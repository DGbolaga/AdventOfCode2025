import sys

def count_num_zeros_on_rotations(rotation_sequence):
    count = 0
    dial = 50
    for seq in rotation_sequence:
        direction = seq[0]
        magnitude = int(seq[1:])
        magnitude %= 100
        dial = (dial + magnitude) % 100 if direction == "R" else (dial - magnitude) % 100


        if dial == 0:
            count += 1
    return count
    

if __name__ == "__main__":
    input = sys.stdin.read()
    rotations = list(map(str, input.split()))
    print(count_num_zeros_on_rotations(rotations))

