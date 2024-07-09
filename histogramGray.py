import cv2
from matplotlib import pyplot as plt
import numpy as np


# Inicial la figura y el subplot.
fig, ax = plt.subplots()
ax.set_title("Histogram (grayscale)")
ax.set_xlabel("Cantidad de píxeles")
ax.set_ylabel("Valor de intensidad")
ax.set_xlim(0, 256)
ax.set_ylim(0, 10000)

# Dibujar la linea inicial.
linea, = ax.plot(np.arange(256), np.zeros((256,1)), c='k', label='intensity')
# linea, = ax.plot([128, 128], [0, 1], c='k', label='intensity')

# Mostrar figura.
plt.ion()
plt.show()

cap = cv2.VideoCapture("prueba_azul.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calcular histograma.
    histograma = cv2.calcHist([gray], [0], None, [256], [0, 256])
    # Normalizar histograma.
    # histograma = np.divide(histograma, np.sum(histograma))

    # Actualizar la línea del plot con los valores del histograma
    linea.set_ydata(histograma)
    # ax.set_ylim(0, histograma.max())

    # Redibujar la linea.
    fig.canvas.draw()
    fig.canvas.flush_events()

    # Mostrar el frame de la cámara en una ventana
    cv2.imshow("grayscale", gray)

    if cv2.waitKey(24) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()