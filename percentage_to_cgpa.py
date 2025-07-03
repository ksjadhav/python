def percentage_to_cgpa(percentage):
    """
    Converts percentage to CGPA on a 10-point scale.
    Formula: CGPA = Percentage / 9.5
    """
    try:
        percentage = float(percentage)
        if percentage < 0 or percentage > 100:
            return "Invalid percentage value. It should be between 0 and 100."
        cgpa = percentage / 9.5
        return round(cgpa, 2)
    except ValueError:
        return "Please enter a valid numeric percentage."

# Example usage:
percentage = input("Enter your percentage: ")
result = percentage_to_cgpa(percentage)
print("Your CGPA is:", result)
