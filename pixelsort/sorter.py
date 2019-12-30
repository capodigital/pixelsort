import random


def sort_image(pixels, intervals, randomness, sorting_function):
    sorted_pixels = []
    for y in range(len(pixels)):
        row = []
        x_min = 0
        for x_max in intervals[y]:
            interval = []
            for x in range(x_min, x_max):
                interval.append(pixels[y][x])
            if random.random() < randomness / 100:
                row += interval
            else:
                row += sort_interval(interval, sorting_function)
            x_min = x_max
        sorted_pixels.append(row)
    return sorted_pixels


def sort_interval(interval, sorting_function):
    return [] if interval == [] else sorted(interval, key=sorting_function)
