import math
import random
from polar import Polar
from cartesian2d import Cartesian2D

def test_polar_to_cartesian_and_back(num_points=5):
    # Генерація випадкових полярних координат
    polar_points = [
        Polar(random.uniform(1, 100), random.uniform(0, 2 * math.pi)) for _ in range(num_points)
    ]
    
    for polar_point in polar_points:
        print(f"Полярні координати: r = {polar_point.r:.2f}, theta = {polar_point.theta:.2f}")
        
        # Перетворення в декартові координати
        cartesian_point = Cartesian2D.from_polar(polar_point.r, polar_point.theta)
        print(f"Декартові координати: x = {cartesian_point.x:.2f}, y = {cartesian_point.y:.2f}")
        
        # Зворотне перетворення в полярні координати
        polar_from_cartesian = Polar.from_cartesian(cartesian_point.x, cartesian_point.y)
        print(f"Зворотні полярні координати: r = {polar_from_cartesian.r:.2f}, theta = {polar_from_cartesian.theta:.2f}")
        
        # Перевірка коректності
        assert math.isclose(polar_point.r, polar_from_cartesian.r, rel_tol=1e-9), "Помилка: Радіуси не рівні"
        assert math.isclose(polar_point.theta, polar_from_cartesian.theta, rel_tol=1e-9), "Помилка: Кути не рівні"
        
        print("Тест виконан: Полярні координати співпадають після зворотнього обернення")
        print("-" * 50)

if __name__ == "__main__":
    test_polar_to_cartesian_and_back()
