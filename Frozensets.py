#Frozen sets 
"""frozenset is an immutable version of a set.
Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset."""
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
# copying a frozenset
c = x.copy()
print(c)
print(type(c))
# difference() method
a = frozenset({"apple", "banana", "cherry"})
b = frozenset({"google", "microsoft", "apple"})
d = a.difference(b)
print(d)