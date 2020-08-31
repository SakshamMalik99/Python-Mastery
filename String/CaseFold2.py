firstString = "der Fluß"
secondString = "der Flusss"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
