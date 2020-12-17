import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,999, 1000)
# array = np.random.choice([0,1], 1000)
array = np.zeros(1000)
array[10:50] = 1
array[34:40]= 0
array[500:700] = 1
plt.plot(x, array)
plt.show()
CLUSTER = False
Clusters = []
k = 10

# for i in range(len(array)):
#     if array[i] and not CLUSTER:
#         start = i
#         CLUSTER = True
#         print(start)
#         if i - k > 0:
#             print("Got into IF")
#             kDist = not np.any(array[int(i-k):int(i)])
#         else:
#             kDist = not np.any(array[0:int(i)])
#         if kDist == True:
#             Clusters.append((start, i))
#             print(CLUSTER)
#             CLUSTER = False
#             print(CLUSTER)
#     print(CLUSTER)
# print(Clusters)

for i in range(len(array)):
    if not CLUSTER:
        if array[i] == 1:
            start = i
            CLUSTER = True
        elif array[i] == 0:
            pass
    elif CLUSTER:
        if array[i] == 1:
            pass
        elif array[i] == 0:
            kDist = not np.any(array[int(i - k):int(i)])
            if kDist:
                Clusters.append((start, i-10))
                CLUSTER = False
            else:
                pass
    else:
        pass
print(Clusters)