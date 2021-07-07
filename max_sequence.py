
#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence(arr):
    max_sum = 0
    for x in range(len(arr)):
        for y in range(len(arr)-x):
            if sum(arr[x:len(arr)-y]) > max_sum:
                max_sum = sum(arr[x:len(arr)-y])
        for y in range(x):
            if sum(arr[:y]) > max_sum:
                max_sum = sum(arr[:y])
    return max_sum


if __name__ == '__main__':
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))