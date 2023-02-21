from create import create_multi_bars
from create import create_multi_bars3
from create import draw_pic_test
from create import draw_pic_test2
from create import draw_pic_multi
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=[]
plt.rcParams['axes.unicode_minus']=False
'''
plt.rcParams['savefig.dpi'] = 300 # 图片像素
plt.rcParams['figure.dpi'] = 300 # 分辨率
#x = ['ljourney', 'uk-2002', 'pow2.0', 'uk-2005']
#x = ['ljourney', 'uk-2002', 'uk-2005', 'twitter', 'pow2.0']
x = ['core-twitter', 'pow1.8']
#x = ['High Cut', 'Low Cut']
ylables = "Execution time (sec)"
#labels = ['Oblivious', 'Hybrid', 'Ginger','TopoX', 'HCPD']
labels = ['Ginger','TopoX', 'HCPD']
#xlabels = "Pow2.0"
data = np.loadtxt("data/densetime.csv")
#print(data)
'''

#x = ['Hash', 'Greedy','DBH','HDRF', 'PDS', 'VCPD']
x = ['Orkut']
#x = ['Twitter', 'Friendster']
labels = ['Hash', 'Greedy','DBH','HDRF', 'PDS', 'VCPD']
ylables = "平衡系数"

'''
x = ['总时间','过滤阶段','检查阶段']
labels = ['范围划分','集中划分','均匀划分']
ylables  = "时间(秒)"

'''

'''
#x = ["1","2","3","4","5","6","7","8","9","10"]
x = ["1", "2" ,"4", "8"]
#labels = ["OpenNCI","Enamine","GraphGen"]
labels = ["PrefixFPM","ParPrefix-1","ParPrefix-3", "ParPrefix-3",]
data = np.loadtxt("data/vcpd_time.txt")
xlabels = "单机线程数"
ylables = "运行时间（秒）"
'''
data = np.loadtxt("data/vcpd_time.txt")
create_multi_bars(x, ylables, labels, data,  bar_gap=0.02) #group_gap=0.3,

#draw_pic_test(xlabels, ylables, x, labels, data)