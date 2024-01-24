student_dictionary = dict({'first_name': 'Kanishkar', 'last_name': 'sadasivam', 'gender': 'Male', 'age': '22','martial_status': 'Single', 'Skills': 'Python', 'Country': 'India', 'city': 'Erode', 'address': 'House no. 118, First street, Thayirpalayam,Chithode'})
print(student_dictionary)
print(len(student_dictionary))
print(student_dictionary['Skills'])
print(type(student_dictionary))
print(student_dictionary.keys())
print(student_dictionary.values())
print(student_dictionary.items())

more_skills = dict(student_dictionary, **{'Skills': 'Python, C, C++'})
print(more_skills)

di = student_dictionary.pop('city')
print(di)

more_skills.pop('Skills')
print(more_skills)

