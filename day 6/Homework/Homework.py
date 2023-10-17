total = 0
total_nums = 0
for i in range(5):
    num = int(input("Enter Your Grade: "))
    total += num
    total_nums += 1


print(total // total_nums)
Average_arithmetic = total // total_nums
if Average_arithmetic > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif Average_arithmetic < 5:
    print("გილოცავ გაექეცი მატრიცას")
elif Average_arithmetic > 5 and Average_arithmetic < 10:
    print("You are MID")
elif Average_arithmetic > 10 or Average_arithmetic < 0:
    print("there is something wrong with you")




salary = int(input("Enter your salary: "))

if salary > 10000:
    print("გო ა ში სწავლ ობდ ი?")
elif salary > 1000 and salary < 10000:
    print("you mid")
else:
    print("შემოსუ ლ იყავი გო აში, მატ რიცელ ო.")




compositions = [
    "Simphony 5",
    "Simphony 3",
    "Simphony 7"
]

for i in compositions:
    print(compositions)