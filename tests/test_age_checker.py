from lib.age_checker import age_checker
import pytest
import datetime

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

def test_for_underage_users_outputs_denied_entry():
    age_check = age_checker("2025/01/01")
    year = datetime.datetime.now().year()
    assert age_check == "Access denied. 1 year olds are not old enough."

print(datetime.datetime.now().year())
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