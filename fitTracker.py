# SECTION 1: VARIABLES & NAMING CONVENTIONS
full_name = "Jane DOE"
age = 25
email = "jane.doe@gmail.com"
height_cm = 165.0
weight_cm = 60.0
is_student = True

print("=" * 40)
print("Name:", full_name)
print("Age:", age)
print("Email:", email)
print("Height:", height_cm)
print("Weight:", weight_cm)
print("Student:", is_student)
print("=" * 40)

# SECTION 2: DATA TYPE VALIDATION
print("=" * 40)
print("Age is an int:", isinstance(age, int))
print("Height is an float:", isinstance(age, float))
print("Weight is an float:", isinstance(age, float))
print("Student is an boolean:", isinstance(age, bool))
print("What type is the email:", type(email))
print("=" * 40)

# SECTION 3: STRING PROCESSING
fixed_name = full_name.strip() and full_name.title()
username = full_name[0:3] + str(age)
is_valid_email = "@" in email and "." in email

print("=" * 40)
profile_summary = f'{fixed_name} ({age}) |{username}|{email}| Valid: {is_valid_email}'
print(profile_summary)
print("=" * 40)