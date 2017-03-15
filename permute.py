import sys

def permutations(array):
    if len(array) == 1:
        return [array]
    arr = []
    for i in range(len(array)):
        for elem in permutations(array[0:i] + array[i+1:]):
            arr.append([array[i]] + elem)
    return arr


if __name__ == "__main__":
    print permutations(sys.argv[1].split(','))
