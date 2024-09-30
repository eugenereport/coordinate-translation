import matplotlib.pyplot as plt
import time
from cartesian2d import Cartesian2D
from polar import Polar
from spherical import Spherical
from cartesian3d import Cartesian3D
import random

# Генерація масиву пар точок для кожної системи координат
def generate_cartesian_point_pairs(count):
    return [(Cartesian2D(random.uniform(0, 100), random.uniform(0, 100)), 
             Cartesian2D(random.uniform(0, 100), random.uniform(0, 100))) for _ in range(count)]

def generate_cartesian3d_point_pairs(count):
    return [(Cartesian3D(random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)),
             Cartesian3D(random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100))) for _ in range(count)]

def generate_polar_point_pairs(count):
    return [(Polar(random.uniform(0, 100), random.uniform(0, 2 * 3.1415)),
             Polar(random.uniform(0, 100), random.uniform(0, 2 * 3.1415))) for _ in range(count)]

def generate_spherical_point_pairs(count):
    return [(Spherical(random.uniform(0, 100), random.uniform(0, 2 * 3.1415), random.uniform(0, 3.1415)),
             Spherical(random.uniform(0, 100), random.uniform(0, 2 * 3.1415), random.uniform(0, 3.1415))) for _ in range(count)]

# Функція для вимірювання часу виконання
def benchmark(func, point_pairs):
    start_time = time.time() * 1000
    func(point_pairs)
    return time.time() * 1000 - start_time 

# Приклад функцій, які розраховують відстані між парами точок
def calculate_distances_cartesian(point_pairs):
    for point1, point2 in point_pairs:
        point1.distance(point2)

def calculate_distances_cartesian3d(point_pairs):
    for point1, point2 in point_pairs:
        point1.distance(point2)

def calculate_distances_polar(point_pairs):
    for point1, point2 in point_pairs:
        point1.distance(point2)

def calculate_distances_spherical_volume(point_pairs):
    for point1, point2 in point_pairs:
        point1.distance_through_volume(point2)

def calculate_distances_spherical_surface(point_pairs):
    for point1, point2 in point_pairs:
        point1.distance_on_surface(point2)

# Генерація масиву розмірів пар точок
start_size = 10000
end_size = 500000
step = 25000
point_sizes = list(range(start_size, end_size + 1, step)) 

cartesian_times = []
cartesian3d_times = []
polar_times = []
spherical_volume_times = []
spherical_surface_times = []

for size in point_sizes:
    cartesian_pairs = generate_cartesian_point_pairs(size)
    cartesian3d_pairs = generate_cartesian3d_point_pairs(size)
    polar_pairs = generate_polar_point_pairs(size)
    spherical_pairs = generate_spherical_point_pairs(size)

    # Вимірювання часу виконання для кожної системи координат
    cartesian_time = benchmark(calculate_distances_cartesian, cartesian_pairs)
    cartesian3d_time = benchmark(calculate_distances_cartesian3d, cartesian3d_pairs)
    polar_time = benchmark(calculate_distances_polar, polar_pairs)
    spherical_volume_time = benchmark(calculate_distances_spherical_volume, spherical_pairs)
    spherical_surface_time = benchmark(calculate_distances_spherical_surface, spherical_pairs)

    cartesian_times.append(cartesian_time)
    cartesian3d_times.append(cartesian3d_time)
    polar_times.append(polar_time)
    spherical_volume_times.append(spherical_volume_time)
    spherical_surface_times.append(spherical_surface_time)

# Побудова графіків
plt.plot(point_sizes, cartesian_times, label='Cartesian 2D', marker='o')
plt.plot(point_sizes, cartesian3d_times, label='Cartesian 3D', marker='o')
plt.plot(point_sizes, polar_times, label='Polar', marker='o')
plt.plot(point_sizes, spherical_volume_times, label='Spherical by Volume distance', marker='o')
plt.plot(point_sizes, spherical_surface_times, label='Spherical by Surface distance', marker='o')

plt.title('Measurement of Distance Calculations')
plt.xlabel('Array Size (number of point pairs)')
plt.ylabel('Execution Time (milliseconds)')
plt.legend()

# Зміна назви вікна
plt.get_current_fig_manager().set_window_title('Graphic Results')

plt.show()
