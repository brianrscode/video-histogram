"""
Author: brianrscode (github.com/brianrscode)
Created: 08/07/2024
"""


import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


class VideoHistogram:
    def __init__(self, opt):
        if os.path.exists(opt):
            self.cap = cv2.VideoCapture(opt)
        else:
            self.cap = cv2.VideoCapture(0)

        self. fig, self. ax = plt.subplots()
        self.ax.set_xlabel("Cantidad de píxeles")
        self.ax.set_ylabel("Valor de intensidad")
        self.ax.set_xlim(0, 256)
        self.ax.set_ylim(0, 10000)

    def gray_histogram(self):
        self.ax.set_title("Histogram (grayscale)")
        linea, = self.ax.plot(np.arange(256), np.zeros((256,1)), c='k', label='intensity')
        plt.ion()
        plt.show()
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Calcular histograma.
            histograma = cv2.calcHist([gray], [0], None, [256], [0, 256])
            # Normalizar histograma.
            # histograma = np.divide(histograma, np.sum(histograma))

            # Actualizar la línea del plot con los valores del histograma
            linea.set_ydata(histograma)
            # Cambiar el valor máximo del eje y
            # ax.set_ylim(0, histograma.max())

            # Redibujar la linea.
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            # Mostrar el frame de la cámara en una ventana
            cv2.imshow("grayscale", gray)

            if cv2.waitKey(24) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def rgb_histogram(self):
        self.ax.set_title("Histogram (RGB)")
        linea_b, = self.ax.plot(np.arange(256), np.zeros((256,1)), c='b', label='Blue')
        linea_g, = self.ax.plot(np.arange(256), np.zeros((256,1)), c='g', label='Green')
        linea_r, = self.ax.plot(np.arange(256), np.zeros((256,1)), c='r', label='Red')
        plt.ion()
        plt.show()
        while self.cap.isOpened():
            ret, frame = self.cap.read()
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

            # Cambiar el valor máximo del eje y
            # ax.set_ylim(0, max(histogram_b.max(), histogram_g.max(), histogram_r.max()))

            # Redibujar las lineas.
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            if cv2.waitKey(24) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


hist = VideoHistogram(1)
# hist.gray_histogram()
hist.rgb_histogram()