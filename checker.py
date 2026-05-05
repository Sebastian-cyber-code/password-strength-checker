def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()" for char in password):
        score += 1

    if score == 3:
        return "Strong"
    elif score == 2:
        return "Medium"
    else:
        return "Weak"

password = input("Enter password: ")
print("Strength:", check_password(password))
