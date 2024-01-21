# BMI = w / (h** 2)
def bmi_cal():
    w = float(input('Input your weight: '))
    h = float(input('input your height: '))
    print(w / (h ** 2))



def tip_cal():
    print('Welcomed to the tip calculator')
    total_amount = input('What was the total bill? ')
    tip_per = input('What percentage would you like to give? ')
    split_between = input('How many people to split the bill? ')
    tip = float(tip_per)
    print(f"Each peron should pay ${tip}")


if __name__ == '__main__':
    bmi_cal()