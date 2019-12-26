from Menu import Menu
from MenuItem import MenuItem
from Student import Student
from User import User
from Admin import Admin
from Course import Course


class CourseManagementSystem:
	def __init__(self):
		self.courses = self.build_courses()
		self.users = self.build_users()
		self.admin_menu = self.build_menus("admin")
		self.student_menu = self.build_menus("student")
		self.current_user = self.login()
		if type(self.current_user) is Student:
			self.show_student_menu()
		elif type(self.current_user) is Admin:
			self.show_admin_menu()
			
	
	def login(self):
		userId = input("Please enter your Id: ")
		password = input("Please enter your password: ")
		#check if the user exist
		if userId in self.users:
			if self.users[userId].password == password:
				self.current_user = self.users[userId]
				print("Login success.")
				return self.users[userId]
			else:
				print("Wrong password")
		else:
			print("No such user")
	
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
		
		if menu_type == "student":
			student_menu_items = []
			student_menu_items.append(MenuItem("Add courses to my courses", 1))
			student_menu_items.append(MenuItem("Delete a course from my courses", 2))
			student_menu_items.append(MenuItem("Show my courses", 3))
			student_menu_items.append(MenuItem("Budget Menu", 4))
			student_menu_items.append(MenuItem("Exit", 5))
			#creating student menu and header
			student_menu = Menu(student_menu_items, "")
			return student_menu
		
		
	def show_student_menu(self):
		inp = 0
		while True:
			for i in self.student_menu.items:
				print(str(i.number)+"- " + i.text)
		
			#getting input from user
			inp = input("Your choise: ")
			
			if inp == "1":
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
							self.current_user.take_money(self.current_user.registered_courses[inp-1].course_price())
				
				except:
					print("You had to enter a number.")
			
			elif inp == "2":
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
				self.display_courses(self.current_user.registered_courses)
			
			elif inp == "4":
				print('\n#### BUDGET MENU #####')
				print('Your budget is: {}'.format(self.current_user.budget))
				print('What do you want to do?\n1-Add Money\n2-Go to main menu')
				inp = input("Your choise:")
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
				break
								
		
		
	def show_admin_menu(self):
		for i in self.admin_menu.items:
			print(str(i.number)+"- " + i.text)
			         
         
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
		
		users[student1.userId] = student1
		users[student2.userId] = student2
		users[admin.userId] = admin
		
		return users
		
	def display_courses(self, courses):
		print ('Course Name\tCredit')
		for index,item in enumerate(courses,1):print ('{}-{}\t{}'.format(index,item.name,item.credits))
		
	def isInputIncludedInAllCourses(self, inp):
		for course in self.courses:
			if course.name == inp:
				return course
		return False



		
a = CourseManagementSystem()
