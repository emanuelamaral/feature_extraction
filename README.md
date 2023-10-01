# Extração de características de imagens utilizando Python OpenCV

Este é um projeto que utiliza a biblioteca OpenCV em Python para a extração de características de imagens.
Neste trabalho, irei demonstrar como carregar uma imagem, redimensioná-la e calcular métricas baseadas em GLCM (Matriz de Coocorrência de Nível de Cinza), como dissimilaridade, homogeneidade, contraste, energia e entropia.
As métricas GLCM fornecem informações valiosas sobre a textura e estrutura da imagem. 
Além disso, exploraremos a extração de características por meio da identificação de contornos e aplicação de esqueletização para obter informações relacionadas à forma e estrutura da imagem.
Vamos apresentar graficamente essas métricas para cada imagem processada.

## Sobre o trabalho

- Disciplina: OP63I-CC8 - Processamento de Imagens e Reconhecimento de Padrões
- Turma: 2023/2 - 8° Período
- Professor: Pedro Luiz de Paula Filho

## Pré-requisitos e Instalação no Linux

### Python (versão recomendada: 3.11 ou superior)

A maioria das distribuições Linux já vem com o Python instalado. Para verificar se o Python está instalado, abra o terminal e digite:

`python3 --version`

Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu/Debian:

`
sudo apt-get update
sudo apt-get install python3
`

No Arch Linux:

`
sudo pacman -Sy python
`

### PyCharm (ou qualquer outra IDE de sua escolha)

Você pode baixar o PyCharm diretamente do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/) ou, se preferir, pode usar o gerenciador de pacotes da sua distribuição para instalar a versão Community:

#### Ubuntu/Debian:

`
sudo snap install pycharm-community --classic
`

#### Arch Linux:

`
sudo pacman -Sy pycharm-community
`

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes Python:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Pré-requisitos e Instalação no Windows

### Python (versão recomendada: 3.11 ou superior)

1. Baixe o instalador Python para Windows no site oficial (https://www.python.org/downloads/windows/).

2. Execute o instalador e marque a opção "Adicionar o Python X.Y ao PATH" durante a instalação, onde X.Y é a versão do Python (por exemplo, 3.11).

### PyCharm (ou qualquer outra IDE de sua escolha)

1. Baixe o instalador do PyCharm Community ou Professional do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/).

2. Execute o instalador e siga as instruções na tela.

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes de pacotes Python:

Abra o prompt de comando (cmd) e execute:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Executando o Projeto

1. Clone este repositório em seu sistema:

`
git clone https://github.com/seuusuario/python-opencv-trabalho.git
`

2. Abra o projeto no PyCharm (ou sua IDE preferida).

## Modo de Uso
A aplicação realizará o processo de extração das características por meio do GLCM e também do contorno e esqueletização das imagens.
O GLCM salvará as imagens que foram analisadas enquanto que as analises estruturais passarão as informações das imagens no console.

## Autores

- Amoz Emanuel

## Referências

- [OpenCV Documentation](https://docs.opencv.org/)
- [Python.org](https://www.python.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
