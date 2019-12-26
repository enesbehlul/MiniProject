from User import User
class Student(User):
	def __init__(self, userId, password, budget, registered_courses):
		User.__init__(self, userId, password, budget, registered_courses)
		for course in registered_courses:
			course.registered_users.append(self)
