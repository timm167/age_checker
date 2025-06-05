from datetime import date, datetime

def age_checker(dob):
    if type(dob) != str:
        raise TypeError("Error: Invalid Type")
    
    try:
        dob = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - dob.year
        
        if(today.month, today.day) < (dob.month, dob.day):
            age -= 1
            
        if age < 16:
            return f"Access denied. {age} year olds are not old enough. Required age: 16"
        
        return f"Access granted. {age} year olds are welcomed."
        

    except ValueError:
        raise ValueError("Error: Invalid DOB Format")
    

age_checker("2024-01-01")
