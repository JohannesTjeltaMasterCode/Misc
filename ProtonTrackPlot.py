import uproot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


path = ['Data1_2','Data1_4','Data1_8','Data8']
proton =['2.root','52.root','106.root','19.root']
dz=4000
for i,str in enumerate(path):
    specificProt=uproot.open(str+'/'+proton[i])['microdosimetry']
    x = specificProt['x'].array()
    y = specificProt['y'].array()
    z = specificProt['z'].array()
    particle = specificProt['flagParticle'].array()
    process = specificProt['flagProcess'].array()
    Energy=specificProt['totalEnergyDeposit'].array()
    z_index=np.where((z>z[0])&(z<z[0]+dz))
    z=z[z_index]
    x=x[z_index]
    y=y[z_index]
    Energy=Energy[z_index]
    particle=particle[z_index]
    process=process[z_index]
    x0=x[0];x=x-x0
    y0=y[0];y=y-y0
    z0=z[0];z=z-z0

    #print(len(x[np.where((process==12)|(process==22))]),len(x[np.where((process==13)|(process==23))]),len(z))
    print(str)
    x_el=x[np.where(particle==1)]
    y_el=y[np.where(particle==1)]
    z_el=z[np.where(particle==1)]
    x_p=x[np.where(particle==2)]
    y_p=y[np.where(particle==2)]
    z_p=z[np.where(particle==2)]
    print(z_p[0])
    dz_array=np.linspace(0,dz,100)
    """
    local_deposit=np.zeros(100)
    local_deposit_exi=np.zeros(100)
    local_deposit_ion=np.zeros(100)
    for i in range(len(dz_array)-1):
        local_deposit[i]=sum(Energy[np.where((z>dz_array[i])&(z<dz_array[i+1]))])
        local_deposit_ion[i]=sum(Energy[np.where((z>dz_array[i])&(z<dz_array[i+1])&((process==13)|(process==23)))])
        local_deposit_exi[i]=sum(Energy[np.where((z>dz_array[i])&(z<dz_array[i+1])&((process==12)|(process==22)))])
    plt.figure(figsize=(10, 10))
    plt.step(dz_array[:-1],local_deposit[:-1],label='Tot deposit per length')
    plt.step(dz_array[:-1],local_deposit_ion[:-1],label='Ion deposit per length')
    plt.step(dz_array[:-1],local_deposit_exi[:-1],label='Exci deposit per length')
    plt.ylim((0,4000))
    plt.grid()
    plt.xlabel('Dist [nm]',fontsize=13)
    plt.ylabel('Energy deposit [eV/10*nm]',fontsize=13)
    plt.yticks(fontsize=13)
    plt.xticks(fontsize=13)
    plt.legend()

    plt.savefig('Plots/EnergyDeposit{}.png'.format(str),bbox_inches='tight')
    """
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot3D(x_p,y_p,z_p,'red',label='Proton')
    ax.plot3D(x_el,y_el,z_el,label='Electron',marker='.',ms=300./300, mew=0, linestyle="", lw=0,color='blue')
    ax.set_xlabel('Length [nm]')
    ax.set_ylabel('Length [nm]')
    ax.set_zlabel('Length [nm]')
    ax.legend()
    ax.view_init(elev=10.,azim=70)
    ax.view_init(15, 180)
    from matplotlib import ticker
    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1,1))
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    ax.zaxis.set_major_formatter(formatter)
    plt.subplots_adjust(top=1,bottom=0)

    plt.savefig('Plots/ProtonTrack/PtrotonTrack'+str+'.png',bbox_inches='tight',dpi=300)
