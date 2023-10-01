import cv2
import numpy as np
import matplotlib.pyplot as plt
from glcm import fast_glcm_dissimilarity, fast_glcm_homogeneity, fast_glcm_entropy, fast_glcm_contrast, fast_glcm_mean
import os


class GLCMProcessor:
    def __init__(self, image):
        self.imagens = image

    def process(self):
        for i in range(len(self.imagens)):
            filename, image = self.imagens[i]
            resized_image = cv2.resize(image, (200, 200))

            dissimilarity = fast_glcm_dissimilarity(resized_image)
            homogeneity = fast_glcm_homogeneity(resized_image)
            contrast = fast_glcm_contrast(resized_image)
            entropy = fast_glcm_entropy(resized_image)
            mean = fast_glcm_mean(resized_image)

            dissimilarity_scaled = (
                (dissimilarity - dissimilarity.min())
                / (dissimilarity.max() - dissimilarity.min())
                * 255
            )

            fig, axes = plt.subplots(2, 3, figsize=(12, 8))
            fig.suptitle(f"Métricas GLCM para {filename}", fontsize=16)

            axes[0, 0].imshow(resized_image, cmap="gray")
            axes[0, 0].set_title("Imagem Original")

            axes[0, 1].imshow(np.uint8(dissimilarity_scaled), cmap="gray")
            axes[0, 1].set_title("Dissimilarity")

            axes[0, 2].imshow(np.uint8(homogeneity * 255), cmap="gray")
            axes[0, 2].set_title("Homogeneity")

            axes[1, 0].imshow(np.uint8(contrast * 255), cmap="gray")
            axes[1, 0].set_title("Contrast")

            axes[1, 1].imshow(np.uint8(mean * 255), cmap="gray")
            axes[1, 1].set_title("Mean")

            axes[1, 2].imshow(np.uint8(entropy * 255), cmap="gray")
            axes[1, 2].set_title("Entropy")

            # plt.show()

            plt.savefig(os.path.join("GLCM_IMAGES", filename), dpi=300)
