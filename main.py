import matplotlib.pyplot as plt

year = []
temp = []
number = []

with open("data.txt") as file:
    for line in file:
        elem = line.split('\t')
        year.append(int(elem[0]))
        temp.append(float(elem[1]))
        number.append(int(elem[2]))

average = []
width = 5
for i in range(0, len(year)):
    sum = 0
    total = 0
    for j in range(i-width, i+width):
        if j >= 0 and j < len(year):
            sum += temp[j] * number[j]
            total += number[j]
    average.append(sum/total)

plt.plot(year, temp)
plt.plot(year, average)
plt.show()

