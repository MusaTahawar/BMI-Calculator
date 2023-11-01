#here i am getting the input from the user

user_name = str(input("Enter your name "))
user_height = float(input("Enter your height in meters "))
user_weight = int(input("Enter your weight "))

#here i am going to make a function which will count the bmi 

def bmi_calculator():
    user_height_square = user_height * user_height
    bmi_raw = user_weight / user_height_square
    bmi = round(bmi_raw,1)
    print(bmi)
  
    #here i am going to apply some conditions
  
    if bmi < 18.5:
        print(f"{user_name} is underweight \n")
        print("Being underweight may indicate potential health concerns, \n such as malnutrition or underlying medical conditions. \n It's essential to consult with a healthcare professional if you're underweight in this age range.")
   
    elif bmi <= 18.5 or 24.9 >= bmi:
        print(f"{user_name} is normal \n")
        print("Falling within this range is generally considered healthy for individuals between the ages of 18 and 40. \n However, other factors like muscle mass, \n overall health, and fitness level should also be considered.")
    
    elif bmi <= 25.0 or 29.9 >= bmi:
        print(f"{user_name} is Overweight \n")
        print("Being overweight can increase the risk of various health issues, including heart disease, diabetes,\n and joint problems. Weight management and adopting a healthier \n lifestyle may be recommended if you fall into this category.")
    
    elif bmi <= 30:
        print(f"{user_name} are Obese \n")
        print("Obesity is associated with an increased risk of many chronic health conditions, such as heart disease,\n type 2 diabetes, and certain types of cancer.\n Individuals in this age group with obesity should consider consulting with healthcare professionals for weight management\n strategies and lifestyle changes.")
   
    else:
        print("Sorry there is something wrong")

bmi_calculator()
