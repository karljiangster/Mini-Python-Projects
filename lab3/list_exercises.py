#Karl Jiang 
# CS121 Lab 3: Function


# Write functions any, add_lists, and add_one
def any(bool_list):

	for test in bool_list:
		if test:
			return True

	return False
def add_lists(list1, list2):
	
	added_list = []

	for i in range(len(list1)):
		added_list.append(list1[i] + list2[i])

	return added_list


def add_one(list):
	for i in range(len(list)):
		list[i] += 1


def go():
    '''
    Write code to verify that your functions work as expected here
    Try to think of a few good examples to test your work.
    '''

    # replace the pass with test code for your functions
    

if __name__ == "__main__":
    go()

