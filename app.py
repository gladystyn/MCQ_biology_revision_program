print("Title of program: MCQ biology revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What does the liver produce?")
  print("   a) Salivary amylase")
  print("   b) Pancreatic amylase")
  print("   c) Bile")
  print("   d) Pepsin")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is produced by the mouth."
    score -=1
  elif answer == "b":
    output = "Wrong. This is produced by the pancreas."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. This is produced by the stomach."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which one belongs to the human circulatory system?")
  print("   a) Heart")
  print("   b) Lungs")
  print("   c) Urethra")
  print("   d) Oesophagus")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. This belongs to the respiratory system."
    score -=1
  elif answer == "c":
    output = "Wrong. This belongs to the reproductive system."
    score -=1
    
  elif answer == "d":
    output = "Wrong. This belongs to the digestive system."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is protein made up of?")
  print("   a) 1 glycerol molecule and 3 fatty acids")
  print("   b) fibre")
  print("   c) monosaccharide")
  print("   d) chains of amino acids")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This makes up lipids."
    score -=1
  elif answer == "b":
    output = "Wrong.  This is found in some carbohydrates."
    score -=1
  elif answer == "c":
    output = "Wrong.  This is found in carbohydrates."
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
  
