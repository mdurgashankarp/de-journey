def main():
    total_salary = salary_calculator(input("What is annual salary? "), input("What is the bonus % you have received this year? "))
    print(f"Total Comp is: ${float(total_salary):,.2f}")

def salary_calculator(annual_salary, bonus_percentage):
    total_bonus = float(float(annual_salary) * (float(bonus_percentage.replace('%',''))/100))
    total_compensation = float(annual_salary) + float(total_bonus)
    return str(total_compensation)

main()
 