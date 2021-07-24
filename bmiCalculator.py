weight = float(input("Enter your weight. "))
height = float(input("Enter your height. "))
bmi = weight/(height*height)

print(bmi)
if bmi<18.5 :
    print("they are underweight")
elif bmi>=18.5 and bmi<25 :
    print("they have a normal weight")  
elif bmi>=25 and bmi<30 :
    print("they are overweight")
elif bmi>=30 and bmi<35 :
    print("they are obese")
else : 
    print("they are clinically obese")      