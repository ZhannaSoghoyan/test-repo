pythonist_skills = [
    {"Gohar" : "Python Basics"},
    {"Lilit" : "OOP"},
    {"Janna" : "Git"},
    {"Luiza" : "C++"},
    {"Lilit" : "Business Analyst"},
    {"Janna" : "Numpy"},
    {"Luiza" : "Animation"},
    {"Gohar" : "Business Consultant"}
]
some_list = []
for i in range(len(pythonist_skills)):
    for j in range(len(pythonist_skills)):
        for val in pythonist_skills[j]:
            print(pythonist_skills[j].keys())
            if pythonist_skills[i].keys() == pythonist_skills[j].keys():
                if isinstance(pythonist_skills[i][val], list):
                    pythonist_skills[i][val].append(pythonist_skills[j][val])
                    pythonist_skills[j] = {}
                else:
                    pythonist_skills[i][val] = [pythonist_skills[j][val]]

l = len(pythonist_skills)
while l:
    if pythonist_skills[l-1] == {}:
        del pythonist_skills[l-1]
    l -= 1


print(pythonist_skills)

        

