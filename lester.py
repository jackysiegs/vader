Darth = 0
Lea = 0
Luke = 0
with open('jackrabbit.txt', 'r') as jackrabbit:
	      all_text = jackrabbit.read()
	      real_text = str(all_text)
	      data = real_text.split(",")
	      for x in data:
                  if x == "Darth":
                      Darth += 1
                  if x == "Lea":
                      Lea += 1
                  if x == "Luke":
                      Luke += 1
Darth2 = str(Darth)
Lea2 = str(Lea)
Luke2 = str(Luke)                      
print("Darth appears " + Darth2 + " time(s)")
print("Lea appears " + Lea2 + " time(s)")
print("Luke appears " + Luke2 + " time(s)")
                  
	
