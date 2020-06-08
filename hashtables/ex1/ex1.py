from typing import Tuple, List 
Answer = Tuple[int, int]

"""
We add keys using setdefault since we want to keep the oldest key, doing 
regular enumerate will over write with the newest one for duplicates

"""

def get_indices_of_item_weights(weights: List[int], length: int, limit: int) -> Answer:
	# fail on list shorter than 2 
	if length <= 1:
		return None
	# empty dict 
	index_map = {}
	for index_one, n in enumerate(weights):

		m = limit - n
		try:
			index_two = index_map[m]
		except KeyError:
			index_map.setdefault(n, index_one)
		else:
			return tuple(sorted([index_one, index_two], reverse=True))

weights_2 = [4, 4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 3, 8)
print(answer_2)