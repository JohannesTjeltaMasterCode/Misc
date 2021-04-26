import numpy as np

import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import stats
"""
line 9-20 are defining arrays for where to get the information
about the nuclear dose. The working directory are Results so
the program is constructed around this.
"""
IonArrayNuc1=["Dose1.0Gy1000cellsNuc1_2MeV","Dose1.0Gy1000cellsNuc1_4MeV",
                "Dose1.0Gy1000cellsNuc1_8MeV","Dose1.0Gy1000cellsNuc8MeV"]
IonArrayNuc2=["Dose2.0Gy1000cellsNuc1_2MeV","Dose2.0Gy1000cellsNuc1_4MeV",
                "Dose2.0Gy2000cellsNuc1_8MeV","Dose2.0Gy2000cellsNuc8MeV"]
IonArrayNuc3=["Dose3.0Gy1000cellsNuc1_2MeV","Dose3.0Gy1000cellsNuc1_4MeV",
                "Dose3.0Gy1000cellsNuc1_8MeV","Dose3.0Gy2000cellsNuc8MeV"]
IonArrayNuc5=["Dose5.0Gy1000cellsNuc1_2MeV","Dose5.0Gy1000cellsNuc1_4MeV",
                "Dose5.0Gy1000cellsNuc1_8MeV","Dose5.0Gy500cellsNuc8MeV"]
IonArrayNuc8=["Dose8.0Gy1000cellsNuc1_2MeV","Dose8.0Gy1000cellsNuc1_4MeV",
                "Dose8.0Gy3000cellsNuc1_8MeV","Dose8.0Gy1000cellsNuc8MeV"]
IonArrayNuc10=["Dose10.0Gy1000cellsNuc1_2MeV","Dose10.0Gy1000cellsNuc1_4MeV",
                "Dose10.0Gy3000cellsNuc1_8MeV","Dose10.0Gy1000cellsNuc8MeV"]

def IonAnalasis(IonArrayNuc,string,plotname):
    path = 'DataOut'  # defining a path
    document='.txt'
    sigma=np.zeros(len(IonArrayNuc))  # sigma and mu are used to store sd and mean from each dataset
    mu=np.zeros(len(IonArrayNuc))
    plt.figure(figsize=(10, 4.4))
    for i,str in enumerate(IonArrayNuc):  # for loop to get info from textfile
        ionArray =np.loadtxt(path+'/'+str+document)
        histIon,binsIon= np.histogram(ionArray,bins=30,density=True)
        bins_middleIon= np.zeros(len(histIon))
        for ii in range(len(histIon)):
            bins_middleIon[ii]=binsIon[ii]-np.abs(binsIon[ii+1]-binsIon[ii])

        mu[i],sigma[i]=norm.fit(ionArray)
        plt.hist(ionArray,histtype=u'step',bins=30,density=True)
        print(ionArray)
    plt.grid()
    plt.xlabel('Dose [Gy]',fontsize=13)
    plt.ylabel('Ammount of cells [Normalized]',fontsize=13)
    plt.yticks(fontsize=13)
    plt.xticks(fontsize=13)
    #plt.title('Dose distrebution for nuclei for {} protons'.format(string),fontsize=13)
    plt.legend(('1.2MeV    $\sigma$={:1.3f}'.format(sigma[0]),'1.5MeV    $\sigma$={:1.3f}'.format(sigma[1]),
                '1.8MeV    $\sigma$={:1.3f}'.format(sigma[2]),'8.7MeV    $\sigma$={:1.3f}'.format(sigma[3]),'lol'))
    plt.savefig('Plots/Dosedistperc/'+plotname,bbox_inches='tight')


"""
line 52-59 are for plotting the different datasets.
"""
IonAnalasis(IonArrayNuc1,'1gy','1gy.png')
IonAnalasis(IonArrayNuc2,'2gy','2gy.png')
IonAnalasis(IonArrayNuc3,'3gy','3gy.png')
IonAnalasis(IonArrayNuc5,'5gy','5gy.png')
IonAnalasis(IonArrayNuc8,'8gy','8gy.png')
IonAnalasis(IonArrayNuc10,'10gy','10gy.png')

plt.show()
