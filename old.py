print('****Welcome to Course Management System****\nPlease provide login information')
admin_dict={'admin':'123'}

students=[{'burak':'466','budget':900,'courses':['mathematics','physics']},{'ayse':'456','budget':400,'courses':['physics']}]

courses={'physics':4,
         'mathematics':3,
         'programming':3}


def menu_selection(user_id):
    if user_id in admin_dict.keys() and user_pwd == admin_dict[user_id]:
        while 1:
            
            
            print('\nWelcome ' +user_id+ '! What do you want to do?\n',
                                '\n1-List courses',
                                '\n2-Create a course',
                                '\n3-Delete a course',
                                '\n4-Show students registered to a course',
                                '\n5-Users Budget Menu',
                                '\n6-List Users',
                                '\n7-Create User',
                                '\n8-Delete User',
                                '\n9-Exit')
            selected_menu=input('Your choice: ').strip()
            if selected_menu in [str(i) for i in range(1,10)]:break
            else:print('You entered the incorrect value, please try again.')
                
    elif user_id in [list(student.keys())[0] for student in students]:
        while 1:
            
            print('\nWelcome ' +user_id+ '! What do you want to do?\n',
                                '\n1-Add courses to my courses',
                                '\n2-Delete a course from my courses',
                                '\n3-Show my courses',
                                '\n4-Budget Menu',
                                '\n5-Exit')
            selected_menu=input('Your choice: ').strip()
            if selected_menu in [str(i) for i in range(1,6)]:break
            else:print('You entered the incorrect value, please try again.')
    return selected_menu
    
#Input
def login_page():
    while 1:
        global user,user_id,user_pwd
        user_id=input('Id: ')
        user_pwd=input('Password: ')
        
        
        #Admin
        if user_id in admin_dict.keys() and admin_dict.get(user_id)==user_pwd:
            user='admin'
            print('Successfully logged in!')
            break
        
        #Student
        elif user_id in [list(student.keys())[0] for student in students] and [list(student.values())[0] for student in students if list(student.keys())[0]==user_id]==[user_pwd]:
            user='student'
            print('Successfully logged in!')
            break
        
        
        else:
            print('\nInvalid id or password please try again')
