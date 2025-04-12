
name= str(input("write your name here:"))
age= int(input("Enter your age:"))
city=str(input("Enter your city Name:"))
#marks insert method:using input method:
chem=int(input("Enter chem marks:"))
math=int(input("Enter math marks:"))
phy=int(input("Enter phy marks:"))
bio=int(input("Enter bio marks:"))
urdu=int(input("Enter urdu marks:"))
#tuple for subjects store
subjects=("chem","phy","math","bio","urdu")
#set for store cities
Big_cities=["islamabad","Karachi","Lahore"]
result={}
if chem >= 40:
   result["chem"]= "pass"
else:
   result["chem"]="Fail"
if phy >=40:
    result["phy"]="Pass"
else:
    result["phy"]="Fail"
if math >=40:
    result["math"]="Pass"
else:
    result["math"]="Fail"
if bio >= 40:
    result["bio"]="Pass"
else:
    result["bio"]="Fail"
if urdu >=40:
   result["urdu"]="Pass"
else:
   result["urdu"]="Fail"
#output
print("\n------Student Rcord--------")
print("Name:",name)
print("Age:",age)
print("city:",city)
# cities checking
if city in Big_cities:
  print("City category: Big city")
else:
   print("Small city")
print("\n---------subject Result-----------")
print("chem:",result["chem"])
print("phy:",result["phy"])
print("math:",result["math"])
print("bio:",result["bio"])
print("urdu:",result["urdu"])

