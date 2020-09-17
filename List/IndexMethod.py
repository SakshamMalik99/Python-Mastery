vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# element 'e' is searched
index = vowels.index('e')

# index is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)


# random list
random = ['a', ('a', 'b'), [3, 4]]

# element ('a', 'b') is searched
index = random.index(('a', 'b'))

# index is printed
print("The index of ('a', 'b'):", index)

# element [3, 4] is searched
index = random.index([3, 4])

# index is printed
print("The index of [3, 4]:", index)
