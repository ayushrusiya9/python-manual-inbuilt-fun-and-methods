# HIGHER ORDER FUNCTIONS

# map -> a higher order function that applies a function to each item
# of an iterable and returns an iterator with transformed values.
# Example:
# nums = [1, 2, 3]
# map(lambda x: x*x, nums)  ->  [1, 4, 9]


# filter -> a higher order function that selects items from an iterable
# based on a condition (function must return True or False).
# Example:
# nums = [1, 2, 3, 4]
# filter(lambda x: x % 2 == 0, nums)  ->  [2, 4]


# reduce -> a higher order function that reduces an iterable to a single value
# by applying a function cumulatively.
# Example:
# from functools import reduce
# reduce(lambda a, b: a + b, [1, 2, 3, 4])  ->  10


# decorator -> a special type of higher order function that
# takes a function as input and returns a modified function.
# Used to change or extend the behavior of a function
# without changing its original code.
# Example:
# @login_required
# def dashboard():
#     pass


# ITERABLE / ITERATOR / GENERATOR 

# iterable -> an object that can be looped over (list, tuple, string, etc.)
# It does NOT store iteration state.
# Example:
# [1, 2, 3], (1, 2), "abc"


# iterator -> an object that produces values one at a time
# using the next() function and remembers its current state.
# It assigns memory to one element at a time.
# Example:
# it = iter([1, 2, 3])
# next(it) -> 1


# generator -> a special type of iterator created using 'yield'
# It generates values lazily (one at a time).
# Every generator is an iterator, but not every iterator is a generator.
# Example:
# def count(n):
#     for i in range(n):
#         yield i


#  yield vs return

# return -> sends a value and ends the function execution.
# After return, function stops completely.
# Example:
# def add(a, b):
#     return a + b


# yield -> sends a value but pauses the function.
# Function resumes from the same point on next call.
# Used in generators.
# Example:
# def gen():
#     yield 1
#     yield 2
