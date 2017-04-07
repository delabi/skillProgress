map_skills = {'Programming Logic': 0,
              'Agile Methodology': 0,
              'Test Driven Development': 0,
              'Git': 0,
              'OOP': 0}

def run():
   x = True

   while True:
       main_interface()

def main_interface():
    choice = input("\t\tBOOTCAMP LEARNING MAP\nChoose an action\n\t1. Add skill\n\t2. View skills\n\t3. Exit\n")
    if (choice == '1'):
        add_skill()
    elif (choice == '2'):
        action = input("Choose skills to view\n\t1. View all skills\n\t2. View Studied Skills\n\t3. View Unstudied Skills\n\t4. View Progress\n")
        # print(type(action))
        submenu(action)
    else:
        pass

def submenu(action):
    if action == '1':
        for skill in map_skills.keys():
            print(skill  + "\n")
    elif action == '2':
        studied_skill()
    elif action == '3':
        unstudied_skill()
    elif action == '4':
        progress()
    else:
        print("Invalid Input\n")

def add_skill():
    for skill in map_skills.keys():
        print(skill)
    new_skill = input("Enter new skill: ")
    if new_skill in map_skills.keys():
        map_skills[new_skill] = 1
        # exit_choice = input("Do you want to view studied skills? (y/n) ")
        # if exit_choice == 'y':
        #     studied_skill
        # else:
        #     main_interface()
    else:
        print("The skill does not exist.")

def studied_skill():
    for skill in map_skills.keys():
        if(map_skills[skill] == 1):
            print(skill)

def unstudied_skill():
    for skill in map_skills.keys():
        if(map_skills[skill] == 0):
            print(skill)

def progress():
    count_studied = 0
    for skill in map_skills.keys():
        if(map_skills[skill] == 1):
            count_studied +=1
    all_skills = len(map_skills)
    progress_percentage = (count_studied/all_skills) * 100
    print(str(progress_percentage) + "%")


run()
