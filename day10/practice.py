def format_name(f_name, l_name):
    f_name_modified = f_name.title()
    l_name_modified = l_name.title()

    # print(f"{f_name_modified} {l_name_modified}")

    return f"{f_name_modified} {l_name_modified}"  #this goes in the place of the function call

full_name_modified = format_name("ADITI", "LIMKAR")  #hence we can assign its value to a var
# same as:
output = len("Angela")

print(full_name_modified)


def format_name_2(f_name, l_name):
    if f_name=="" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))


# Storing Functions as a Variable Value
# You can store a reference to a function as a value to a variable. e.g.

def add(n1, n2):
    return n1 + n2
            
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8
