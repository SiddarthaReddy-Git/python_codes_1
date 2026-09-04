name = input("Enter your name: ")
adm_id = input("Enter Admission ID: ")
roll_number = int(input("Enter Roll Number: "))
maths = int(input("Enter Maths Marks: "))
physics = int(input("Enter Physics Marks: "))
chemistry = int(input("Enter Chemistry Marks: "))

average_marks = (maths + physics + chemistry) / 3


print("name:", name)
print("Admission ID:", adm_id)
print("Roll Number:", roll_number)
print("Maths marks", maths )
print(" Physics Marks:", physics )
print("Chemistry Marks:", chemistry)
print(f"Average marks: {average_marks:.2f}")