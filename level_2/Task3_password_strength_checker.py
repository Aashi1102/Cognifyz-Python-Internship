# Password Strength Checker

def password_strength(password):

    length= len(password)

    #Check if there are uppercase letters
    has_upper = any(char.isupper() for char in password)

    #Check if there are lowercase letters
    has_lower = any(char.islower() for char in password)

    #Check if there are digits
    has_digit = any(char.isdigit() for char in password)

    #Check if there are special characters
    has_specialchar = any(not char.isalnum() for char in password)

    #Determine strength
    strength = sum([has_upper, has_lower, has_digit, has_specialchar])

    
    if length >=12 and strength == 4:
        return "Strong" 
    elif length >=8 and strength >=3:
        return "Moderate"
    else:
        return "Weak"
    


password = input("Enter your password: ")
strength = password_strength(password)
print(f"Your password strength is: {strength}") 
