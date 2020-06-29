#Pysearch is a small package containing 5 popular searching algorithms, 
#which can be implemented quickly and easily.

from math import sqrt

class Invalid_Array_Error(Exception): pass

#AUTHOR: Reinhold Brant
#GITHUB: https://github.com/reinhold-b

def linear_search(array, x, reversed=False):
	"""Linear search: iterate through the whole array until x is found.
	   INPUT: array, x (opt: reversed) - OUTPUT: Index of x in array, if not found
	   the output will be None """

	array = array if not reversed else array[::-1] #reverse the array if reversed is True

	for index, element in enumerate(array):
		if element == x:
			return index
	
	else: return None

def binary_search(array, x):
	"""Binary search: recursive algorithm, which splits the array in half
	then searches for x in every split and proceeds splitting until x is found
	INPUT: array, x (opt: reversed) - OUTPUT: Index of x in array, if not found
	the output will be None"""


	#run when the array is made up of strings
	if all(map(lambda xx: type(xx) == str, array)):
		hashes, n = {}, 0

		# if the array contains only strings, it will be hashed
		for element in array:
			hashes[element] = n
			n += 1

		func_array = list(hashes.values()) # an array of numbers is used to perform comparison > and < and ==

	elif not all(map(lambda xx: type(xx) == str, array)) and any(map(lambda xx: type(xx) == str, array)):
		raise Invalid_Array_Error("The array given can only contain elements of type str or only elements"
								  " of type int.")

	#if the array does not contain strings we check whether it is sorted or not
	else: 
		if all(array[i] < array[i + 1] for i in range(len(array) - 1)):
			func_array = array
		else:
			raise Invalid_Array_Error("The given array has to be sorted.")


	#define the x
	try: x = hashes[x]
	except: x = x

	#binary search algorithm
	def search(array, x, low, high):
		"""Check if x is equal to the middle element of the array, else 'divide and conquer'. """

		if high >= low:
			mid = int((high + low) / 2)	

			#return the index 'mid' if x == array[mid]
			if x == array[mid]:
				return mid

			elif array[mid] > x:
				return search(array, x, low, mid - 1)
			else:
				return search(array, x, mid + 1, high)

		return None

	return search(func_array, x, 0, len(func_array) - 1)


def jump_search(array, x):
	"""Jump Search: Instead of iterating through the whole array Jump Search iterates in steps
	and performs a linear search when the right interval is found"""
	step_size = int(sqrt(len(array)))

	#run when the array is made up of all strings
	if all(map(lambda xx: type(xx) == str, array)):
		hashes, n = {}, 0

		# if the array contains only strings, it will be hashed
		for element in array:
			hashes[element] = n
			n += 1

		func_array = list(hashes.values()) # an array of numbers is used to perform comparison > and < and ==

	elif not all(map(lambda xx: type(xx) == str, array)) and any(map(lambda xx: type(xx) == str, array)):
		raise Invalid_Array_Error("The array given can only elements of type str or only elements"
								  " of type int.")

	#if the array does not contain strings we check whether it is sorted or not
	else: 
		if all(array[i] < array[i + 1] for i in range(len(array) - 1)):
			func_array = array
		else:
			raise Invalid_Array_Error("The given array has to be sorted.")


	#define the x
	try: x = hashes[x]
	except: x = x

	#because the length of the array can be 6, but the step_size 2 ( as int(sqrt(6)) = 2 ), the last element will be ignored
	#therefore this codeblock will check if the this case will happen with the given array and compare
	#x == array[len(array) - 1] 
	if (len(array) - 1) % step_size != 0 and array[len(array) - 1] == x: return (len(array) - 1)

	for i in range(0, len(array), step_size):

		if func_array[i] == x:
			return i
		elif func_array[i] < x:
			pass
		elif func_array[i] > x:
			for index, element in enumerate(func_array[i - step_size: i]):
				if element == x:
					return index
	return None


def interpolation_search(array, x):
	"""Interpolation Search. Calculate the starting position for the algorithm using this formula:
	start_pos = low + ((x-arr[low])*(high-low) / (arr[high]-arr[low]))
	where low is the element at the lowest index in the array and high is the element at the highest index in the array.
	The rest of the agorithm ist just like binary search."""

	#run when the array is made up of strings
	if all(map(lambda xx: type(xx) == str, array)):
		hashes, n = {}, 0

		# if the array contains only strings, it will be hashed
		for element in array:
			hashes[element] = n
			n += 1

		func_array = list(hashes.values()) # an array of numbers is used to perform comparison > and < and ==

	elif not all(map(lambda xx: type(xx) == str, array)) and any(map(lambda xx: type(xx) == str, array)):
		raise Invalid_Array_Error("The array given can only contain elements of type str or only elements"
								  " of type int.")

	#if the array does not contain strings we check whether it is sorted or not
	else: 
		if all(array[i] < array[i + 1] for i in range(len(array) - 1)):
			func_array = array
		else:
			raise Invalid_Array_Error("The given array has to be sorted.")


	#define the x
	try: x = hashes[x]
	except: x = x

	#interpolation search algorithm
	def interpolation(array, x, low, high):
		"""Check if x is equal to the "start_pos" element of the array, else continue loop and calculate new 
		"start_pos"   . """

		if high >= low:
			start_pos = int(low + ((x-array[low])*(high-low) / (array[high]-array[low])))

			#return the index 'start_pos' if x == array[start_pos]
			if x == array[start_pos]:
				return start_pos

			elif array[mid] > x:
				return search(array, x, low, start_pos - 1)
			else:
				return search(array, x, start_pos + 1, high)

		return None

	return interpolation(func_array, x, 0, len(func_array) - 1)


def bilinear_search(array, x):
	"""Bilinear Search: The algorithm starts with the first and last element of the array and the moves the
	two pointers closer to the middle of the array"""
	start, end = 0, len(array) - 1

	while end >= start:

		if array[start] == x:
			return start
		elif array[end] == x:
			return end
		else:
			start += 1
			end -= 1

	return None
	

if __name__ == "__main__":
	descriptions.info()

