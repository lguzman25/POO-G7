
import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === CONFIGURAR TU PUERTO SERIAL ===
ser = serial.Serial('COM6', 9600, timeout=1)  # Cambia COM3 por el tuyo (usa Arduino IDE para ver cuál)

# === CONFIGURACIÓN DEL RADAR ===
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_thetalim(0, np.pi)
ax.set_rmax(40)  # rango máximo de 40 cm

angles = []
distances = []
points, = ax.plot([], [], 'go', markersize=4)

def update(frame):
    global angles, distances

    try:
        line = ser.readline().decode('utf-8').strip()
        if line and "," in line:
            angle_str, dist_str = line.split(',')
            angle = float(angle_str)
            distance = float(dist_str)
            if distance > 0 and distance < 40:
                theta = np.deg2rad(angle)
                angles.append(theta)
                distances.append(distance)
                if len(angles) > 500:
                    angles.pop(0)
                    distances.pop(0)
    except:
        pass

    points.set_data(angles, distances)
    return points,

ani = FuncAnimation(fig, update, interval=50)
plt.title("Radar Arduino - Python (Tiempo Real)")
plt.show()

