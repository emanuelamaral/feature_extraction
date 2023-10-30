import numpy as np
from skimage.feature import graycomatrix, graycoprops


import os


class GLCMProcessor:
    def __init__(self, image):
        self.imagens = image
        self.caminho_do_arquivo = "resultado.txt"

    def calc_glcm(self):
        result = []
        print("Gerando resultados...")
        for i in range(len(self.imagens)):
            filename, image = self.imagens[i]

            letter = filename[0]

            letter_index = ord(letter) - ord('A')

            g = graycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], normed=True, symmetric=True)
            contrast = graycoprops(g, 'contrast')[0, 0]
            dissimilarity = graycoprops(g, 'dissimilarity')[0, 0]
            homogeneity = graycoprops(g, 'homogeneity')[0, 0]
            asm = graycoprops(g, 'ASM')[0, 0]
            energy = graycoprops(g, 'energy')[0, 0]

            result.append(f"{contrast} {dissimilarity} {homogeneity} {asm} {energy} {letter_index}")
        print("Finalizado!")

        with open(self.caminho_do_arquivo, 'w') as arquivo:
            for line in result:
                arquivo.write(line + '\n')

        arquivo.close()

        print(f"Arquivo '{self.caminho_do_arquivo}' criado e conteúdo salvo com sucesso.")