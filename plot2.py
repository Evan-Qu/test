from create import create_multi_bars
from create import draw_pic_test
from create import draw_pic_test2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300 # 图片像素
plt.rcParams['figure.dpi'] = 300 # 分辨率
plt.subplots_adjust(left=0.15, bottom=0.2, right=0.9, top=0.95)

#plt.subplots_adjust(left=0.3, bottom=0.2, right=0.7, top=0.95)
#x = ["12","13","20","21","30","31"]
x = ["10M", "20M", "40M", "60M", "80M", "100M"]
#x = ["1.8", "1.9", "2.0", "2.1", "2.2"]
#x = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2056']
#x = ["1",'2','3','4','5','6','7','8','9','10']
xlabels = "Number of vertices"
#ylables = "Execution time (sec)"
#ylables = ["Replication factor", "Balance factor"]
ylables = ["Memory usage (MB)", "Ingress time (sec)"]
#labels = ['Oblivious', 'Hybrid', 'Ginger','TopoX', 'HCPD']
labels = ["Memory usage", "Ingress time"]
#labels = ["Replication factor", "Balance factor"]
data = np.loadtxt("data/machines_memory.csv")
#print(data)
#plt.ylabel(ylables)
# plt.title('multi datasets')
# x轴刻度标签位置与x轴刻度一致
#plt.xticks(ticks, xlabels)
#plt.legend(loc='best', ncol=5, bbox_to_anchor=(1.015, 1.1), prop={'size': 9})
# plt.legend(loc='best')
draw_pic_test2(xlabels, ylables, x, labels, data)


#create_multi_bars(xlabels, ylables, labels, data, bar_gap=0.02)