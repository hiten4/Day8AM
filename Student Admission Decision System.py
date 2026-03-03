def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def get_valid_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["yes", "no"]:
            return value
        print("Enter 'yes' or 'no' only.")


def get_valid_category(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["general", "obc", "sc_st"]:
            return value
        print("Enter one of: general / obc / sc_st.")


def admission_decision():
    # Inputs
    entrance_score = get_valid_number("Entrance Score (0-100): ", 0, 100)
    gpa = get_valid_number("GPA (0-10): ", 0, 10)
    has_recommendation = get_valid_yes_no("Recommendation (yes/no): ")
    category = get_valid_category("Category (general/obc/sc_st): ")
    extracurricular_score = get_valid_number("Extracurricular Score (0-10): ", 0, 10)

    # Merit Rule (Auto Admit)
    if entrance_score >= 95:
        print("\nResult: ADMITTED (Scholarship)")
        print("Reason: Entrance score ≥ 95 (Merit rule applied)")
        return

    # GPA Check
    if gpa < 7.0:
        print("\nResult: REJECTED")
        print("Reason: GPA below minimum requirement (7.0)")
        return

    # Category Cutoffs
    cutoffs = {
        "general": 75,
        "obc": 65,
        "sc_st": 55
    }

    base_cutoff = cutoffs[category]

    # Bonus Calculation
    bonus = 0
    bonus_details = []

    if has_recommendation == "yes":
        bonus += 5
        bonus_details.append("+5 (recommendation)")

    if extracurricular_score > 8:
        bonus += 3
        bonus_details.append("+3 (extracurricular)")

    effective_score = entrance_score + bonus

    print(f"\nBonus Applied: {' '.join(bonus_details) if bonus_details else 'None'}")
    print(f"Effective Score: {effective_score}")

    # Final Decision
    if effective_score >= base_cutoff:
        print("\nResult: ADMITTED (Regular)")
        print(f"Reason: Meets {category.upper()} cutoff "
              f"({effective_score} ≥ {base_cutoff}) and GPA requirement ({gpa} ≥ 7.0)")
    elif effective_score >= base_cutoff - 5:
        print("\nResult: WAITLISTED")
        print("Reason: Close to cutoff, placed on waitlist")
    else:
        print("\nResult: REJECTED")
        print("Reason: Does not meet category cutoff")


# Run system
admission_decision()