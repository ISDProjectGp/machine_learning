import matplotlib.pyplot as plt
import numpy as np


def y(e, s):
    return e[0] * s[0] / -e[1]


def drawLine(j, k):
    plt.plot(j[:, 0], [y(k, j[0, :]), y(k, j[1, :])])


def hypothesis(o, u):
    return o[0] * u[0] + o[1] * u[1]


initial_x = np.array([[-20.0, -20.0], [20.0, 20.0]])
initial_w = np.array([1.0, 1.0])

good = np.array([[6, -10.0], [15.0, -15]])
good_result = np.array([1, 1])
bad = np.array([[14.0, 3.0], [11.0, 9.0]])
bad_result = np.array([-1, -1])
thresold = 3

w = np.array([initial_w[0], initial_w[1]])

plt.plot(good[:, 0], good[:, 1], 'ro')
plt.plot(bad[:, 0], bad[:, 1], 'bo')

axes = plt.gca()
axes.set_xlim([-20, 20])
axes.set_ylim([-20, 20])
print(w);
for x in range(0, 20):
    outFlag = True
    for r in range(0, 2):
        if hypothesis(w, good[r, :]) * good_result[r] > 0 :
            continue
        w[0] = w[0] + good_result[r] * good[r, 0]
        w[1] = w[1] + good_result[r] * good[r, 1]
    for d in range(0, 2):
        if hypothesis(w, bad[d, :]) * bad_result[d] > 0 :
            continue
        w[0] = w[0] + bad_result[d] * bad[d, 0]
        w[1] = w[1] + bad_result[d] * bad[d, 1]
    for z in range(0, 2):
        if hypothesis(w, bad[z, :]) * bad_result[z] < 0:
            outFlag = False
    for t in range(0, 2):
        if hypothesis(w, good[t, :]) * good_result[t] < 0:
            outFlag = False
    print(w);
    if outFlag:
        break

drawLine(initial_x, w)




plt.ylabel('some numbers')
plt.show()
