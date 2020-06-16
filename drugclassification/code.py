#kütüphanelerinyüklenmesi
from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd


e1=['asetilsalisilik_asit','parasetamol','propyphenazone','kafein','deksketoprofen_trometamol','naproksen','naproksen_sodyum','ibuprofen','psedoefedrin_hcl','klorfeniramin_maleat','fenilefrin_hcl','dekstrometorfan_hbr','oksolamin_sitrat','dekstrometorfan','difenhidramin_hcl','efedrin_hcl','karbamazepin','paroksetin','opipramol','tianeptin','sitalopram_hidrobromur','sertralin','mirtazapin','amitriptilin_hcl','fluoksetin_hcl','maprotilin_hcl','amlodipin','metoprolol_suksinat','valsartan','hidroklorotiyazid','lacidipin','diltiazem_hcl','losartan_potasyum','metildopa','metformin_hcl','akarboz','glimepirid','rosiglitazon','pioglitazon_hcl','gliklazid','glibenklamid','repaglinid','diflukortolon_valerat','izokonazol','terbinafin_hcl','tiyokonazol','sikloproxolamine_citrate','betametazon_valerat','kliokinol','heksamidin','klotrimazol','vitamin_b1','vitamin_b6','vitamin_b12','siyanokobalamin','tiamin_hcl','ribofilavin_sodyum_fosfat','pridoksin_hcl','pregabalin','pp_vitamini','folik_asit','askorbik_asit','ferroglikokol_sulfat','ranitidin','domperidon','hiyosin_n_butilbromur','rabeprazol','hidrotalsit','lansoprazol','sodyum_aljinat','potasyum_bikarbonat','dekspantenol','simetikon','kalsiyum_karbonat','magnezyum_karbonat']

ilac=['agri_kesici','soguk_alginligi','antidepresan','tansiyon','diyabet','mantar_enfeksiyonu','b12_vitamini','sindirim_sistemi']

e2=[]
for x in range( 0, len(e1)):
    e2.append(0)

#eğitimkümesinihazırlama
sonuc=pd.read_csv("Training.csv")

sonuc.replace({'hastalik_tahmin':{'agri_kesici':0,'soguk_alginligi':1,'antidepresan':2,'tansiyon':3,'diyabet':4,'mantar':5,'b12_vitamini':6,'sindirim_sistemi':7 }},inplace=True)


x_train= sonuc[e1]

y_train = sonuc[["hastalik_tahmin"]]
np.ravel(y_train)


#testkümesinihazırlama
tr=pd.read_csv("Testing.csv")
tr.replace({'hastalik_tahmin':{'agri_kesici':0,'soguk_alginligi':1,'antidepresan':2,'tansiyon':3,'diyabet':4,'mantar':5,'b12_vitamini':6,'sindirim_sistemi':7 }},inplace=True)

x_test= tr[e1]
y_test = tr[["hastalik_tahmin"]]
np.ravel(y_test)

#algoritmalar

def KararAgaci():

    from sklearn import tree
    snf1 = tree.DecisionTreeClassifier()  
    snf1 = snf1.fit(x_train,y_train)

#accuracyhesaplama
    from sklearn.metrics import accuracy_score
    y_tahmin=snf1.predict(x_test)
    print(accuracy_score(y_test, y_tahmin))
    print(accuracy_score(y_test, y_tahmin,normalize=False))
    # -----------------------------------------------------

    etkenm = [Etken1.get(),Etken2.get(),Etken3.get(),Etken4.get(),Etken5.get()]

    for i in range(0,len(e1)):
       
        for l in etkenm:
            if(l==e1[i]):
                e2[i]=1

    girdi = [e2]
    predict = snf1.predict(girdi)
    tahminsonucu=predict[0]

    t='false'
    for a in range(0,len(ilac)):
        if(tahminsonucu == a):
            t='true'
            break


    if (t=='true'):
        a1.delete("1.0", END)
        a1.insert(END, ilac[a])
    else:
        a1.delete("1.0", END)
        a1.insert(END, "Bulunamadi")

    from sklearn.metrics import confusion_matrix
   

def RassalOrman():
    from sklearn.ensemble import RandomForestClassifier
    snf2 = RandomForestClassifier()
    snf2 = snf2.fit(x_train,np.ravel(y_train))


    from sklearn.metrics import accuracy_score
    y_tahmin=snf2.predict(x_test)
    print(accuracy_score(y_test, y_tahmin))
    print(accuracy_score(y_test, y_tahmin,normalize=False))
   

    etkenm = [Etken1.get(),Etken2.get(),Etken3.get(),Etken4.get(),Etken5.get()]

    for i in range(0,len(e1)):
        for l in etkenm:
            if(l==e1[i]):
                e2[i]=1

    girdi = [e2]
    predict = snf2.predict(girdi)
    tahminsonucu=predict[0]

    t='false'
    for a in range(0,len(ilac)):
        if(tahminsonucu == a):
            t='true'
            break

    if (t=='true'):
        a2.delete("1.0", END)
        a2.insert(END, ilac[a])
    else:
        a2.delete("1.0", END)
        a2.insert(END, "Bulunamadi")


