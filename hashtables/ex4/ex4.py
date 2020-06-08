from typing import List

def has_negatives(a: List[int]) -> List[int]:
    number_map = {}

    for i in a:
        number_map[i] = -i

   # return(number_map)
    negatives = {k:v for k, v in number_map.items() if k < 0}
    return(list(set(negatives.values()).intersection(set(a))))

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
