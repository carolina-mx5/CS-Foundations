# takes user input for name, age, city
name = input("What is your name? ")
age = input ("What is your age? ")
city = input ("What city do you live in? ")

# converts string age, into int, so we can calculate the new age
age_num = int(age)

new_age = age_num + 1  # adds 1 to the current age, so we get next year's age

# converts next year's age back into string so we can concatenate the string output
string_age = str(new_age)  

# concatenates the user's input to the strings we have
print("Hello " + name + "!\nYou are " + age + " years old and live in " + city + ".\nNext year, you will be " + string_age + " years old.")