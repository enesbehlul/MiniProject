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
