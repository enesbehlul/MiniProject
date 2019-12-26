class User:
	def __init__(self, userId, password, budget, registered_courses):
		self.userId = userId
		self.password = password
		self.budget = budget
		self.registered_courses = registered_courses

	def can_take_course(self, course):
		if course.course_price() <= self.budget:
			return True
		return False

	def course_exist(self, course):
		if course in self.registered_courses:
			return True
		return False
	
	def add_course(self,course):
		self.registered_courses.append(course)
		
	def delete_course(self, course):
		self.registered_courses.remove(course)
		
	def add_money(self, amount):
		self.budget = self.budget + amount
	
	def take_money(self, amount):
		self.budget = self.budget - amount
	

