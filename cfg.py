#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np # numpy kütüphanesinin yüklenmiş olmasi gereklidir #numpy website #  https://numpy.org/
import warnings 
#yorum satırı koymaya vaktim kalmadı hocam
warnings.filterwarnings("ignore")
#S->aa|bX|aXX,X->ab|b

global kontrol

def sonuc(ifade,index1,index2,kontrol):
    GeciciList=[]
    uzunluk=len(ifade)
    geciciifade=""
    ifade1=ifade[:index1]
    ifade2=ifade[:index2]
    
    if(kontrol==0):
        
        for index in range(1):     
            for xindex in range(2):
                ifade1+=X[xindex]+ifade[index1+1:uzunluk]
                ifade2+=X[xindex]+ifade[index2+1:uzunluk]
                GeciciList.append(ifade1)
                GeciciList.append(ifade2)
                ifade1 = ifade[:index1]
                ifade2 = ifade[:index2]
    
        for sayi in range(len(GeciciList)):
            geciciifade=GeciciList[sayi]
            search_fonk(geciciifade)

    if(kontrol==1):
        for index in range(1):
            for xindex in range(2):
                ifade1+=X[xindex]+ifade[index1+1:uzunluk]
                Genelliste.append(ifade1)
                ifade1 = ifade[:index1]

def search_fonk(ifade):
    indexliste=[]
    index=0
    bayrak=0
    kontrol=0

    for harf in ifade:
        if harf == "X":
         indexliste.append(index)
         bayrak=1

        index+=1
    if bayrak == 0:
        Genelliste.append(ifade)
        bayrak=0


    uzunluk=len(indexliste)
    
    if uzunluk==1:
        kontrol=1
        ind=indexliste[0]
        sonuc(ifade,ind,0,kontrol)
    
    elif uzunluk==2:
        kontrol=0
        ind=indexliste[0]
        ind2=indexliste[1]
        sonuc(ifade,ind,ind2,kontrol)

if __name__ == '__main__':
    Genelliste = []
    Tekrar=[]
    As=[]
    X = []
    X1=[]
    S = []
    S1=[]
    alf=[]
    alf1=[]
    alfabe=[]
    alf2=[]
    liste=[]
    liste2=[]
    xalf=[]
    xalf1=[]
    xalf2=[]
    Xalfabe=[]
    
    giriş=input("İfadeyi giriniz ")
 
    alf.append(giriş)


    for i in alf:
        liste.append(i.split(","))
    for i in liste:
        for a in i:
            liste2.append(a)
            if(a==","):
                break
    alf.clear()
    alf.append(liste2[0])
    xalf.append(liste2[1])
    
    for i in alf:
        alf1.append(i.split("|"))
    for i in alf1:
        for a in i:
            alf2.append(a.split(">"))
    arr=np.array(alf2)
    for i in arr: 
        for b in i:
            alfabe.append(b)
    uzunluk_alfabe=len(alfabe)
    S1.append(alfabe[1:uzunluk_alfabe])
    for i in S1:
        for a in i:
            S.append(a)
    print("S elemanlari",S)
    

    
    for i in xalf:
        xalf1.append(i.split("|"))
    for i in xalf1:
        for a in i:
            xalf2.append(a.split(">"))

    Xarr=np.array(xalf2)
    for i in Xarr: 
        for b in i:
            Xalfabe.append(b)
    uzunlukX_alfabe=len(Xalfabe)
    X1.append(Xalfabe[1:uzunlukX_alfabe])
    for i in X1:
        for a in i:
            X.append(a)
    print("X elemanlari",X)


    for i in range(uzunluk_alfabe-1):
        ifade=S[i]
       
        search_fonk(ifade)


    for i in Genelliste:
        if i not in As:
            As.append(i)
        else:
            Tekrar.append(i)

    print("Liste ")
    print(As)
    print("Tekrar eden Kelimeler ")
    print(Tekrar)
   

