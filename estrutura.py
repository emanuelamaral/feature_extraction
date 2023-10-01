import cv2
import numpy as np


class Estruturas:
    def __init__(self, img):
        self.img = img
        _, self.img_binary = None, None

    def tratar_imagens(self):
        print("\n==========================================CONTORNOS===============================================")
        for nome_imagem, imagem in self.img:
            _, self.img_binary = cv2.threshold(imagem, 0, 150, cv2.THRESH_BINARY_INV)
            self.calcula_contornos(imagem, nome_imagem)

        print("\n==========================================SKELETONS===============================================")
        for nome_imagem, imagem in self.img:
            _, self.img_binary = cv2.threshold(imagem, 0, 150, cv2.THRESH_BINARY_INV)
            self.calcula_skeleton(imagem, nome_imagem)

    @staticmethod
    def calcular_direcao_contorno(p1, p2):
        # Calcula a direção entre dois pontos p1 e p2
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        return np.arctan2(dy, dx)

    def calcula_contornos(self, imagem, nome_imagem):
        contours, _ = cv2.findContours(self.img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours)

        vetor_caracteristicas = np.zeros(8)

        for contorno in contours:
            print("\n================================================================================================")
            area_contorno = cv2.contourArea(contorno)
            print(f"Área da imagem {nome_imagem}: ", area_contorno)

            # Calcule o momento do contorno
            momento_contorno = cv2.moments(contorno)

            # Calcule o ponto médio (centroide) do contorno
            if momento_contorno['m00'] != 0:
                ponto_central_x = int(momento_contorno['m10'] / momento_contorno['m00'])
                ponto_central_y = int(momento_contorno['m01'] / momento_contorno['m00'])
                ponto_central = (ponto_central_x, ponto_central_y)
                print(f"Ponto central (centroide) da imagem: {nome_imagem}", ponto_central)

            for i in range(len(contorno)):
                # Obtenha dois pontos consecutivos no contorno
                ponto_atual = contorno[i][0]
                ponto_proximo = contorno[(i + 1) % len(contorno)][0]

                # Calcule a direção entre os dois pontos
                direcao = self.calcular_direcao_contorno(ponto_atual, ponto_proximo)

                # Converta a direção para um índice no vetor de características
                indice_caracteristica = int((direcao + np.pi) / (np.pi / 4)) % 8

                # Atualize o vetor de características
                vetor_caracteristicas[indice_caracteristica] += 1

        vetor_caracteristicas /= np.sum(vetor_caracteristicas)
        print(f"Vetor de características da imagem {nome_imagem}:", vetor_caracteristicas)
        img_contours = cv2.cvtColor(imagem, cv2.COLOR_GRAY2BGR)

        cv2.drawContours(img_contours, contours, -1, (255, 0, 0), 1)
        return img_contours

    def calcula_skeleton(self, imagem, nome_imagem):
        skel = np.zeros(imagem.shape, dtype=np.uint8)
        # temp = np.zeros(self.img.shape, dtype=np.uint8)
        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        done = False

        while not done:
            temp = cv2.morphologyEx(self.img_binary, cv2.MORPH_OPEN, element)
            temp = cv2.bitwise_not(temp)
            temp = cv2.bitwise_and(self.img_binary, temp)
            skel = cv2.bitwise_or(skel, temp)
            self.img_binary = cv2.erode(self.img_binary, element)
            _, max_val, _, _ = cv2.minMaxLoc(self.img_binary)
            done = (max_val == 0)

        # Calcular o ponto central (centroide) da imagem esqueletonizada
        moments = cv2.moments(skel)
        ponto_central_x = int(moments['m10'] / moments['m00'])
        ponto_central_y = int(moments['m01'] / moments['m00'])
        ponto_central_esqueleto = (ponto_central_x, ponto_central_y)
        print(f"Ponto central (centroide) do esqueleto da imagem {nome_imagem}: ", ponto_central_esqueleto)

        return skel

    def run(self):
        self.tratar_imagens()

        cv2.waitKey(0)
        cv2.destroyAllWindows()
