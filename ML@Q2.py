dog={}
dog['name']='maxi'
dog['color']='brown'
dog['breed']='husky'
dog['legs']=4
dog['age']='two years'
print("dog_dictionary=",dog)
student={'first_name': 'Akshay','last_name':'Mittapally','gender':'Male','age':23,
'Marital status':'single','skills':['Quick learner','Leadership'],'country':'USA','city':'kansas','address':"6655 w 141 st"}
print("student_dictionary=",student)
print("length of the student dictionary is:",len(student))
student.get('skills')
student['skills']=['computer proficiency','cummunication skills']
print('student dictionary with updated skills is student=:',student)
print(type(student['skills']))
keylist=list(student.keys())
print('student keys as list:',keylist)
valueslist=list(student.values())
print('student values as list:',valueslist)
