student = {"name":"joe","course":"science","age":"22"}

#get() method
# print(student.get("phone"," "))

# student ['phone'] = "2222-2222"
# student['name'] = "jane"


# update() 
student.update({'name':'jane','age':21,'phone':'2222-30303'})
print(student)


#pop

phone = student.pop('phone')
print(student)