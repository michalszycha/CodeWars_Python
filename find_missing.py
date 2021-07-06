
#https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python

def find_progression(sequence):
    check = {}
    for x in range(1, len(sequence)):
        maybeProgression = sequence[x] - sequence[x-1]
        if maybeProgression in list(check.keys()):
            return maybeProgression
        else:
            check[maybeProgression] = 1

def find_missing(sequence):
    progression = find_progression(sequence)
    for x in range(len(sequence)-1):
        if sequence[x+1] - sequence[x] != progression:
            return sequence[x]+progression


if __name__ == '__main__':
    print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
    print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))