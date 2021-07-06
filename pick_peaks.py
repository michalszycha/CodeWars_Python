
#https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

def pick_peaks(arr):
    pos = []
    peaks = []
    plateau = 0
    plateauPos = 0
    x = 0
    for i in range(len(arr)-1):
        if i != 0:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                peaks.append(arr[i])
                pos.append(i)
            if plateau == 0:
                if arr[i - 1] < arr[i] == arr[i + 1]:
                    plateau = arr[i]
                    plateauPos = i
                    peaks.append(plateau)
                    pos.append(plateauPos)
                    x = len(peaks)-1
            else:
                if arr[i - 1] == plateau > arr[i + 1]:
                    plateau = 0
                    plateauPos = 0
                if arr[i - 1] == plateau < arr[i + 1]:
                    del peaks[x]
                    del pos[x]
                    plateau = 0
                    plateauPos = 0
                    x = 0
    if plateau != 0:
        del peaks[x]
        del pos[x]

    return {"pos": pos, "peaks": peaks}




if __name__ == '__main__':
    print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]))
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]))
    print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]))
    print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]))
    print(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]))
    print(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]))
    print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))
    print(pick_peaks([]))
    print(pick_peaks([1, 1, 1, 1]))