login_page() 
#while True:
while 1:
    
    
    
    #ADMİN
    if user=='admin':
        selected_menu=menu_selection(user_id)
        
        
        #List Courses
        if selected_menu=='1':
            print('\n*** Offered Courses ***\n')
            print ('Course Name\tCredit')
            for index,item in enumerate(courses,1):
                
                print ('{}-{}\t{}'.format(index,item,courses[item]))
        
        
        #Create a course
        elif selected_menu=='2':
            while 1:
                course_name=input('What is the name of the course that you want to add? ')
                try:
                    course_credit=int(input('How many credits this course has? '))
                except:
                    print('Please enter an integer value.')
                    continue
                print('\n{} will be added with {} credits.'.format(course_name,course_credit))
                
                while 1:
                    confirm=input('Are you sure?[Y/N] ')
                    
                    if confirm=='Y' or confirm=='y':
                        print('\n{} has been added to courses with {} credits'.format(course_name,course_credit))
                        courses[course_name]=course_credit
                        break
                    elif confirm=='N' or confirm=='n':
                        break
                break
                    
                    
                    
        #Delete a course
        elif selected_menu=='3':
                        
            #List of Courses
            print ('Course Name\tCredit')
            for index,item in enumerate(courses,1):print ('{}-{}\t{}'.format(index,item,courses[item]))
            
            while 1:
                try:
                    del_course_int=int(input('Which course do you want to delete? '))
                    
                except:
                    print('Please enter an integer value.')
                    continue
                    
                
                print('\n{} has been deleted and money has been transferred back to student accounts.'.format(list(courses.keys())[del_course_int-1]))
                for student in students:
                    for course in student['courses']:
                        if list(courses.keys())[del_course_int-1] == course:
                            
                            student['courses'].remove(course)
                            student['budget']+=(courses[list(courses.keys())[del_course_int-1]])*100
                        
                del courses[list(courses.keys())[del_course_int-1]]
                break
          
         
        
        #Show students registered to a course
        elif selected_menu=='4':
            course_name=input('Which course do you want to show? ')
            
            val=0
            counter=0
            
            for student in students:
                if course_name in  student['courses']:
                    if val == 0:
                        val+=1
                        print('Course Name: {}\nStudents taking {}:'.format(course_name,course_name))
                    if course_name in  student['courses']:
                        counter+=1
                        print('{}-{}'.format(counter,list(student.keys())[0]))
            if counter ==0:
                print("\nThis course doesn't exist, please provide a valid input")
        #Users Budget Menu
        elif selected_menu=='5':
            print ('User\tMoney')
            for index,student in enumerate(students,1):
                print ('{}-{}\t{}'.format(index,list(student.keys())[0],student[list(student.keys())[1]]))
                            
                            #selected menu user budget input
            while 1:
                print('\nWhat do you want to do?\n\n1-Add money to user\n2-Subtract money from user\n3-Back to admin menu')
                selected_menu_user_budget=input('Your choice: ')
                
                
                #add money
                if selected_menu_user_budget=='1':
                    print('Which user do you want add money to their account?')
                    for index,student in enumerate(students,1):
                        print ('{}-{}'.format(index,list(student.keys())[0]))
                    while 1:
                        try:
                            user_budget_choosen_user = int(input('Your choice: '))
                        
                        except:
                            continue
                        break
                    
                    while 1:
                        try:how_much=int(input('How much money do you want to add? '))
                        except:continue
                        break
                    
                    print('{} $ will be added to {}.'.format(str(how_much),list(students[user_budget_choosen_user-1].keys())[0]))
                    
                    
                    while 1:
                        
                        confirm=input('Are you sure?[Y/N]: ')
                    
                    
                        if confirm=='Y' or confirm=='y':
                        
                            students[user_budget_choosen_user-1]['budget']=students[user_budget_choosen_user-1]['budget']+how_much
                            break
                        if confirm=='N' or confirm=='n':
                            break
                    
                #subtract money
                elif selected_menu_user_budget=='2':
                    print('Which user do you want add money to their account?')
                    for index,student in enumerate(students,1):
                        print ('{}-{}'.format(index,list(student.keys())[0]))
                    
                    while 1:
                        try:
                            user_budget_choosen_user = int(input('Your choice: '))
                            
                        except:
                            print('Please enter a valid value')
                            continue
                        break
                    
                    while 1:
                        try:
                            how_much=int(input('How much money do you want to subtract? '))
                            
                            if how_much> students[user_budget_choosen_user-1]['budget']:
                                continue
                        except:
                            print('Please enter a valid')
                            continue
                        break
                    
                    print('\n{} $ will be subtracted to {}.'.format(str(how_much),list(students[user_budget_choosen_user-1].keys())[0]))
                    
                    
                    while 1:
                        confirm=input('Are you sure?[Y/N]: ')
                        
                        
                        if confirm=='Y' or confirm=='y':
                            
                            students[user_budget_choosen_user-1]['budget']=students[user_budget_choosen_user-1]['budget']-how_much
                            break
                        if confirm=='N' or confirm=='n':
                            break
                    
                #Back to admin menu
                elif selected_menu_user_budget=='3':
                    break
    
    
        #List users
        elif selected_menu=='6':
            for index,student in enumerate(students,1):
                print ('{}-{}'.format(index,list(student.keys())[0]))
    
    
    
        #Create user
        elif selected_menu=='7':
            user_name=input('What is the name of user that you want to create? ')
            
            if user_name not in [list(i.keys())[0] for i in students]:
                while 1:
                    while 1:
                    #user pwd
                        try:added_user_pwd=int(input('What is the password for account? '))
                        except:continue
                        break
                    while 1:
                        #user budget
                        try:user_budget=int(input('How much money do you want user to have? '))
                        except:continue
                        break
                    break
                students.append({user_name:added_user_pwd,'budget':user_budget,'courses':[]})
                print('\nThe new user has been added successfully!')

            else:
                print('\nAlready registered with this name')
                continue
            
            
        #Delete user
        elif selected_menu=='8':
            print('Current Users:')
            for index,student in enumerate(students,1):
                print ('{}-{}'.format(index,list(student.keys())[0]))
            
            
            while 1:
                try:
                    selected_user=int(input('Which user do you want to delete: '))
                
                
            
                    if list(students[selected_user-1].keys())[0] in [list(i.keys())[0] for i in students]:
                        
                        print('\n{} is deleted!'.format(list(students[selected_user-1].keys())[0]))
                        del students[selected_user-1]
                        
                        break

                except:
                    print('\nPlease enter a valid value')
                    continue
            
        #Exit
        elif selected_menu=='9':
            login_page()
    
    
    #STUDENT
    elif user=='student':
        selected_menu=menu_selection(user_id)
        
        #Add courses to my courses
        if selected_menu == '1':
            print('\n*** Offered Courses ***\n')
            print ('Course Name\tCredit')
            for index,item in enumerate(courses,1):
                
                print ('{}-{}\t{}'.format(index,item,courses[item]))
            while 1:
                try:
                    selected_course=int(input('Which course do you want to take (Enter 0 to go to main menu)?'))
                                                               
                    if selected_course!=0:
                        selected_course=list(courses.keys())[selected_course-1]
                        if selected_course in courses:
                            for student in students:
                                if list(student.keys())[0]==user_id and selected_course not in list(student.values())[2]:
                                    if student['budget'] >=courses[selected_course]*100:
                                        student['courses'].append(selected_course)
                                        student['budget']-=courses[selected_course]*100
                                        print('{} has been successfully added to your courses.'.format(selected_course))
                                        break
                                    else:
                                        print("You don't have enough money in your account. Please deposit money, or choose a course with lesser credit.")
                                        break
                                    
                                else:
                                    print('This course is already in your profile, please choose another course:')
                                    break
                    
                    
                        else:print('no such course, please enter a valid value')           
                    elif selected_course==0:
                        break
                except ValueError:
                    print('please enter a valid value')
                    continue
        
        #Delete a course from my courses
        elif selected_menu=='2':
            for student in students:
                if list(student.keys())[0]== user_id:
                    print('Course Name\tCredit')
                    for index,course in enumerate(student['courses'],1):
                        
                        print('{}-{}\t{}'.format(index,course,courses[course]))
                while 1:
                    try:delete_course=int(input('Which course do you want to remove? '))
                    except:
                        print('please enter a valid value')
                        continue
                    break
                print('You have chosen: {}'.format(student['courses'][delete_course-1]))
                print('{}$ will be returned to your account.'.format(courses[student['courses'][delete_course-1]]*100))
                
                while 1:
                    confirm=input('Are you sure that you want to remove this course? [Y/N]')
                    if confirm=='Y' or confirm=='y':
                        student['budget']+=courses[student['courses'][delete_course-1]]*100
                        del student['courses'][delete_course-1]
                        print('Course has been deleted from your profile')
                        break
                    elif confirm=='N' or confirm=='n':break
                
                    else:
                        print('please enter a valid value')
                        continue
                break
            
                        
        #Show my courses 
        elif selected_menu=='3':
            print('Course Name\tCredit')
            for student in students:
                if list(student.keys())[0]== user_id:
                    for index,course in enumerate(student['courses'],1):
                        print('{}-{}\t{}'.format(index,course,courses[course]))
    
    
    
        #Budget Menu 
        elif selected_menu=='4':
            print('\n#### BUDGET MENU #####')
            for student in students:
                if list(student.keys())[0]== user_id:
                    print('Your budget is: {}'.format(student['budget']))
                    print('What do you want to do?\n1-Add Money\n2-Go to main menu')
                while 1:
                    try:
                        selected_menu_budget_menu=int(input('Your choice: '))
                        if selected_menu_budget_menu!=1 and selected_menu_budget_menu!=2:continue
                        elif selected_menu_budget_menu==1:
                            while 1:
                                try:
                                    how_much=int(input('Amount of money:'))
                                    student['budget']+=how_much
                                    print('Your budget has been updated.')
                                
                                except:continue
                                break
                            break
                        elif selected_menu_budget_menu==2:
                            break
                    except:
                        print('please enter a valid value')
                        continue
                    break
                break
        
        
        elif selected_menu=='5':
            login_page()
