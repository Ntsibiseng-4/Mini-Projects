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

# SECTION 4: NUMBER CRUNCHING
height_m = height_cm / 100

bmi = weight_cm / (height_m ** 2)
rbmi = round(bmi, 1)

base_fee = 50
student_discount = 10

membership_fee = base_fee - student_discount

loyalt_point = 100
loyalt_point += 20

bouns = 2 ** 3
loyalt_point += bouns

reward_tiers = loyalt_point // 50

print("\n" + "=" * 40)
print("BML:", bmi)
print("Membership Fee", membership_fee)
print("Loyalty Points:", loyalt_point)
print("Reward Tiers:", reward_tiers)
print("\n" + "=" * 40)

# SECTION 5: CONDITIONAL LOGIC

#BMI Catetory
if rbmi < 18.5:
    weight = "Underweight"
elif rbmi >= 18.5 or rbmi <= 24.5:
    weight = "Normal Weight"
elif rbmi >= 25 or rbmi <= 29.9:
    weight = "Overweight"
else:
    weight = "Obese"
    
#Membership Categoty
if age < 18:
    member = "Junior Member"
elif age >= 65:
    member = "Senior Member"
elif is_student == True and age >= 18:
    member = "Student Member"
else:
    member = "Standard Member"


#Membership Tier category
is_eligible = not((not is_valid_email) or (age  < 13))  # expressing it as "IS eligible" instead of "is NOT eligible,"

print("\n" + "=" * 40)
print("Username:", username)
print(f'BMI: {rbmi} ({weight})')
print("Tier:", member)
print(f'Loyalty pts: {loyalt_point} ({reward_tiers} reward tiers)')
print("Eligible:", is_eligible)
