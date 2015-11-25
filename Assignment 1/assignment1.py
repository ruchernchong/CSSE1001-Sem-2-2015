import csv
import math

def load_data(filename):
    file = open(filename)
    reader = csv.reader(file)
    heights = []

    for animal in reader:
        name = animal.pop(0)
        animalArray = []

        for height in animal:
            animalArray.append(float(height))

            tup = (name, animalArray)
            heights.append(tup)

        print heights
        return heights

load_data("animal_heights.csv")