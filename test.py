class CourseManagementSystem:
	def __init__(self):
		self.courses = self.build_courses()
		self.users = self.build_users()
		self.admin_menu = self.build_menus("admin")
		self.student_menu = self.build_menus("student")
		self.admin_money_sub_menu = self.build_menus("admin_money_sub")
		self.student_money_sub_menu = self.build_menus("student_money_sub")
		print("****Welcome to Course Management System****")
		self.current_user = self.login()
		self.manage_login()
			
	
	def login(self):
		print("\nPlease provide login information!\n")
		user_id = input("Please enter your id: ")
		password = input("Please enter your password: ")
		#check if the user exist
		if user_id in self.users:
			if self.users[user_id].password == password:
				self.current_user = self.users[user_id]
				print("Login success.")
				return self.current_user
			else:
				print("Wrong password")
		else:
			print("No such user")
		return None
		
	def manage_login(self):
		if type(self.current_user) is Student:
			self.show_student_menu()
		elif type(self.current_user) is Admin:
			self.show_admin_menu()
		else:
			 return None
	
	def build_menus(self, menu_type):
		if menu_type == "admin":
			#creating admin menu and its items
			admin_menu_items = []
			admin_menu_items.append(MenuItem("List courses", 1))
			admin_menu_items.append(MenuItem("Create a course", 2))
			admin_menu_items.append(MenuItem("Delete a course", 3))
			admin_menu_items.append(MenuItem("Show students registered to a course", 4))
			admin_menu_items.append(MenuItem("Users Budget Menu", 5))
			admin_menu_items.append(MenuItem("List Users", 6))
			admin_menu_items.append(MenuItem("Create User", 7))
			admin_menu_items.append(MenuItem("Delete User", 8))
			admin_menu_items.append(MenuItem("Exit", 9))
			#creating admin menu and header
			admin_menu = Menu(admin_menu_items, "Welcome Admin! What do you want to do?")
			return admin_menu
		
		elif menu_type == "student":
			student_menu_items = []
			student_menu_items.append(MenuItem("Add courses to my courses", 1))
			student_menu_items.append(MenuItem("Delete a course from my courses", 2))
			student_menu_items.append(MenuItem("Show my courses", 3))
			student_menu_items.append(MenuItem("Budget Menu", 4))
			student_menu_items.append(MenuItem("Exit", 5))
			#creating student menu and header
			student_menu = Menu(student_menu_items, "")
			return student_menu
		
		elif menu_type == "admin_money_sub":
			admin_money_sub_menu_items = []
			admin_money_sub_menu_items.append(MenuItem("Add money to user", 1))
			admin_money_sub_menu_items.append(MenuItem("Subtract money from user", 2))
			admin_money_sub_menu_items.append(MenuItem("Back to admin menu", 3))
			
			admin_money_sub_menu = Menu(admin_money_sub_menu_items, "")
			return admin_money_sub_menu
			
		elif menu_type == "student_money_sub":
			student_money_sub_menu_items = []
			student_money_sub_menu_items.append(MenuItem("Add money", 1))
			student_money_sub_menu_items.append(MenuItem("Go to main menu", 2))
						
			student_money_sub_menu = Menu(student_money_sub_menu_items, "")
			return student_money_sub_menu
			
		
	def show_student_menu(self):
		while True:
			print("\nWelcome " + self.current_user.user_id + " What do you want to do?")
			#getting input from user
			inp = self.student_menu.display(False)
			if inp == "1":
				print("")
				self.display_courses(self.courses)
				try:
					inp = int(input("please Enter a valid course number:"))
				
					if inp > len(self.courses):
							print("Wrong input")
							
					#check if the course already taken by current user	
					elif self.current_user.course_exist(self.courses[inp-1]):
						print("You already picked this course")
					else:
						if self.current_user.can_take_course(self.courses[inp-1]):
							print(self.courses[inp-1].name + " added successfully, money has taken from your account.")
							self.current_user.add_course(self.courses[inp-1])
							self.current_user.take_money(self.courses[inp-1].course_price())
							self.courses[inp-1].registered_users.append(self.current_user)
						else:
							print("You can't take this course.")
				
				except:
					print("You had to enter a number.")
			
			elif inp == "2":
				print("")
				#delete if we have a course
				if len(self.current_user.registered_courses)>0:
					self.display_courses(self.current_user.registered_courses)
					try:
						inp = int(input("please Enter a valid course number:"))
					
						if inp > len(self.current_user.registered_courses):
							print("Wrong input")
						else:
							print(self.current_user.registered_courses[inp-1].name + " deleted successfully, and money has been transferred back to student accounts.")
							self.current_user.add_money(self.current_user.registered_courses[inp-1].course_price())
							self.current_user.delete_course(self.current_user.registered_courses[inp-1])
					except:
						print("You had to enter a number.")
				
				else:
					print("You have no course")
			elif inp == "3":
				print("")
				if len(self.current_user.registered_courses)>0:
					self.display_courses(self.current_user.registered_courses)
				else:
					print("You have no course")
			
			elif inp == "4":
				print('\n#### BUDGET MENU #####')
				print('Your budget is: {}'.format(self.current_user.budget))
				inp = self.student_money_sub_menu.display(False)
				if inp == "1":
					while True:
						try:
							inp = int(input("How much money do you want to add? : "))
							self.current_user.add_money(inp)
							print("Money added succesfully")
							break
						except:
							print("please enter a valid value")
			elif inp == "5":
				print("")
				self.current_user = self.login()
				login = self.manage_login()
				while login is None:
					self.current_user = self.login()
					login = self.manage_login()
		
	def show_admin_menu(self):
		while True:
			print("")
			#getting input from user
			inp = self.admin_menu.display(True)			
			
			
			if inp == "1":
				print("\n*** Offered Courses ***")
				self.display_courses(self.courses)
				
			elif inp == "2":
				print("")
				name = input("What is the name of the course that you want to add? : ")
				credit = int(input("How many credits this course has? : "))
				price = int(input("How much should the course cost? : "))
				print(name + " will be added with " + str(credit) + " credits.")
				sure = input("Are you sure?[Y/N]")
				if sure == "Y" or sure == "y":
					new_course = Course(name, credit, price)
					self.courses.append(new_course)
					print("Course added successfully")
				else:
					print("Course has not added.")
			
			elif inp == "3":
				print("")
			
				self.display_courses(self.courses)
				inp = int(input("Which course do you want to delete?"))
				
				if inp > len(self.courses):
					print("Please enter a valid number")
				else:
					print(self.courses[inp-1].name + " has been deleted and money has been transferred back to student accounts")
					for student in self.users.values():
						if type(student) is Student and student.course_exist(self.courses[inp-1]):
							student.add_money(self.courses[inp-1].course_price())
							student.registered_courses.remove(self.courses[inp-1])
					self.courses.remove(self.courses[inp-1])
					
			elif inp == "4":
				inp = input("\nWhich course do you want to show? : ")
				
				for course in self.courses:
					if course.name == inp:
						if len(course.registered_users) == 0:
							print("There is no student")
						else:
							print("Students taking " + course.name)
							for index,std in enumerate(course.registered_users,1):
								print('{}-{}'.format(index,std.user_id))
			
			elif inp == "5":
				while True:
					print("")
					inp = self.admin_money_sub_menu.display(False)
					#the student list created for reaching the user easily
					students = []
					if inp == "1":
						print("")
						if len(self.users.values()) == 0:
							print("There is no student")
						else:	
							for index,std in enumerate(self.users.values(),1):
								#adding students to list
								students.append(std)
								print('{}-{}'.format(index,std.user_id))
							#this index is for reaching student which is student[inp-1]
							inp = int(input("Which user do you want add money to their account?"))
							if inp > len(self.users.values()):
								print("Please enter a valid number")
							else:							
								student = students[inp-1]
								money = int(input("How much money do you want to add? : "))
								sure = input((str(money) + "$ will be added to " + student.user_id + "\nAre you sure?[Y/N]: "))
								if sure == "Y" or sure == "y":
									self.users[student.user_id].add_money(money)
									print("Money added successfully")
									print("New budget: " + str(self.users[student.user_id].budget))
					
					elif inp == "2":
						print("")
						if len(self.users.values()) == 0:
							print("There is no student")
						else:	
							for index,std in enumerate(self.users.values(),1):
								students.append(std)
								print('{}-{}'.format(index,std.user_id))
							inp = int(input("Which user do you want subtract money to their account?"))
							if inp > len(self.users.values()):
								print("Please enter a valid number")
							else:							
								student = students[inp-1]
								money = int(input("How much money do you want to subtract? : "))
								sure = input((str(money) + "$ will be subtracted to " + student.user_id + "\nAre you sure?[Y/N]: "))
								if sure == "Y" or sure == "y":
									if student.budget >= money:
										self.users[student.user_id].take_money(money)
										print("Money subtracted successfully")
										print("New Budget: " + str(self.users[student.user_id].budget))
									else:
										print("Insufficient balance. Fail to subtract")
					elif inp == "3":
						break
			
				
			elif inp == "6":
				print("")
				if len(self.users.values()) == 0:
					print("There is no user")
				else:
					print("Current users:")
					for index,std in enumerate(self.users.values(),1):
						print('{}-{}'.format(index,std.user_id))
						a = 25
					
			elif inp == "7":
				print("")
				id = input("What is the id(name) of user that you want to create? : ")		
				password = input("What is the password for account? : ")
				budget = int(input("How much money do you want user to have?"))
				
				student = Student(id, password, budget, [])
				self.users[student.user_id] = student
				print("The new user has been added successfully!")
											
			elif inp == "8":
				print("")
				students = []
				if len(self.users.values()) == 0:
					print("There is no user")
				else:
					for index,std in enumerate(self.users.values(),1):
						students.append(std)
						print('{}-{}'.format(index,std.user_id))
						
					inp = int(input("Which user do you want to delete:"))
					if inp > len(self.users.values()):
						print("please enter a valid number")
					else:
						print(students[inp-1].user_id + " deleted!")
						#remove student from its courses registered_user list
						for course in students[inp-1].registered_courses:
							course.registered_users.remove(students[inp-1])
						del self.users[students[inp-1].user_id]
				
			elif inp == "9":
				print("")
				self.current_user = self.login()
				login = self.manage_login()
				while login is None:
					self.current_user = self.login()
					login = self.manage_login()
			         
         
	def build_courses(self):
		courses = []
		
		physics = Course('physics', 4, 300)
		mathematics = Course('mathematics', 6, 500)
		programming = Course('programming', 3, 250)

		courses.append(physics)
		courses.append(mathematics)
		courses.append(programming)
		
		return courses
         
         
	def build_users(self):
		users = {}
		
		student1 = Student('burak', '466', 900, [self.courses[0], self.courses[1]])
		student2 = Student('ayse', '456', 400, [self.courses[1], self.courses[2]])
		
		admin = Admin('admin', 'admin', 10000, [])
		
		users[student1.user_id] = student1
		users[student2.user_id] = student2
		users[admin.user_id] = admin
		
		return users
		
	def display_courses(self, courses):
		print ('Course Name\tCredit\tPrice')
		for index,item in enumerate(courses,1):
			print ('{}-{}\t{}\t{}'.format(index, item.name, item.credits, item.course_price()))
		
		
	def is_input_included_in_all_courses(self, inp):
		for course in self.courses:
			if course.name == inp:
				return course
		return False


