import sys
import parse
import matplotlib.pyplot as plt


print("Provided file: " + sys.argv[1])
file = open(sys.argv[1], 'r')
inGraph = False
graphs = []
labels = []
plots = []

fpsMax = 0
timeMax = 0

for line in file:
    if line.startswith("label:"):
        labels.append(parse.parse("label: {}", line)[0])

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
        if float(parsed[0]) >= 60:
            graphs[len(graphs) - 1][0].append(float(parsed[0]))
            graphs[len(graphs) - 1][1].append(float(parsed[1]))

i = 0
for graph in graphs:
    if len(labels) > 0:
        plots.append(plt.plot(graph[0], graph[1], label=labels[i]))
    else:
        plots.append(plt.plot(graph[0], graph[1]))
    i += 1

if len(labels) > 0:
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)


plt.axis([55, timeMax + 5, 0, fpsMax + 10])
plt.ylabel("FPS")
plt.xlabel("TIME")
plt.show()

