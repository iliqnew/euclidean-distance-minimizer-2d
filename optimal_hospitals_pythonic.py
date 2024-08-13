import math
import random
from itertools import combinations


def __get_cities_randomized(n: int, grid_w: int, grid_h: int) -> list[tuple[int, int]]:
    cities = []
    while len(cities) < n:
        x = random.randint(0, grid_w - 1)
        y = random.randint(0, grid_h - 1)
        if (x, y) not in cities:
            cities.append((x, y))
    return cities


def __get_distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def place_hospitals(
    city_coordinates: list[tuple[int, int]]
) -> list[tuple[int, int, int]]:
    return list(
        sorted(
            combinations(city_coordinates, 2),
            key=lambda points: sum(
                min(__get_distance(points[0], city), __get_distance(points[1], city))
                for city in city_coordinates
            ),
        )[0]
    )


def __plot(
    city_coordinates: list[tuple[int, int]],
    hospital_coordinates: list[tuple[int, int, int]],
):
    import matplotlib.pyplot as plt
    import numpy as np

    cities_xpoints = np.array([city[0] for city in city_coordinates])
    cities_ypoints = np.array([city[1] for city in city_coordinates])
    hospitals_xpoints = np.array([hospital[0] for hospital in hospital_coordinates])
    hospitals_ypoints = np.array([hospital[1] for hospital in hospital_coordinates])

    plt.grid(visible=True)
    plt.gca().set_aspect("equal")
    plt.plot(cities_xpoints, cities_ypoints, "o", color="green")
    plt.plot(hospitals_xpoints, hospitals_ypoints, "+", color="red", markersize=10)
    plt.show()


if __name__ == "__main__":
    # # test_result_1_c10_h2_W10_H10.png
    # city_coordinates = [(x, 0) for x in range(10)]
    # print(f"cities: {city_coordinates}")
    # hospital_coordinates = place_hospitals(city_coordinates)
    # print(f"hospitals: {hospital_coordinates}")
    # __plot(city_coordinates, hospital_coordinates)

    # # test_result_2_c10_h2_W10_H10.png
    # city_coordinates = [(0, y) for y in range(10)]
    # print(f"cities: {city_coordinates}")
    # hospital_coordinates = place_hospitals(city_coordinates)
    # print(f"hospitals: {hospital_coordinates}")
    # __plot(city_coordinates, hospital_coordinates)

    # # test_result_3_c10_h2_W10_H10.png
    # city_coordinates = [(x, x) for x in range(10)]
    # print(f"cities: {city_coordinates}")
    # hospital_coordinates = place_hospitals(city_coordinates)
    # print(f"hospitals: {hospital_coordinates}")
    # __plot(city_coordinates, hospital_coordinates)

    # # test_result_4_c10_h2_W10_H10.png
    # city_coordinates = [(x, 9 - x) for x in range(10)]
    # print(f"cities: {city_coordinates}")
    # hospital_coordinates = place_hospitals(city_coordinates)
    # print(f"hospitals: {hospital_coordinates}")
    # __plot(city_coordinates, hospital_coordinates)

    # # test_result_5_c10_h2_W1000_H1000.png
    # city_coordinates = [(x, y) for x in range(10) for y in range(10)]
    # print(f"cities: {city_coordinates}")
    # hospital_coordinates = place_hospitals(city_coordinates)
    # print(f"hospitals: {hospital_coordinates}")
    # __plot(city_coordinates, hospital_coordinates)

    # # result_1_c10_h2_W1000_H1000.png
    # city_coordinates = [
    #     # square 1
    #     (200, 200),
    #     (400, 400),
    #     (200, 400),
    #     (400, 200),
    #     # center of square 1
    #     (300, 300),
    #     # square 2
    #     (700, 700),
    #     (900, 900),
    #     (700, 900),
    #     (900, 700),
    #     # center of square 2
    #     (800, 800),
    # ]
    # print(f"cities: {city_coordinates}")
    # hospital_coordinates = place_hospitals(city_coordinates)
    # print(f"hospitals: {hospital_coordinates}")
    # __plot(city_coordinates, hospital_coordinates)

    # # result_2_c10_h2_W1000_H1000.png
    # city_coordinates = [
    #     # sides
    #     (200, 200),
    #     (200, 400),
    #     (800, 200),
    #     (800, 400),
    #     # centers
    #     (350, 300),
    #     (650, 300),
    # ]
    # print(f"cities: {city_coordinates}")
    # hospital_coordinates = place_hospitals(city_coordinates)
    # print(f"hospitals: {hospital_coordinates}")
    # __plot(city_coordinates, hospital_coordinates)

    # result_3_c10_h2_W1000_H1000.png
    city_coordinates = [
        # randomized
        (902, 307),
        (328, 582),
        (891, 407),
        (708, 873),
        (703, 699),
        (657, 557),
        (322, 746),
        (859, 697),
        (572, 142),
        (197, 484),
    ]
    print(f"cities: {city_coordinates}")
    hospital_coordinates = place_hospitals(city_coordinates)
    print(f"hospitals: {hospital_coordinates}")
    __plot(city_coordinates, hospital_coordinates)
