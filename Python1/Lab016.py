def num_grid(lst):

    #Code Here

    return lst
lst_input = []

input_list = input().split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")
