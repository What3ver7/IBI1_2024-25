#First define a new function named volume with two variables named weight and strength.
#Store the strength into the strength_dict as key, and also store the value
#Have two variables named weight_auth and strength_auth equal True
#Then judge whether the weight is between 10kg and 100kg
#if not, let weight_auth become False
#Then judge whether the strength is in strength_dict
#if not, let strength_auth become False
#if weight_auth or strength_auth is False
#return None, weight_auth, strength_auth
#if not
#calculate the required_weight and volume 
#For the main part
#First input the weight and strength
#then judge if weight_auth is False
#print Give me a vaild weight, between 10kg and 100kg :(
#judge if strength_auth is False
#print Give me a valid strength :(
#if both of them are True
#print The drug dosage should be volumn ml.

def volume(weight,strength):
    strength_dict={"120mg/5ml":24
                   ,"250mg/5ml":50}
    weight_auth=True
    strength_auth=True
    if not 10<int(weight)<100:
        weight_auth=False
    if strength not in strength_dict:
        strength_auth=False
    if weight_auth==False or strength_auth==False:
        return None, weight_auth, strength_auth
    required_weight=int(weight)*15
    volume=required_weight/strength_dict[strength]
    return volume, weight_auth, strength_auth

weight=input("Give me the weight: ")
strength=input("Give me the strength: ")
x,y,z=volume(weight,strength)
if y==False:
    print("Give me a vaild weight, between 10kg and 100kg :(")
if z==False:
    print("Give me a vaild strength:(") 
if y==True and z==True:
    print(f"The drug dosage should be {x} ml.")


#Success Example
"""
weight=60
strength=120mg/5ml
volume=required_weight/strength_dict[strength]=60*15/24=37.5
print("The drug dosage should be 37.5 ml.")
"""

#Failure Example
"""
Weight=120
strength=130mg/5ml
print Give me a vaild weight, between 10kg and 100kg :(
      Give me a vaild strength :(
"""