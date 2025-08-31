import re

def check_password_strength(password):
    # Rules for a strong password:
    # At least 8 characters
    # At least one uppercase letter
    # At least one lowercase letter
    # At least one digit
    # At least one special character

    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    if strength == 5:
        remarks = "Very Strong 💪"
    elif strength == 4:
        remarks = "Strong ✅"
    elif strength == 3:
        remarks = "Moderate ⚠️"
    else:
        remarks = "Weak ❌"

    return remarks

# Run the program
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Password Strength: {result}")