class User:
	def __init__(self, user_id, password, budget, registered_courses):
		self.user_id = user_id
		self.password = password
		self.budget = budget
		self.registered_courses = registered_courses

	def can_take_course(self, course):
		if self.budget >= course.course_price():
			return True
		else:
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
		if self.budget - amount < 0:
			print("Insufficent balance")
		else:
			self.budget = self.budget - amount
	

class Course:
	def __init__(self, name, credit, price):
		self.name = name
		self.credits = credit
		self.registered_users = []
		self._price = price

	def display(self):
		print(self.name + "\t" + str(self.credits))

	def delete_course(self):
		pass

	def course_price(self):
		return self._price

class MenuItem:
	def __init__(self, text, number):
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
			print(str(i.number)+"- " + i.text)
		
		return input("Your choise ")
		
	def add_menu_item(self, text, number):
		item = MenuItem(text, number)
		self.items.append(item)

class Student(User):
	def __init__(self, user_id, password, budget, registered_courses):
		User.__init__(self, user_id, password, budget, registered_courses)
		for course in registered_courses:
			course.registered_users.append(self)

class Admin(User):
	def __init__(self, user_id, password, budget, registered_courses):
		User.__init__(self, user_id, password, budget, registered_courses)


		
   a = CourseManagementSystem()
