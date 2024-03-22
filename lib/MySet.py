class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

# Bonus methods
# MySet.clear(): Removes all the items from the set, and returns the updated set.
# Print the set in a readable format using the __str__ method.

# Uncomment the following lines if you want to test the bonus methods

# set = MySet([1,2,3])
# print(set)
# # => MySet: {1, 2, 3}
#
# set.clear()
# print(set)
# # => MySet: {}
