score = int(input("Provide the score: "))

if score >= 80:
    print("Your grade is A")
elif 80 > score >= 60:
    print("Your grade is B")
elif 60 > score >= 40:
    print("Your grade is C")
elif 40 > score >= 20:
    print("Your grade is D")
elif 20 > score >= 0:
    print("Your grade is E")
else:
    print("Invalid score!")
