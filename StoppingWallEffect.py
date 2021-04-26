import numpy as np
import matplotlib.pyplot as plt


water=list(open('Programtildisk/water.txt','r'))
print(len(water))
for i,str in enumerate(water):
    water[i]=float(str[10:19])
    print(water[i],i)


m20=list(open('Programtildisk/m20.txt','r'))
for i,str in enumerate(m20):
    m20[i]=float(str[10:19])
muscle=list(open('Programtildisk/muscle.txt','r'))
for i,str in enumerate(muscle):
    muscle[i]=float(str[10:19])
energy=list(open('Programtildisk/energy.txt','r'))
for i,str in enumerate(energy):
    energy[i]=str[0:9]
max=10
min=0
fig= plt.figure(figsize=(10, 4.4))
plt.plot(energy[min:max],water[min:max],label='Water')
plt.plot(energy[min:max],m20[min:max],label='MS20')
plt.plot(energy[min:max],muscle[min:max],label='Muscle')
plt.legend()
#plt.grid()
plt.xlabel('Energy [MeV]',fontsize=13)
plt.ylabel('Stopping Power [MeV $cm^2$/g]',fontsize=13)
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
plt.xscale('log')
plt.yscale('log')
plt.savefig('Plots/StoppingPower.jpg',bbox_inches='tight')
plt.show()
