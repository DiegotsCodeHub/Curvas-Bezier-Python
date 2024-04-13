import matplotlib.pyplot as plt
import numpy as np
import math

def bezier_curve(control_points_list, num_points=100):
    t = np.linspace(0, 1, num_points)
    n = len(control_points_list[0]) - 1
    curve = np.zeros((num_points, 2))
    for control_points in control_points_list:
        coefficients = np.array([math.comb(n, i) * t ** i * (1 - t) ** (n - i) for i in range(n + 1)])
        segment_curve = np.dot(coefficients.T, control_points)
        curve = np.vstack((curve, segment_curve))
    return curve

# Definir puntos de control para las 10 curvas
control_points_list = [
    np.array([[0, 0], [1, 3], [2, -3], [3, 0]]),
    np.array([[3, 0], [4, 3], [5, -3], [6, 0]]),
    # Agrega aquí los puntos de control para las otras 8 curvas
]

# Generar la curva de Bézier compuesta
curve = bezier_curve(control_points_list)

# Graficar la curva de Bézier compuesta
import matplotlib.pyplot as plt
plt.plot(curve[:, 0], curve[:, 1], label='Curvas de Bézier')
plt.plot(control_points_list[0][:, 0], control_points_list[0][:, 1], 'ro--', label='Puntos de control (1er segmento)')
plt.plot(control_points_list[1][:, 0], control_points_list[1][:, 1], 'bo--', label='Puntos de control (2do segmento)')
# Agrega aquí las líneas para los puntos de control de las otras 8 curvas
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curvas de Bézier')
plt.grid(True)
plt.axis('equal')
plt.show()
