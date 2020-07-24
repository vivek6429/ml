import numpy as np

x = np.array([56, 78, 23, 21])

ip = int(input("enter the element :"))
op = 0
while (ip != 0):
    op = op + ip % 10
    ip = ip // 10
print("sum=", op)
