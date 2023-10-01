import os
import cv2
from glcm_processor import GLCMProcessor
from estrutura import Estruturas
from PIL import Image


class ExtracaoDeCaracteristica:
    def __init__(self, diretorio):
        self.diretorio = diretorio
        self.converter_imagens()
        self.imagens = self.ler_imagens_diretorio()
        self.process_estruturas()
        # self.process_glcm()

    def process_glcm(self):
        glcm_processor = GLCMProcessor(self.imagens)
        glcm_processor.process()

    def process_estruturas(self):
        estrutura = Estruturas(self.imagens)
        estrutura.run()

    def converter_imagens(self):
        for filename in os.listdir(self.diretorio):
            if filename.endswith('.pgm'):
                caminho_pgm = os.path.join(self.diretorio, filename)

                # Lendo a imagem PGM
                img_pgm = cv2.imread(caminho_pgm, cv2.IMREAD_GRAYSCALE)

                if img_pgm is not None:
                    img_pil = Image.fromarray(img_pgm)

                    # Salvando a imagem como PNG
                    caminho_png = os.path.join("maiusculas_convertidas", os.path.splitext(filename)[0] + '.png')
                    img_pil.save(caminho_png, format='PNG')

    def ler_imagens_diretorio(self):
        imagens = []
        for filename in os.listdir("maiusculas_convertidas"):
            if filename.endswith('.png'):
                caminho_completo = os.path.join("maiusculas_convertidas", filename)
                img = cv2.imread(caminho_completo, cv2.IMREAD_GRAYSCALE)

                if img is not None:
                    imagens.append((filename, img))

        return imagens


if __name__ == "__main__":
    diretorio = "maiusculas_reduzidas"
    extracao = ExtracaoDeCaracteristica(diretorio)
