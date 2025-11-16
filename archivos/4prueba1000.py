#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:55:55 2021

@author: xxxxx
"""
import pandas as pd
# Funciones
"""
Este script toma como entrada un dataset y lo blanquea por sobrepaso. 
"""
# Principale
def azteca_main(dataframe1=None, dataframe2 = None):
    longitudTotal=len(dataframe1)
    champos=dataframe1.columns.tolist()
    sumaPositEnTarget=sum(list(dataframe1.iloc[:,len(champos)-1]))
    aMultiplicar=int(round(1/(sumaPositEnTarget/longitudTotal)))
    print('k=',aMultiplicar)
    df=pd.DataFrame()
    for i in range(len(champos)):
        nuevaLista=[]
        for j in range(longitudTotal):
            if(dataframe1.iloc[j,len(champos)-1]==1):
                for k in range(aMultiplicar):
                    nuevaLista.append(dataframe1.iloc[j,i])
            else:
                nuevaLista.append(dataframe1.iloc[j,i])        
        df[campos[i]]=nuevaLista
    return df
data1=pd.read_csv('cabecita.csv')
data2=[]
df=azteca_main(data1, data2)
df.to_csv('arch.csv')
