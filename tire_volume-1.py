import math
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire in mm (ex 60): "))
diameter = float(input("Enter the diameter of the wheel  in inches (ex 15): "))
pi = math.pi
volume = (pi * width**2 * aspect_ratio * ((width * aspect_ratio) + (2540*diameter)))/(10000000000)
print(f'The approximate volume is {volume:.2f} liters')
user_choices = input("Would you like to buy the tire with the dimensions you've entered?(Answer'yes' or 'no') ")
if user_choices == "yes" :
    phone_number = input("Enter your phone number:")
    print("Thanks for inputing your desired Dimension and Phone number")
    
elif user_choices == "no" :
    print("Thanks for inputing your desired Dimension")
    phone_number = "N/A"

else :
    print("Thanks for inputing your desired Dimension")
    phone_number = "N/A"


from datetime import datetime
current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:
    print(f'{current_date_and_time:%Y-%m-%d},{width:.0f},{aspect_ratio:.0f},{diameter:.0f},{volume:.2f},{phone_number}', file=volumes_file )

