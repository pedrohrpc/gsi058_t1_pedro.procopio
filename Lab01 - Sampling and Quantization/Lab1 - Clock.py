import cv2
import matplotlib.pyplot as plt
import numpy as np

dpi1250 = 1250
dpi300 = 300
dpi150 = 150
dpi72 = 72

img = cv2.imread("relogio.tif", cv2.IMREAD_GRAYSCALE)


def mediaMatriz(matriz, linhaInicial, linhaFinal, colunaInicial, colunaFinal):

    total = 0
    cont = 0
    for i in range(linhaInicial,linhaFinal):
        for j in range(colunaInicial,colunaFinal):
            total = total + matriz[i][j]
            cont = cont + 1

    return total/cont

# convertendo para 300dpi
linhas = img.shape[0]
colunas = img.shape[1]

razao = dpi1250/dpi300
linhas300 = int(linhas/razao)
colunas300 = int(colunas/razao)
erro = 0
passo = int(razao)

img300 = np.zeros((linhas300,colunas300))

for i in range(0,linhas300,passo):

    for j in range(0,colunas300,passo):

        img300[i][j] = mediaMatriz(img, i*passo, i*passo+passo, j*passo, j*passo+passo)


print('Tamanho da imagem 1 : ',img.shape)
cv2.imshow('Original',img)

print('Tamanho da imagem 2 : ',img300.shape)
cv2.imshow('300',img300)
cv2.waitKey(0)
cv2.destroyAllWindows()