def NaifBayes(): 
    from sklearn.naive_bayes import GaussianNB
    GausNB = GaussianNB()
    GausNB=GausNB.fit(x_train,np.ravel(y_train))

 
    from sklearn.metrics import accuracy_score
    y_tahmin=GausNB.predict(x_test)
    print(accuracy_score(y_test, y_tahmin))
    print(accuracy_score(y_test, y_tahmin,normalize=False))
    
    etkenm = [Etken1.get(),Etken2.get(),Etken3.get(),Etken4.get(),Etken5.get()]
    for i in range(0,len(e1)):
        for l in etkenm:
            if(l==e1[i]):
                e2[i]=1

    girdi = [e2]
    predict = GausNB.predict(girdi)
    tahminsonucu=predict[0]

    t='false'
    for a in range(0,len(ilac)):
        if(tahminsonucu == a):
            t='true'
            break

    if (t=='true'):
        a3.delete("1.0",END)
        a3.insert(END, ilac[a])
    else:
        a3.delete("1.0",END)
        a3.insert(END, "Bulunamadi ")
        

#görselform(tkinter)
base = Tk()
base.geometry('1000x400')
base.configure(background='light blue')

#Header
header = Label(base, justify=CENTER, text= "MAKİNA ÖĞRENMESİ İLE PROSPEKTÜS/İLAÇ SINIFLANDIRMASI ",bg="white", fg="grey")
header.config(font=("Helvetica", 20))
header.grid(row=2, column=0, columnspan=2, pady=10, padx=25)


#Sol Etiket/etken maddeler
e1Label1 = Label(base, text="Etken Madde 1" ,fg="white", bg="grey").place(x=5, y =70)
e2Label2 = Label(base, text="Etken Madde 2", fg="white", bg="grey").place(x=5, y =110)
e3Label3 = Label(base, text="Etken Madde 3", fg="white", bg="grey").place(x=5, y =150)
e4Label4 = Label(base, text="Etken Madde 4", fg="white", bg="grey").place(x=5, y =190)
e5Label5 = Label(base, text="Etken Madde 5", fg="white", bg="grey").place(x=5, y =230)


# değişkenler
Etken1 = StringVar()
Etken1.set(0)
Etken2 = StringVar()
Etken2.set(0)
Etken3 = StringVar()
Etken3.set(0)
Etken4 = StringVar()
Etken4.set(0)
Etken5 = StringVar()
Etken5.set(0)
isim = StringVar()


#EtkenmaddeSecim
AYARLAR = sorted(e1)

E1Label1 = OptionMenu(base, Etken1,*AYARLAR)
E1Label1.grid(row=9, column=1, pady=5)

E2Label2 = OptionMenu(base, Etken2,*AYARLAR)
E2Label2.grid(row=10, column=1, pady =5)

E3Label3 = OptionMenu(base, Etken3,*AYARLAR)
E3Label3.grid(row=11, column=1,pady=5)

E4Label4 = OptionMenu(base, Etken4,*AYARLAR)
E4Label4.grid(row=12, column=1,pady =5)

E5Label5 = OptionMenu(base, Etken5,*AYARLAR)
E5Label5.grid(row=13, column=1, pady =5)


#algoritmaButon 
kaa = Button (base, text="KararAgaci", command=KararAgaci, bg="white", fg="blue")
kaa.grid(row=10, column=3,padx=20)

roa = Button (base, text="RassalOrman", command=RassalOrman, bg="white", fg= "blue" )
roa.grid(row=11, column=3,padx=20)

nba = Button (base, text="NaifBayes", command=NaifBayes, bg="white",fg= "blue")
nba.grid(row=12, column=3,padx=20)


#sol etiket/algoritma çıktıları
nbaLabel = Label(base, text="KararAgaci",bg="blue" ,fg="white" )
nbaLabel.grid(row=18, column=0,padx=5, pady=8,sticky=SW)

kaaLabel = Label(base, text="RassalOrman", bg="blue", fg="white")
kaaLabel.grid(row=20, column=0,padx=5, pady=8, sticky=SW)

raaLabel = Label(base, text="NaifBayes", bg="blue", fg="white")
raaLabel.grid(row=22, column=0,padx=5, pady=8,sticky=SW)


#text/çıktılar(sol etiket karşısı)
a1 = Text (base, height=1, width=40, bg="white",fg="black")
a1.grid(row=18, column=1, padx=6)

a2 = Text (base, height=1, width=40,bg="white",fg="black")
a2.grid(row=20, column=1 , padx=6)

a3 = Text (base, height=1, width=40,bg="white",fg="black")
a3.grid(row=22, column=1 , padx=6)


base.mainloop()
