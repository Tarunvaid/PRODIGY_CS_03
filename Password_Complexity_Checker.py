import re

def password_strength_checker(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    # Check how many criteria are met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])

    # Determine the strength of the password
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback on which criteria are not met
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# Main program
if __name__ == "__main__":
    while True:
        password = input("Enter your password: ")
        strength, feedback = password_strength_checker(password)

        print(f"Password Strength: {strength}")
        if feedback:
            print("Feedback:")
            for f in feedback:
                print(f"- {f}")
        
        if strength in ["Very Strong", "Strong"]:
            break
        else:
            print("\nPlease try again with a stronger password.\n")
