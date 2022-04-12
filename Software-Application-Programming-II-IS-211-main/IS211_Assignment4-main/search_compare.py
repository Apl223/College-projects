import random
import time

def get_me_random_list(n):

    a_list = list(range(len(n)))
    random.shuffle(a_list)
    return a_list
    
def sequential_search(a_list,item):
        time_start = time.time()
        pos = 0
        found = False
        
        while pos < len(a_list) and not found:
            if a_list[pos] == item:
                found = True
            else:
                pos = pos + 1
        time_end = time.time()
        return (found, time_end - time_start)
        

def ordered_sequential_search(a_list, item):
        time_start = time.time()
        pos = 0
        found = False
        stop = False

        while pos < len(a_list) and not found and not stop:
            if a_list[pos] == item:
                found = True
            else:
                if a_list[pos] > item:
                    stop = True
                else: 
                    pos = pos + 1
        time_end = time.time()
        return (found, time_end - time_start)


def binary_search_iterative(a_list, item):


        time_start = time.time()
        first = 0
        last = len(a_list) - 1
        found = False
        
        while first <= last and not found:
            midpoint = (first + last) // 2
            if a_list[midpoint] == item:
                found = True
            else:
                if item < a_list[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        time_end = time.time()
        return (found, time_end - time_start)
        
        
        
def binary_search_recursive(a_list, item):
        time_start = time.time()

        if len(a_list) == 0:
            time_end = time.time()
            return (False, time_end - time_start)
        else:
            midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            time_end = time.time()
            return (True, time_end - time_start)
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

if __name__ == "__main__":

    input_list_500 = []
    input_list_1k = []
    input_list_5k = []

    sq500 = []
    sq1k = []
    sq5k = []

    osq500 = []
    osq1k = []
    osq5k = []

    bsi500 = []
    bsi1k = []
    bsi5k = []

    bsr500 = []
    bsr1k = []
    bsr5k = []

    #This is where the basis for the lists are created
    for q in range(100):
        for e in range(500):
            input_list_500.append(e)
        for y in range(1000):
            input_list_1k.append(y)
        for u in range (5000):
            input_list_5k.append(u)
        #Randomize based off length
        a = get_me_random_list(input_list_500)
        b = get_me_random_list(input_list_1k)
        c = get_me_random_list(input_list_5k)

#Append the time spent per match attempt
sq500.append(sequential_search(a,99999999)[1])
sq1k.append(sequential_search(b,99999999)[1])
sq5k.append(sequential_search(c,99999999)[1])
        
input_list_500.sort()
input_list_1k.sort()
input_list_5k.sort()
        
osq500.append(ordered_sequential_search(a,99999999)[1])
osq1k.append(ordered_sequential_search(b,99999999)[1])
osq5k.append(ordered_sequential_search(c,99999999)[1])
        
bsi500.append(binary_search_iterative(a,99999999)[1])
bsi1k.append(binary_search_iterative(b,99999999)[1])
bsi5k.append(binary_search_iterative(c,99999999)[1])
        
bsr500.append(binary_search_recursive(a,99999999)[1])
bsr1k.append(binary_search_recursive(b,99999999)[1])
bsr5k.append(binary_search_recursive(c,99999999)[1])   

#Obtain average from summing up the elements divided by the length of the arrays
sq_average_500 = sum(sq500) / float(len(sq500))
sq_average_1k = sum(sq1k) / float(len(sq1k))
sq_average_5k = sum(sq5k) / float(len(sq5k))

osq_average_500 = sum(osq500) / float(len(osq500))
osq_average_1k = sum(osq1k) / float(len(osq1k))
osq_average_5k = sum(osq5k) / float(len(osq5k))

bsi_average_500 = sum(bsi500) / float(len(bsi500))
bsi_average_1k = sum(bsi1k) / float(len(bsi1k))
bsi_average_5k = sum(bsi5k) / float(len(bsi5k))

bsr_average_500 = sum(bsr500) / float(len(bsr500))
bsr_average_1k = sum(bsr1k) / float(len(bsr1k))
bsr_average_5k = sum(bsr5k) / float(len(bsr5k))

print("Sequential Search took %10.7f seconds, on average, to run over a list of length 500" % sq_average_500)
print ("Sequential Search took %10.7f seconds, on average, to run over a list of length 1000" % sq_average_1k)
print ("Sequential Search took %10.7f seconds, on average, to run over a list of length 5000" % sq_average_5k)
print ("Ordered Sequential Search took %10.7f seconds, on average, to run over a list of length 500" % osq_average_500)
print ("Ordered Sequential Search took %10.7f seconds, on average, to run over a list of length 1000" % osq_average_1k)
print ("Ordered Sequential Search took %10.7f seconds, on average, to run over a list of length 5000" % osq_average_5k)
print ("Binary Search Iterative took %10.7f seconds, on average, to run over a list of length 500" % bsi_average_500)
print ("Binary Search Iterative took %10.7f seconds, on average, to run over a list of length 1000" % bsi_average_1k)
print ("Binary Search Iterative took %10.7f seconds, on average, to run over a list of length 5000" % bsi_average_5k)
print ("Binary Search Recursive took %10.7f seconds, on average, to run over a list of length 500" % bsr_average_500)
print ("Binary Search Recursive took %10.7f seconds, on average, to run over a list of length 1000" % bsr_average_1k)
print ("Binary Search Recursive took %10.7f seconds, on average, to run over a list of length 5000" % bsr_average_5k)