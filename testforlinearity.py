#import libraries
import uproot
import numpy as np
import matplotlib.pyplot as plt
import os
dz=4*1e3
data_path = ('Data1_2/','Data1_4/','Data1_8/','Data8/')
N=10000
n=4
differance = np.zeros((N,n))

for j,path in enumerate(data_path):
    root_files=os.listdir(path)
    nn=100
    if 'Res'in root_files:
        root_files.remove('Res')
    if 'analasis' in root_files:
        root_files.remove('analasis')
    N=len(root_files)
    tot_ener_dep=np.zeros(nn)
    for i,root in enumerate(root_files):
        file = uproot.open(path+root)['microdosimetry']
        z=file['z'].array()
        x=file['x'].array()
        y=file['y'].array()
        energy=file['totalEnergyDeposit'].array()
        if len(z)>1:
            print(root)
            x=x[np.where((z>z[0])&(z<z[0]+dz))]
            y=y[np.where((z>z[0])&(z<z[0]+dz))]
            z=z[np.where((z>z[0])&(z<z[0]+dz))]
            energy=energy[np.where((z>z[0])&(z<z[0]+dz))]
            x0=x[0]
            y0=y[0]
            x_null = x-x0
            y_null = y-y0
            z=z-z[0]
            dist=np.linspace(0,4000,nn)
            energy_deposit_bin=np.zeros(nn)
            print(len(energy))
            for ii in range(nn-1):
                bin=np.where((z>dist[ii])&(z<dist[ii+1]))
                energy_deposit_bin[ii]=sum(energy[bin])
            tot_ener_dep+=energy_deposit_bin

    tot_ener_dep=tot_ener_dep/N
    plt.plot(dist,tot_ener_dep)
    plt.show()


"""
plt.hist(differance[:,0],bins=20,range=[0.,1000.],alpha=0.7,label='1.1 MeV')
plt.hist(differance[:,1],bins=20,range=[0.,1000.],alpha=0.7,label='1.4 MeV')
plt.hist(differance[:,2],bins=20,range=[0.,1000.],alpha=0.7,label='1.8 MeV')
plt.hist(differance[:,3],bins=20,range=[0.,1000.],alpha=0.7,label='8.6 MeV')
plt.xlabel('path differance from straight line [nm]')
plt.ylabel('ammount')
plt.title('How far do protons stray from a path in nm')
plt.grid()
plt.xscale()
plt.legend(loc='best')
plt.show()
"""
