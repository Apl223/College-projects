import random
import time

def get_me_random_list(n):
    a_list = list(range(len(n)))
    random.shuffle(a_list)
    return a_list
    
def insertion_sort(a_list):
	time_start = time.time()
	for index in range(1, len(a_list)):
		current_value = a_list[index]
		position = index

		while position > 0 and a_list[position - 1] > current_value:
			a_list[position] = a_list[position - 1]
			position -= 1
		a_list[position] = current_value
	time_end = time.time()
	time_difference = time_end - time_start
	return { "the list": a_list, "difference": time_difference}


def shell_sort(a_list):
	time_start = time.time()
	sublist_count = len(a_list) // 2
	while sublist_count > 0:
		for start_position in range(sublist_count):
			gap_insertion_sort(a_list, start_position, sublist_count)

		sublist_count = sublist_count // 2
	time_end = time.time()
	time_difference = time_end - time_start
	return { "the list": a_list, "difference": time_difference}

def gap_insertion_sort(a_list, start, gap):
	for i in range(start + gap, len(a_list), gap):
		current_value = a_list[i]
		position = i
		while position >= gap and a_list[position - gap] > current_value:
			a_list[position] = a_list[position - gap]
			position = position - gap
		a_list[position] = current_value

def python_sort(a_list):
		time_start = time.time()
		a_list.sort()
		time_end = time.time()
		time_difference = time_end - time_start
		return { "the list": a_list, "difference": time_difference}

def populate(top_values):
	sorting_list = []
	for e in range(top_values):
		sorting_list.append(e)
	return sorting_list

if __name__ == "__main__":

    lists_size = [500,1000,5000]

    for x in lists_size:
        sort_types = {
            'Insertion sort':0.0,
            'Shell sort': 0.0,
            'Python sort': 0.0
        }

        i = 0
        while i < 100:
            sorting_list = populate(x)
            randomlist=get_me_random_list(sorting_list)
            sort_types['Insertion sort'] += insertion_sort(randomlist)["difference"]
            sort_types['Shell sort'] += shell_sort(randomlist)["difference"]
            sort_types['Python sort'] += python_sort(randomlist)["difference"]
            i += 1

        for sort in sort_types:
            print("%s  took %10.7f seconds to run, on average %s" % (sort, sort_types[sort] / i, x))