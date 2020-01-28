### Exploring the Built-in Functions and Types

## Using abs(), round(), min(), max(), divmod(), len(), sum()
x = -2.5678
nums = [1,2,3,4,5]
print('x = -2.5678')
print('nums = [1,2,3,4,5]')
print(f'abs(x): {abs(x)}')
print(f'round(x): {round(x)}')
print(f'min(nums): {min(nums)}')
print(f'max(nums): {max(nums)}')
print(f'sum(nums): {sum(nums)}')
print(f'divmod(7,3): {divmod(7,3)}') # Returns tuple (quotient, remainder)
print(f'len(nums): {len(nums)}')

## Using range, list
print(f'range(0,100,20): {range(0,100,20)}')
print(f'list(range(0,100,20)): {list(range(0,100,20))}')

## Using iter()
iter_nums = iter(nums)
print(f'iter_nums = iter(nums)')
print(f'next(iter_nums): {next(iter_nums)}')
print(f'next(iter_nums): {next(iter_nums)}')
print(f'next(iter_nums): {next(iter_nums)}')
print(f'next(iter_nums): {next(iter_nums)}')
print(f'next(iter_nums): {next(iter_nums)}')
try:
	print(f'next(iter_nums): {next(iter_nums)}')
except Exception as e:
	print(e)


## Using all(), any()
bools1 = [True, True, True]
bools2 = [True, False, True]
bools3 = [False, False, False]
print('{all(bools1)}, {all(bools2)}, {all(bools3)}')
print(f'{all(bools1)}, {all(bools2)}, {all(bools3)}')
print('{any(bools1)}, {any(bools2)}, {any(bools3)}')
print(f'{any(bools1)}, {any(bools2)}, {any(bools3)}')

# bin() converts an integer to a binary string prefixed with "0b"

## Using bool()
true_list = [True, 1, 'anystring']
false_list = [False, 0, (), [], {}, ""]
for x in true_list:
	print(f'x is {x}: bool(x) is {bool(x)}')
for x in false_list:
	print(f'x is {x}: bool(x) is {bool(x)}')

## Using dir()
print(f'dir(): {dir()}')

## Using enumerate()
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(f'seasons = {seasons}')
print(f'list(enumerate(seasons)): {list(enumerate(seasons))}')

## Using filter()
# function that filters vowels 
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False 
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
# using filter function 
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
    print(s) 

## Using globals(), locals()
print(f'globals(): {globals()}')
print(f'locals(): {locals()}')

## Using map()
def times2(n): 
    return n + n 
 # We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(times2, numbers) 
print(list(result)) 

## Using sorted
let = ['a','A','b','B','abacus','Abacus']
print(f'sorted(let, key=str.lower): {sorted(let, key=str.lower)}')
print(f'sorted(let, key=str.lower, reverse=True): {sorted(let, key=str.lower, reverse=True)}')

## Using staticmethod(), classmethod()
class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	@staticmethod
	def say_hello():
		print(f'Hello!!!')

	@classmethod
	def from_dict(Person, dict_input):
		# A class method receives the class as the implicit first argument
		# This function creates a Person from a dictionary
		return Person(dict_input['name'], dict_input['age'])


## Using zip
x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)
print(f'x = {x}, y = {y}, zipped = {zip(x,y)}')
print(f'list(zipped): {list(zipped)}')
print(f'Unzipping zipped objects. x2,y2 = zip(*zip(x,y))')
x2,y2 = zip(*zip(x,y))
print(f'x == list(x2) and y == list(y2): {x == list(x2) and y == list(y2)}')
