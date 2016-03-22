#Lab 4 Grades Exercise 

def count_grade(grades):
	'''
	takes a list of grades
	as an argument and returns a dict of grade counts.
	''' 

	counts = {} 
	for grade in grades: 
		if not grade in counts:
			counts[grade] = 1
		else:
			counts[grade] += 1 

	return counts 



def process_grades(filename): 
	
	return count_grade(turn_to_list(filename))

def turn_to_list(filename): 
	f = open(filename, 'r')
	lines = f.readlines() 
	grade_listings = lines[0]

	just_grade = grade_listings.strip("\n")
	grades = just_grade.split(" ")

	return grades


def list_grades():
	f = open("grades_names.txt", 'r')
	lines = f.readlines() 
	
	grades_dict = {} 

	for line in lines: 
		entry = line.strip("\n")
		entry = entry.split(" ")
		grade = entry[0]
		name = entry[1]

		if not grade in grades_dict:
			grades_dict[grade] = [name]
		else:
			grades_dict[grade].append(name)


	return grades_dict