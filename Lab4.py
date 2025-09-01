# a. 
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# b. 
def largest_number(lst):
    return max(lst)

# c.
def remove_duplicates(lst):
    return list(set(lst))

# d. 
def frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# e. 
def common_items(lst1, lst2):
    return list(set(lst1) & set(lst2))

# f. 
def list_to_integer(lst):
    return int("".join(map(str, lst)))



if _name_ == "_main_":
    # Example input
    lst = [2, 3, 4, 2, 5, 3, 7]
    lst2 = [3, 7, 8, 9]

    print("\nList 1:", lst)
    print("List 2:", lst2)

    # a
    print("\n(a) Multiplication of all items:", multiply_list(lst))

    # b
    print("(b) Largest Number:", largest_number(lst))

    # c
    print("(c) List after removing duplicates:", remove_duplicates(lst))

    # d
    print("(d) Frequency of elements:", frequency(lst))

    # e
    print("(e) Common items in both lists:", common_items(lst, lst2))

    # f
    int_list = [1, 2, 3, 4, 5]
    print("(f) List:", int_list, "→ Single Integer:", list_to_integer(int_list))
