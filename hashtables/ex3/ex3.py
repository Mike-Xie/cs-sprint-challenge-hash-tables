from typing import List
from collections import Counter
# assume inputs lists are sets without duplicate
def intersection(arrays: List[int]) -> List[int]:
    num_sets = len(arrays)
    # flatten list 
    flat_list = [item for sublist in arrays for item in sublist]
    counter_dict = Counter(flat_list)
    # newDict = dict(filter(lambda elem: elem[1] == num_sets, counter_dict.items()))
    newDict = {k:v for k,v in counter_dict.items() if v == num_sets}
    return(newDict.keys())
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
