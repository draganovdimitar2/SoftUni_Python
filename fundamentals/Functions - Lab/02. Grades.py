def grade(user_input):
    if user_input > 5.49:
        return "Excellent"

    elif user_input > 4.49:
        return "Very Good"

    elif user_input > 3.49:
        return "Good"

    elif user_input > 3:
        return "Poor"
    
    else:
        return "Fail"


user_input = float(input())
print(grade(user_input))