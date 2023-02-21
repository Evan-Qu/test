from create import create_multi_bars
from create import draw_pic_test
import numpy as np
import matplotlib.pyplot as plt

xlabels = ['12', '13', '20', '21', '30', '31']
ylables = "Normalized execution time"
labels = ['Oblivious', 'Hybrid', 'Ginger','TopoX', 'HCPD']
data = np.loadtxt("data/machines.csv")
#print(data)
#plt.ylabel(ylables)
# plt.title('multi datasets')
# x轴刻度标签位置与x轴刻度一致
#plt.xticks(ticks, xlabels)
#plt.legend(loc='best', ncol=5, bbox_to_anchor=(1.015, 1.1), prop={'size': 9})
# plt.legend(loc='best')
draw_pic_test(xlabels, ylables, labels, data)


#create_multi_bars(xlabels, ylables, labels, data, bar_gap=0.02)