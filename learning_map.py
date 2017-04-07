"""
logic behind studied and unstudied skill
"""

def studied_skill():
    for skill in map_skills.keys():
        if(map_skills[skill] == 1):
            print(skill)

def unstudied_skill():
    for skill in map_skills.keys():
        if(map_skills[skill] == 0):
            print(skill)
