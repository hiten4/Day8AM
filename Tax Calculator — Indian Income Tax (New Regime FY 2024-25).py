def get_valid_income():
    while True:
        try:
            income = float(input("Enter Annual Income (₹): "))
            if income >= 0:
                return income
            else:
                print("Income cannot be negative.")
        except ValueError:
            print("Invalid input. Enter numeric value.")


def calculate_tax(income):
    STANDARD_DEDUCTION = 75000
    taxable_income = max(0, income - STANDARD_DEDUCTION)

    slabs = [
        (0, 300000, 0.00),
        (300000, 700000, 0.05),
        (700000, 1000000, 0.10),
        (1000000, 1200000, 0.15),
        (1200000, 1500000, 0.20),
        (1500000, float('inf'), 0.30)
    ]

    total_tax = 0
    breakdown = []

    for lower, upper, rate in slabs:
        if taxable_income > lower:
            taxable_amount = min(taxable_income, upper) - lower
            tax = taxable_amount * rate
            total_tax += tax

            breakdown.append(
                (lower, upper, taxable_amount, rate, tax)
            )

    effective_rate = (total_tax / income) * 100 if income > 0 else 0

    return taxable_income, breakdown, total_tax, effective_rate


def display_result(income):
    taxable_income, breakdown, total_tax, effective_rate = calculate_tax(income)

    print("\n----- TAX SUMMARY (FY 2024-25 New Regime) -----")
    print(f"Gross Income: ₹{income:,.2f}")
    print("Standard Deduction: ₹75,000")
    print(f"Taxable Income: ₹{taxable_income:,.2f}\n")

    print("Slab-wise Breakdown:")
    for lower, upper, taxable_amount, rate, tax in breakdown:
        upper_display = "Above" if upper == float('inf') else f"{upper:,.0f}"
        print(
            f"₹{lower:,.0f} - ₹{upper_display} | "
            f"Income in Slab: ₹{taxable_amount:,.2f} | "
            f"Rate: {rate*100:.0f}% | "
            f"Tax: ₹{tax:,.2f}"
        )

    print("\nTotal Tax: ₹{:,.2f}".format(total_tax))
    print("Effective Tax Rate: {:.2f}%".format(effective_rate))


if __name__ == "__main__":
    income = get_valid_income()
    display_result(income)