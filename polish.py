# -*- coding: utf-8 -*-
import numpy as np # numpy kütüphanesinin yüklenmiş olmasi gereklidir #numpy website #  https://numpy.org/
import sys# standart kütüphanedir.koddan çıkış için kullandım
#print(np.version.version) #kendi bilgisarimda nump sürümü 1.21.0 dır.
def notasyon_hesapla(alfabe):
    #alfabemizi aldık
    sonuc=0
    deger=0
    sayac=-1
    print("Ters çevrilmiş alfabemiz \n",alfabe)
    
    for i in alfabe:

        sayac=sayac+1
        if(i=='+'):#operand bir değer görülürse işlemlere başlıyoruz
            alfabe.pop(sayac)#operandı listeden kaldırıyoruz
            
            if(sayac>=3):#sayaca bakarak operand bulana kadar ne kadar adim gittik onu kontrol ediyoruz
                deger=sayac-2
                for i in alfabe[deger:sayac]:#operanddan onceki 2 degeri bulup doğru işleme tabi tutuyoruz
                    sonuc=float(float(i)+sonuc)   
                alfabe.pop(deger)#işlem yaptiğimiz degerleri listeden kaldırıyoruz
                alfabe.pop(deger)
            
            else:#sayacla ılgılı bır ıslem operanddan once 2 dan fazla deger yoksa buraya girer eger kı 2 den fazla değer varsa operanddan oncekı 2 degerı bulması ıcın
                 #if bloguna giricekti
                for i in alfabe[0:sayac]:
                    sonuc=float(float(i)+sonuc)#operanddan onceki 2 degeri bulup doğru işleme tabi tutuyoruz
            
                alfabe.pop(0)#işlem yaptiğimiz degerleri listeden kaldırıyoruz
                alfabe.pop(0)
           
            alfabe.insert(deger,str(sonuc))#sonucumuzu listemize ekliyoruz kaldırdıgımız operand ve sayilarin yerıne
            #degerın default degeri 0 dir.


            if(len(alfabe)==1):#eger listemiz bir adet değere düştüyse geriye sadece sonuç kalmış demektir sonucu yazdiririz.
                print("Sonuç",alfabe[0])
                break
            else:
                notasyon_hesapla(alfabe)#listemiz bir adet değere düşmediyse çıkarılmış ve sonuc eklenmiş yeni alfabemizle tekrar işlemlere gireriz.
        
        #****# + - / * için satirlar aynidir sadece sonuc=float(float(i) /*+- sonuc) kisminda gerekli operator konulmuştur ve duruma göre sonucun default değeri
        #****#belirlenmiştir örneğin sonuca 0 deseydik çarpim işlemi sürekli 0 olurdu o yüzden 1 dedik.
        
        if(i=='*'):
            sonuc=1
            alfabe.pop(sayac)
            if(sayac>=3):
                deger=sayac-2
                for i in alfabe[deger:sayac]:
                    sonuc=float(float(i)*sonuc)    
                alfabe.pop(deger)
                alfabe.pop(deger)
            else:    
                for i in alfabe[0:sayac]:
                    sonuc=float(float(i)*sonuc)  
                alfabe.pop(0)
                alfabe.pop(0)
            alfabe.insert(deger,str(sonuc))
            if(len(alfabe)==1):
                print("Sonuç",alfabe[0])
                break  
            else:
                notasyon_hesapla(alfabe)

        if(i=='-'):
            sonuc=0
            alfabe.pop(sayac)
            if(sayac>=3):
                deger=sayac-2
                for i in alfabe[deger:sayac]:
                    sonuc=float(float(i)-sonuc)
    
                alfabe.pop(deger)
                alfabe.pop(deger)
            else:    
                for i in alfabe[0:sayac]:
                    sonuc=float(float(i)-sonuc)
                alfabe.pop(0)
                alfabe.pop(0)
            alfabe.insert(deger,str(sonuc))
        
            
            if(len(alfabe)==1):
                print("Sonuç",alfabe[0])
                break  
            else:
                notasyon_hesapla(alfabe)
        if(i=='/'):

            sonuc=1
            alfabe.pop(sayac)
        
            if(sayac>=3):
                deger=sayac-2
                for i in alfabe[deger:sayac]:
                    sonuc=float(float(i)/sonuc)
                alfabe.pop(deger)
                alfabe.pop(deger)    
            else:    
                for i in alfabe[0:sayac]:
                    sonuc=float(float(i)/sonuc)  
                alfabe.pop(0)
                alfabe.pop(0)
            alfabe.insert(deger,str(sonuc))
        
            
            if(len(alfabe)==1):
                print("Sonuç",alfabe[0])
                break  
            else:
                notasyon_hesapla(alfabe)

        
if __name__ == "__main__":
    alf=[]
    alf1=[]
    alfabe=[]

    try:
        notasyon=input("Notasyonu aralarinda boşluk olcak şeklinde giriniz= ")#girilcek değerleri alıyoruz string olarak
    except:
        sys.exit()
    
    alf.append(notasyon)#str olarak aldıgımız degeri listeye atıyoruz
    
    for i in alf:
        alf1.append(i.split())#str bir bütün olduğu için split yontemiyle tek tek alf1 içine atıyoruz degerlerimizi
   
    arr=np.array(alf1)
    #[[]] formatında deger geldiği için bunu [] şekline çeviriyoruz daha rahat işlem yapabilmek için tek satırda yazıyoruz yani
    for i in arr: 
        for b in i:
            alfabe.append(b)

    print("Asil alfabemiz",alfabe)#inputlarımızı tek tek bir listeye yerlestirdik
    _=np.array(alfabe)#alfabeyı np.arraylere çeviriyoruz
    yeni_alfabe=np.flip(_, 0)#ters_cevrilmiş alfabe
    yeni_alfabe=yeni_alfabe.tolist()
    #liste üzerinde daha rahat işlem yapabilmek için önce np.arraye çevirip ters çeviriyoruz ardından listeye geri çeviriyoruz
    #polish algoritması uzerınde bir değişiklik yok sadece işlem kolaylığı için bunu yaptım
    
    kontrol=0
    kontrol2=0
    sayac_sayi=0
    sayac_operand=0
    #yanlis bir input olup olmadiğini kontrol ediyoruz inputlarda operand var mi sayi değeri var mi polish notasyonuna uygun yazilmişmi bunu kontrol ediyoruz
    for i in yeni_alfabe:
        if(i=="+" or i=="-" or i=="*" or i=="/"):
            kontrol=1
            sayac_operand=sayac_operand+1 #operandların sayısının hesaplanması
        else:
            try:
                a=float(i)#sayi var mı yok mu kontrolu
                sayac_sayi=sayac_sayi+1 #sayıların sayısının hesaplanması
                kontrol2=1
            except:
                sys.exit("Yanlis input girildi çikiş yapiliyor")
    if(sayac_sayi!=sayac_operand+1): #operand ve sayiların sayısının karsılastırılmasi
        sys.exit("Yanlis input girildi çikiş yapiliyor")
    if(kontrol==0 or kontrol2==0):#sayi veyahut operand olup olmadıgının kontrolü
        sys.exit("Yanlis input girildi çikiş yapiliyor")

    
    notasyon_hesapla(yeni_alfabe)#fonksiyonumuza listemizi yolluyoruz

