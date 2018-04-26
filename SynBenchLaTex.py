import sys
import parse
import os

def Convert2LaTeX(filename, directory):
    filename = os.fsdecode(filename)
    file = open("{}\\{}".format(directory, filename))

    inGraph = False
    coordinates = []
    for line in file:
        if line.startswith("["):
            inGraph = True

        elif line.startswith("]"):
            inGraph = False

        elif inGraph:
            parseLine = line.split("|")
            if len(parseLine) == 3:
                time = parse.parse("Time: {} Seconds ", parseLine[0])
                threads = parse.parse(" Threads: {}\n", parseLine[2])
                coordinates.append("({}, {})".format(str(threads[0]), str(time[0])))
            else:
                time = parse.parse("Time: {} Seconds ", parseLine[0])
                threads = parse.parse(" Threads: {}\n", parseLine[1])
                coordinates.append("({}, {})".format(str(threads[0]), str(time[0])))

    outputName = "{}_latex\\{}_LaTeX.tex".format(directory, filename.split(".")[0])
    print(outputName)
    file = open(outputName, 'w')
    file.write("coordinates {\n")
    for coordinate in coordinates:
        file.write(coordinate)
    file.write("\n};")

print("Provided directory: " + sys.argv[1])
directory = sys.argv[1]

for file in os.listdir(os.fsencode(directory)):
    Convert2LaTeX(file, directory)


