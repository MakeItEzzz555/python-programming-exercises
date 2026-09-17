def apr_formula(future, annual_interest, years):
    p = int(future/((1+annual_interest)**years))
    return p
def main():
    future = float(input("Enter your future value: "))
    annual_interest = float(input("Enter the annual interest value: "))
    years = int(input("Enter the number of years the money will grow: "))
    apr_formula(future, annual_interest, years)

    print("You will need to deposit this amount :"+str(apr_formula(future, annual_interest, years)))

main()