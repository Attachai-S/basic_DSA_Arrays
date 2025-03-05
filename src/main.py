import random

def createArr(member): #random member to arrays
    for i in range(member):
        num = random.randint(1, 100)
        arr.append(num)

def minVal(): #find minimum number from list(arrays)
    current_member = arr[0]
    for next_member in arr:
        if next_member < current_member:
            current_member = next_member
    print(f"Minimum number from arrays is : {current_member}")

def maxVal(): #find minimum number from list(arrays)
    current_member = arr[0]
    for next_member in arr:
        if next_member > current_member:
            current_member = next_member
    print(f"Maximum number from arrays is : {current_member}")

arr = []
createArr(7)#change number to increase or decrease member arrays

print(f"{arr}\n"
      f"1.Find minimum number\n"
      f"2.Find maximum number\n"
      f"3.Exit")
while True:
    try:
        user_input = int(input("Enter your choice to action: "))
        if user_input == 1:
            minVal()
        elif user_input == 2:
            maxVal()
        elif user_input == 3:
            print("Thank you!")
            break
        else:
            print("Invalid choice, try again")
    except ValueError:
        print("Invalid input, please enter a choice")