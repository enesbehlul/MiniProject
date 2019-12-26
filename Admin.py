from User import User

class Admin(User):
	def __init__(self, userId, password, budget, registered_courses):
		User.__init__(self, userId, password, budget, registered_courses)
