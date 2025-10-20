import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === CONFIGURAR TU PUERTO SERIAL ===
ser = serial.Serial('COM6', 9600, timeout=1)  # asegurate de usar el mismo puerto que en Arduino

# === CONFIGURACIÓN DEL RADAR ===
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_thetalim(0, np.pi)
ax.set_rmax(40)

angles = []
distances = []

points, = ax.plot([], [], 'go', markersize=4)

# --- Parámetros para suavizar detección ---
SMOOTH_WINDOW = 5      # cuántas lecturas promediar
MIN_DISTANCE_DIFF = 3   # diferencia mínima (en cm) para considerar que es otro objeto

def suavizar(valores, n=SMOOTH_WINDOW):
    if len(valores) < n:
        return valores
    arr = np.convolve(valores, np.ones(n)/n, mode='valid')
    # completamos para que mantenga longitud
    return np.concatenate([valores[:n-1], arr])

def update(frame):
    global angles, distances

    try:
        line = ser.readline().decode('utf-8').strip()
        if line and "," in line:
            angle_str, dist_str = line.split(',')
            angle = float(angle_str)
            distance = float(dist_str)

            # descartamos valores fuera de rango
            if 0 < distance < 40:
                theta = np.deg2rad(angle)
                angles.append(theta)
                distances.append(distance)

                # mantenemos la lista con un máximo de 500 puntos
                if len(angles) > 500:
                    angles.pop(0)
                    distances.pop(0)

    except:
        pass

    # --- aplicar suavizado ---
    if len(distances) > SMOOTH_WINDOW:
        smooth_dist = suavizar(distances)
    else:
        smooth_dist = distances

    # --- Filtrar puntos redundantes ---
    filtered_angles = []
    filtered_distances = []

    for i in range(len(smooth_dist)):
        if i == 0 or abs(smooth_dist[i] - smooth_dist[i-1]) > MIN_DISTANCE_DIFF:
            filtered_angles.append(angles[i])
            filtered_distances.append(smooth_dist[i])

    points.set_data(filtered_angles, filtered_distances)
    return points,

ani = FuncAnimation(fig, update, interval=60)
plt.title("Radar Arduino - Python (con suavizado de detección)")
plt.show()