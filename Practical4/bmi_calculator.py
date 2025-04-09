# BEGIN
#    PRINT "Enter your weight (kg) and height (m), separated by a comma: "
#    READ input
#    SPLIT input by "," into weight and height

#    SET bmi TO FLOAT(weight) / (FLOAT(height) * FLOAT(height))

#    IF bmi > 30 THEN
#        PRINT "Obese"
#    ELSE IF bmi < 18.5 THEN
#        PRINT "Underweight"
#    ELSE
#        PRINT "Normal weight"

x=input("Please, give me your weight(kg) and height(m),please separate them use comma: ").split(",")
weight=float(x[0])
height=float(x[1])
bmi=weight/height**2  #SET bmi TO FLOAT(weight)/(FLOAT(height)*FLOAT(height))
if bmi>30:
    print(f"Your BMI is {bmi}, your are obese,sorry :(")
elif bmi<18.5:
    print(f"Your BMI is {bmi},you are underweight,sorry :(")
else:
    print(f"Your BMI is {bmi},You are normal weight :)")