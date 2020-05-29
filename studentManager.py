from tabulate import tabulate 
from pprint import pprint
import json

# create class Students
class Student:
	#constructor
	def __init__(self): 
		print('\n Enter the following student data: ')
		self.name = input('\n Enter name of the student: ')  
		self.rollno =  int(input('\n Enter roll number of the student: '))
		self.math = int(input('\n Enter the marks scored by the student in Mathematics: '))
		self.science = int(input('\n Enter the marks scored by the student in Science: '))
		self.socialscience = int(input('\n Enter the marks scored by the student in Social Science: '))
		self.english = int(input('\n Enter the marks scored by the student in English: '))
		self.language = int(input('\n Enter the marks scored by the student in Language: '))
		self.total = self.math + self.science + self.socialscience + self.english + self.language 
		self.percentage = self.total/500 * 100
	
	

						
				

							






				





				
		



	









			 
	