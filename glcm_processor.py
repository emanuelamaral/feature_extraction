import numpy as np
from skimage.feature import graycomatrix, graycoprops


import os


class GLCMProcessor:
    def __init__(self, image):
        self.imagens = image

    def calc_glcm(self):
        for i in range(len(self.imagens)):
            filename, image = self.imagens[i]

            letter = filename[0]

            g = graycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], normed=True, symmetric=True)
            contrast = graycoprops(g, 'contrast')[0, 0]
            dissimilarity = graycoprops(g, 'dissimilarity')[0, 0]
            homogeneity = graycoprops(g, 'homogeneity')[0, 0]
            asm = graycoprops(g, 'ASM')[0, 0]
            energy = graycoprops(g, 'energy')[0, 0]

            print(f"{contrast} {dissimilarity} {homogeneity} {asm} {energy} {letter}")
