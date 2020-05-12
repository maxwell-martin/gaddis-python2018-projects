ASSESSMENT_VALUE_RATE = 0.60
TAX_RATE = 0.0072

actual_value = float(input("Enter actual value of property: "))

assessment_value = actual_value * ASSESSMENT_VALUE_RATE

print("Assessment value: $", format(assessment_value, ",.2f"), sep="")

tax = assessment_value * TAX_RATE

print("Property tax: $", format(tax, ",.2f"), sep="")
