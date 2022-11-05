s=int(input("add text"))
a=int(input("add text"))
d=int(input("add text"))
num_list = [s, a, d]
res = sum(num_list)
avg = res / len(num_list)
print("sum is: ", res, "Average is: ", avg)
res1 = 0
for num in num_list:
    res1 += num
avg1 = res1 / len(num_list)
print("sum is: ", res1, "Average is: ", avg1)