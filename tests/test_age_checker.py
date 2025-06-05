from lib.age_checker import age_checker
import pytest
from datetime import date, datetime


def test_dob_is_not_string_outputs_invalid():
    
    with pytest.raises(Exception) as e:
        age_check = age_checker(11)
    
    error_message = str(e.value)
    
    assert error_message == "Error: Invalid Type"

def test_dob_is_empty_string_outputs_error():
    
    with pytest.raises(Exception) as e:
        age_check = age_checker("")
    
    error_message = str(e.value)
    
    assert error_message == "Error: Invalid DOB Format"
    
def test_string_text_outputs_invalid_format():
    with pytest.raises(Exception) as e:
        age_check = age_checker("hello")
    
    error_message = str(e.value)
    
    assert error_message == "Error: Invalid DOB Format"

def test_for_underage_users_outputs_age_and_denied_entry():
    age_check = age_checker("2024-01-01")
    dob = datetime.strptime("2024-01-01", "%Y-%m-%d").date()
    today = date.today()
    age = today.year - dob.year
    
    if(today.month, today.day) < (dob.month, dob.day):
        age -= 1
        
    assert age_check == f"Access denied. {age} year olds are not old enough. Required age: 16"

def test_for_older_users_outputs_age_and_valid_entry():
    age_check = age_checker("2000-01-01")
    dob = datetime.strptime("2000-01-01", "%Y-%m-%d").date()
    today = date.today()
    age = today.year - dob.year
    
    if(today.month, today.day) < (dob.month, dob.day):
        age -= 1
        
    assert age_check == f"Access granted. {age} year olds are welcomed."

def test_for_fringe_underage_users_outputs_age_and_denied_entry():
    age_check = age_checker("2009-12-01")
    dob = datetime.strptime("2009-12-01", "%Y-%m-%d").date()
    today = date.today()
    age = today.year - dob.year
    
    if(today.month, today.day) < (dob.month, dob.day):
        age -= 1
        
    assert age_check == f"Access denied. {age} year olds are not old enough. Required age: 16"

'''
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.
'''