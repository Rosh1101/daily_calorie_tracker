import math
import time
print("The tool is designed to help you calculate your daily calorie intake and stay in healthy zone to maintain health and fitness")

array = []
limit = int(input("Enter your daily calorie limit: "))
n = int(input("Number of meals: "))

for i in range(n):
    meal = input("Enter meal name: ")
    while True:
        try:
            cal = int(input("Enter calories number: "))
            if cal < 1:
                print("Calories can never be less than 1. Kindly eneter valid number")
            else:
                break
        except ValueError:
            print("Enter correct data type")
    grouped = (meal,cal)
    array.append(grouped)


def diff_calc(limit,consumed):
    diff = limit-consumed
    if(diff>=0):
        print("consumed in limit!")
    else:
        print(f"Limit exceeded. Added {-(diff)} more than limit of {limit} calories")

def create_file(data):
    time_stamp = time.localtime()
    store_time_stamps = {
        "hour":time_stamp.tm_hour,
        "min":time_stamp.tm_min,
        "sec":time_stamp.tm_sec
    }
    with open("data.txt","w") as f:
        f.write(f"{data}\n{store_time_stamps['hour']}H-{store_time_stamps['min']}M-{store_time_stamps['sec']}S")

        

def info_cal(limit, array, alert,save_file=None):
    cal_per_meal = []
    for i in range(len(array)):
        cal_per_meal.append(array[i][1])
    #dict = {"total":sum(cal_per_meal), "mean": math.floor(sum(cal_per_meal)/len(array)), "diff": limit-sum(cal_per_meal)} 
    
    total = sum(cal_per_meal)
    average = math.floor(total/len(array))

    print("Meal Name\tCalories\n")
    print("-------------------------")

    for i in range(len(array)):
        print(f"{array[i][0]}\t\t{array[i][1]}")
    print(f"Total:\t\t{total}\nAverage:\t{average}")
    
    alert(limit,total)
    ask = input("Do you want to save the record to a file? y/n: ").lower()
    if(ask == 'y'):
        save_file(f"meal:{array}, total:{total}, average: {average}")
    else:
        pass
    
info_cal(limit,array,diff_calc,create_file)

    