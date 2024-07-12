import cv2
from matplotlib import pyplot as plt
import numpy as np


# Inicial la figura y el subplot.
fig, ax = plt.subplots()
ax.set_title("Histogram (RGB)")
ax.set_xlabel("Valor de intensidad")
ax.set_ylabel("Cantidad de píxeles")
ax.set_xlim(0, 256)  # Eje x de 0 a 256
ax.set_ylim(0, 10_000)  # Eje y de 0 a 40000
ax.grid(True)  # Habilitar la cuadrícula

# Dibujar las lineas iniciales.
linea_b, = ax.plot(np.arange(256), np.zeros(256), c='b', label='Blue')
linea_g, = ax.plot(np.arange(256), np.zeros(256), c='g', label='Green')
linea_r, = ax.plot(np.arange(256), np.zeros(256), c='r', label='Red')

# Mostrar figuras.
plt.ion()  # Activa la interacción con la ventana.
plt.show()  # Muestra la ventana.

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Mostrar el video en una ventana
    cv2.imshow("RGB", frame)
    # Calcular histograma.
    b, g, r = cv2.split(frame)
    histogram_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    histogram_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    histogram_r = cv2.calcHist([r], [0], None, [256], [0, 256])

    # Normalizar histograma.
    # histogram_b = np.divide(histogram_b, np.sum(histogram_b))
    # histogram_g = np.divide(histogram_g, np.sum(histogram_g))
    # histogram_r = np.divide(histogram_r, np.sum(histogram_r))

    # Actualizar las líneas del plot con los valores del histograma
    linea_b.set_ydata(histogram_b)
    linea_g.set_ydata(histogram_g)
    linea_r.set_ydata(histogram_r)

    # ax.set_ylim(0, max(histogram_b.max(), histogram_g.max(), histogram_r.max()))

    # Redibujar las lineas.
    fig.canvas.draw()
    fig.canvas.flush_events()

    if cv2.waitKey(24) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()