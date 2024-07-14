print("body weight index finder")
height=float(input("height(in meters): "))
kilo=float(input("Kilo: "))
bwi=kilo/(height**2)
if (bwi < 18.5):
     print("underweight")
elif (bwi < 25):
     print("normal")
elif (bwi < 30):
     print("overweight")
else:
     print("obese")
print("""Height: {}
Kilo: {} 
Body Weight Index: {:.2f}
      """.format(height,kilo,bwi))