import random

def random_arr(member): #random member to arrays
    for i in range(member):
        num = random.randint(1, 100)
        arr.append(num)
    return(arr)

arr = []
random_arr(7)#change number to increase or decrease member arrays
print(arr)
# strt,stp,step = 1,6,1
# run_number = list(range(strt,stp,step))

# print(f"1.find max\n2.find min")
# inp = input("Select to do: ")
# if (type(inp) != int) or (inp not in range(strt,stp,step)):
#     print(f"{inp} is not in command")

