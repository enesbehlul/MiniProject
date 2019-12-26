class Course:
	def __init__(self, name, credits, registered_users, price):
		self.name = name
		self.credits = credits
		self.registered_users = registered_users
		self._price = price

	def display(self):
		print(self.name)
		print(self.credits)
		print(self.registered_users)

	def delete_course(self):
		pass

	def course_price(self):
		return self._price

class User:
	def __init__(self, userId, password, budget, registered_courses):
		self.userId = userId
		self.password = password
		self.budget = budget
		self.registered_courses = registered_courses

	def can_take_course(self, course):
		if course.course_price <= self.budget:
			return True
		return False

	def course_exist(self, course):
		if course in this.registered_courses:
			return True
		return False


class MenuItem:
	def __init_(self, text, number):
		self.text = text
		self.number = number
	
	def display(self):
		return str(self.number) + ". " + self.text
	
class Menu:
	def __init__(self, items, header):
		self.items = items
		self.header = header
		
	def display(self, display_header):
		if display_header:
			print(self.header)
			
		for i in self.items:
			print (i.display())
		return int(input("Please select an operation: "))
		
	def add_menu_item(self, text, number):
		item = MenuItem(text, number)
		self.items.append(item)

class CourseManagementSystem:
	def __init__(self, courses, users, admin_menu, student_menu, admin_money_sub_menu, current_user):
		pass
	
	def login(self):
		userId = input("Please enter your Id: ")
		password = input("Please enter your password: ")
		if userId in self.users:
			if self.users[userId].password == password:
				self.current_user = self.users[userId]
				print("Login success.")
		
