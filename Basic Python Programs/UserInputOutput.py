user_name = input("Enter User Name: ")
if len(user_name) > 2:      # Ensure UserName has minimum 3 Characters 
    print("Hello {}, How are you?".format(user_name))
else:
    print("Please enter a User Name having atleast 3 characters ")           