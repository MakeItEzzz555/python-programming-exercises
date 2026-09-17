def calc_avg(t1, t2, t3):
    sum = t1 + t2 + t3
    return sum / 3

def main():
    test1 = float(input("Enter your test score: "))
    test2 = float(input("Enter your test score: "))
    test3 = float(input("Enter your test score: "))
    print("The average score is "+str(calc_avg(test1, test2, test3)))
main()