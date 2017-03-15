import sys

def permutations(array):
    if len(array) == 1:
        return [array]
    arr = []
    for i in range(len(array)):
        [arr.append([array[i]] + x) for x in permutations(array[0:i] + array[i+1:])]
        '''
        for elem in permutations(array[0:i] + array[i+1:]):
            arr.append([array[i]] + elem)
        '''
    return arr


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Usage: {0} comma_separated_list_of_elements'.format(sys.argv[0]))
    print permutations(sys.argv[1].split(','))
