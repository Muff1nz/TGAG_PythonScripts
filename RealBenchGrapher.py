import sys
import parse
import matplotlib.pyplot as plt


print("Provided file: " + sys.argv[1])
file = open(sys.argv[1], 'r')
inGraph = False
graphs = []

fpsMax = 0
timeMax = 0

for line in file:
    if line.startswith("["):
        graphs.append([[], []])
        inGraph = True

    elif line.startswith("]"):
        maxFps = max(graphs[len(graphs) - 1][1])
        if maxFps > fpsMax:
            fpsMax = maxFps

        maxTime = max(graphs[len(graphs) - 1][0])
        if maxTime > timeMax:
            timeMax = maxTime

        inGraph = False

    elif inGraph:
        parsed = parse.parse("x:{}|y:{}", line)
        graphs[len(graphs) - 1][0].append(float(parsed[0]))
        graphs[len(graphs) - 1][1].append(float(parsed[1]))

for graph in graphs:
    plt.plot(graph[0], graph[1])


plt.axis([0, timeMax + 5, 0, fpsMax + 10])
plt.ylabel("FPS")
plt.xlabel("TIME")
plt.show()

