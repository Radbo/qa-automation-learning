def my_function():
    local_var = "I'm local variable"
    print(local_var)

my_function()


variable = "I'm a variable out of scope"


def my_function_2():
    variable = "I'm a local variable inside function"
    print(variable)


my_function_2()
print(variable)

COMFORTTABLE_TEMPERATURE = 25


def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
    return COMFORTTABLE_TEMPERATURE - temperature


print(get_diff_from_comfortable_temperature(temperature=14))


global_var = "I'm a global variable"


def my_function_changer():
    global global_var
    global_var = "I defined inside the scope of my_function_changer"
    print(global_var)


my_function_changer()
print(global_var)

DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False
    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True
    
    return level_up


print(is_leveled_up(current_experience=49, gained_experience=179))