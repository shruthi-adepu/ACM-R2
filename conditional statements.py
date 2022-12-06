my_num="12345"
print(my_num)
print(type(my_num))
also_my_num=float(my_num)
print(also_my_num)
print(type(also_my_num))
new_string="abc"+"def"
print(new_string)
print(type(new_string))
will_work= "abc" * 3
print(will_work)
print(type(will_work))
#defining a new function
def add_five(input_var):
    output_var=input_var+5
    return output_var
new_number=add_five(10)
print(new_number)
print(6>7)
var_one=4
var_two=16
print(var_one>var_two)
print(var_two >= var_one)
print(var_two==var_one**2)
def evaluate_temp(temp):
#set an initial message
    message = "Normal temperature."
#update value of message only if temp is greater than 38
    if temp>38:
        message = "Fever!"
    return message 
print(evaluate_temp(37))
print(evaluate_temp(40))
#for weather forecast
def evaluate_weather(humidity):
    message="Cloudy."
    if humidity<0.5:
     message="Dry!"
    return message
print(evaluate_weather(0.3))
print(evaluate_weather(1))

    