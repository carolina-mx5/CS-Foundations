# takes user string input
second = input("Enter Seconds: ")

# converts string input into int
sec_int = int(second)

# calculates how many whole hours
hours = sec_int // 3600

# calculates how many remainding, whole minutes
minutes = (sec_int % 3600) // 60

# calculates how many remainding seconds
sec_calc = (sec_int % 3600) % 60

# converts hours, minutes, seconds, back to strings 
# so we can concatenate output
hr_str = str(hours)
min_str = str (minutes)
sec_str = str(sec_calc)

# prints calculations
print("\n" + hr_str + " hours")
print(min_str + " minutes")
print(sec_str + " seconds")