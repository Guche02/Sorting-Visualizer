import random

# generating a list to sort
def generate_starting_list(n, min_val, max_value):
    lst = []

    for _ in range(n):
        val  = random.randint(min_val, max_value)
        lst.append(val)

    return lst

def bubble_sort(draw_info, draw_list, ascending = True):
    lst = draw_info.lst

    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (lst[j] > lst[j+1] and ascending) or (lst[j] < lst[j+1] and not ascending):  # for both ascending and descending cases
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True   # it allows to iterate upto this point 1 single time, using yield, the bubble sort function becomes a generator
    return lst

# next() # first time, next is called, only first 2 elements are swapped, second time next is called, the next two elements are swapped..and so on..it is used in main code
   
def insertion_sort(draw_info, draw_list, ascending = True):
    lst = draw_info.lst

    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and ((key < lst[j] and ascending) or (key > lst[j] and not ascending)):
            lst[j+1] = lst[j]
            j -= 1
            lst[j+1] = key
            draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
            yield True   # it allows to iterate upto this point 1 single time, using yield, the insertion sort function becomes a generator
    return lst

def selection_sort(draw_info, draw_list, ascending = True):
    lst = draw_info.lst

    n = len(lst)
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if ((lst[index] > lst[j]) and ascending):
              index = j
        lst[i], lst[index] = lst[index], lst[i]
        draw_list(draw_info, {index: draw_info.GREEN, i: draw_info.RED}, True)
        yield True   # it allows to iterate upto this point 1 single time, using yield, the insertion sort function becomes a generator
    return lst
