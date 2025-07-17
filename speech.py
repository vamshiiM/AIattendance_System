import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([0,8])
ypoint=np.array([0,16])
x=np.array([20,50,67])


plt.plot(xpoint,ypoint)
plt.show()
plt.pie(x)
plt.show()

int=input("ENTER THE NUMBER:")
def arms(num):
    string=str(num)
    num_len=len(string)
    total=0

    for digit in string:
        total += int(digit) ** num_len
    return total == num

arms(int)





