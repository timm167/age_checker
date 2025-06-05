from datetime import datetime, date
dob = datetime.strptime("2009-12-01", "%Y-%m-%d").date()
today = date.today()
age = today.year - dob.year

print(today.month)
print(dob.month)

if(today.month, today.day) < (dob.month, dob.day):
    print("hello")
    age -= 1
    
print(age)
    