# takes user stirng input
f_input = input("Temperature in Fahrenheit: ")

# converts string input, to int
F = int(f_input)

# calculates F to C
C = (F - 32) * 5/9

# rounds C to 2 decimal places and assigns value to C_round
C_round = round(C, 2)

# converts int to string so we can concatenate to strings later
C_str = str(C_round)

# "\u00b0" is the unidcode for the degree symbol

print(f_input + "\u00b0F = " + C_str + "\u00b0C")