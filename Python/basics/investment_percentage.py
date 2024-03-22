# Tres  personas  deciden  invertir  su  dinero  para  fundar  una  empresa.  Cada  una  de  ellas  invierte  una  cantidad  
# distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida. 


def investment_percentage():

    # user input
    first_investor = float(input("Enter the amount of money invested (first investor): "))
    second_investor = float(input("Enter the amount of money invested (second investor): "))
    third_investor = float(input("Enter the amount of money invested (third investor): "))

    # calculate the percentage of investment per investor
    total_investment = first_investor + second_investor + third_investor
    print(f"\nThe first investor put {first_investor} ({((first_investor*100)/total_investment):.2f}%) of the company revenue")
    print(f"The second investor put {second_investor} ({(((second_investor*100)/total_investment)):.2f}%) of the company revenue")
    print(f"The third investor put {third_investor} ({(((third_investor*100)/total_investment)):.2f}%) of the company revenue")


if __name__ == "__main__":
    investment_percentage()