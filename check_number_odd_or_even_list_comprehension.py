new_list=[]
[new_list.append("Even") if i%2==0 else new_list.append("Odd") for i in range(5)]
print(new_list)
