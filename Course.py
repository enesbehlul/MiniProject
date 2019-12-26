class Course:
	def __init__(self, name, credits, price):
		self.name = name
		self.credits = credits
		self.registered_users = []
		self._price = price

	def display(self):
		print(self.name + "/t" + str(self.credits))

	def delete_course(self):
		pass

	def course_price(self):
		return self._price
