import random

def random_arr(round): #random member to arrays
    arr = []
    for i in range(round):
        num = random.randint(1, 100)
        arr.append(num)
    print(arr)

random_arr(5)#change number to increase or decrease member arrays

# strt,stp,step = 1,6,1
# run_number = list(range(strt,stp,step))

# print(f"1.find max\n2.find min")
# inp = input("Select to do: ")
# if (type(inp) != int) or (inp not in range(strt,stp,step)):
#     print(f"{inp} is not in command")

