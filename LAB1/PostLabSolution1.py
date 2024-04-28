import numpy
from scipy import stats

list = []

print("List Size 9")

for i in range(9):
    
    list.append(int(input('Enter Value List: ')))

print("List: ", list)

x = numpy.mean(list)
y = numpy.median(list)
z = stats.mode(list)

print("Median:", y)
print("Mode:", z)
print("Mean:", x)