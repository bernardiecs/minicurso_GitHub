# -*- coding: utf-8 -*-
"""

---------------------------first_script.py-------------------------------------

Este script é um teste para o curso de GitHub

@author: Ewerthon Bernardi

-------------------------------------------------------------------------------
"""

#importação de pactoes para usar este script
import numpy as np
import matplotlib.pyplot as plt

#Função para gerar um plot de séries temporais
def timeSeriesPlot(arr):
    """
    Parameters
    ----------
    arr : np.array
        array numpu com a matriz de dados.

    Returns
    -------
    fig : TYPE
        DESCRIPTION.


    Exemplos de uso:
        fig = timeSeriesPlot(arr)
    """
    #Média do eixo 1
    arr_average = np.mean(arr,axis=1)
    
    #Criando uma figura
    fig, ax = plt.subplots(2)
    
    #Plotando a média e dados brutos
    ax[0].plot(arr_average)
    ax[1].plot(arr)
    
    fig.savefig("C:\\Documentos\\Repositorios_GitHub\\minicurso_GitHub\\"+
                "figuras\\timeSeriesPLot.png", dpi=300)
    
    return fig, arr_average

