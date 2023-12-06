import statistics


def correlation(arr1, arr2):
    return round(statistics.correlation(arr1, arr2), 4)


if __name__ == '__main__':
    orbital_period = [88, 225, 365, 687, 4331, 10756, 30_687, 60190]
    dist_from_sun = [58, 108, 150, 228, 778, 1400, 2900, 4500]

    print(correlation(orbital_period, dist_from_sun))
