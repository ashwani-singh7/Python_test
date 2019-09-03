
class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def avrage(self):
		print(sum(self.marks)/len(self.marks)
			
	def friend(self, frnd_name):
		return Student(frnd_name,self.school)
