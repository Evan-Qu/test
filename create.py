import matplotlib.pyplot as plt
import numpy as np




def create_multi_bars(x, ylables, labels, datas, tick_step=1, group_gap=0.2, bar_gap=0):
    '''
    labels : x轴坐标标签序列
    datas ：数据集，二维列表，要求列表每个元素的长度必须与labels的长度一致
    tick_step ：默认x轴刻度步长为1，通过tick_step可调整x轴刻度步长。
    group_gap : 柱子组与组之间的间隙，最好为正值，否则组与组之间重叠
    bar_gap ：每组柱子之间的空隙，默认为0，每组柱子紧挨，正值每组柱子之间有间隙，负值每组柱子之间重叠
    '''
    # ticks为x轴刻度
    ticks = np.arange(len(x)) * tick_step
    # group_num为数据的组数，即每组柱子的柱子个数
    group_num = len(datas)
    # group_width为每组柱子的总宽度，group_gap 为柱子组与组之间的间隙。
    group_width = tick_step - group_gap
    # bar_span为每组柱子之间在x轴上的距离，即柱子宽度和间隙的总和
    bar_span = group_width / group_num
    # bar_width为每个柱子的实际宽度
    bar_width = bar_span - bar_gap
    # baseline_x为每组柱子第一个柱子的基准x轴位置，随后的柱子依次递增bar_span即可
    baseline_x = ticks - (group_width - bar_span) / 2
    i = 0
    for index, y in enumerate(datas):
        plt.bar(baseline_x + index * bar_span, y, bar_width, label=labels[i])
        i = i + 1

    plt.ylabel(ylables, fontsize=12, font={'family':'SimSun'})
    #plt.ylim(0, 0.015)
    #plt.xlabel(xlabels)
    # plt.title('multi datasets')
    # x轴刻度标签位置与x轴刻度一致
    plt.xticks(ticks, x, fontsize=12,)#font={'family':'SimSun'}
    #plt.legend(loc='best', ncol=5, bbox_to_anchor=(0.98, 1.1), prop={'size': 8, 'weight': 'bold'}) #0.915
    #plt.legend(loc='best', ncol=5, bbox_to_anchor=(1.01, 1.12), prop={'size': 8, 'weight': 'bold'}) #0.915
    #plt.tight_layout()
    plt.legend(loc='best', prop={'size': 8, 'weight': 'bold'})#, 'family': 'SimSun'
    #plt.savefig('pg.pdf', bbox_inches='tight')
    plt.show()

def create_multi_bars3(xlabels, ylables, labels, datas, tick_step=1, group_gap=0.2, bar_gap=0):
    '''
    labels : x轴坐标标签序列
    datas ：数据集，二维列表，要求列表每个元素的长度必须与labels的长度一致
    tick_step ：默认x轴刻度步长为1，通过tick_step可调整x轴刻度步长。
    group_gap : 柱子组与组之间的间隙，最好为正值，否则组与组之间重叠
    bar_gap ：每组柱子之间的空隙，默认为0，每组柱子紧挨，正值每组柱子之间有间隙，负值每组柱子之间重叠
    '''
    # ticks为x轴刻度
    ticks = np.arange(len(xlabels)) * tick_step
    # group_num为数据的组数，即每组柱子的柱子个数
    group_num = len(datas)/2
    # group_width为每组柱子的总宽度，group_gap 为柱子组与组之间的间隙。
    group_width = tick_step - group_gap
    # bar_span为每组柱子之间在x轴上的距离，即柱子宽度和间隙的总和
    bar_span = group_width / group_num
    # bar_width为每个柱子的实际宽度
    bar_width = bar_span - bar_gap
    # baseline_x为每组柱子第一个柱子的基准x轴位置，随后的柱子依次递增bar_span即可
    baseline_x = ticks - (group_width - bar_span) / 2
    i = 0
    for index, y in enumerate(datas[0:4]):
        plt.bar(baseline_x + index * bar_span, y, bar_width, label=labels[i]+"(high)")
        plt.bar(baseline_x + index * bar_span, datas[index+4], bar_width, bottom = y, label=labels[i]+"(low)")
        i = i + 1

    plt.ylabel(ylables)
    # plt.title('multi datasets')
    # x轴刻度标签位置与x轴刻度一致
    plt.xticks(ticks, xlabels)
    #plt.legend(loc='best', ncol=5, bbox_to_anchor=(1.015, 1.1), prop={'size': 9})
    plt.legend(loc='best')
    plt.show()

def draw_pic_test(xlables, ylabels, x, labels, data):
    '''
    作图
    '''
    #colors=['red', 'blue', 'green', 'dodgerblue', 'magenta']
    markers=['*', 'v', '^', 'o', 'D']
    #data = [data]
    for i in range(len(data)):
        plt.plot(x, data[i], marker=markers[i], linestyle='-', label=labels[i])
    plt.legend(prop={'size': 7, 'weight': 'bold'})  # 显示图例

    plt.ylabel(ylabels, fontsize=14,font={'family':'SimSun'})  # 设置Y轴标签
    plt.xlabel(xlables, fontsize=14,font={'family':'SimSun'})
    #plt.xlabel("prediction Horizon(s)")  # 设置X轴标签
    plt.show()

def draw_pic_test2(xlables, ylabels, x, labels, data):
    '''
    作图
    '''
    colors=['red', 'blue', 'green', 'dodgerblue', 'magenta']
    markers=['*', 'v', '^', 'o', 'D']
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    line1 = ax1.plot(x, data[0], color = colors[2], marker=markers[0], linestyle='-', label=labels[0])
    ax1.set_ylabel(ylabels[0], fontsize=14)  # 设置Y轴标签
    ax2 = ax1.twinx()
    line2 = ax2.plot(x, data[1],  color = colors[3], marker=markers[3], linestyle='-', label=labels[1])
    ax2.set_ylabel(ylabels[1], fontsize=14,)  # 设置Y轴标签
    ax2.set_ylim(0, 800)
    #ax1.tick_params(labelsize=8)
    ax1.set_xlabel(xlables, fontsize=14,)

    ax = line1 + line2
    labels = [line.get_label() for line in ax]
    #plt.legend(ax, labels, prop={'weight': 'bold'})
    plt.legend(ax, labels, loc="upper left",prop={'weight': 'bold'})

    #plt.xlabel("prediction Horizon(s)")  # 设置X轴标签
    plt.show()


def create_multi_bars2(labels, datas, tick_step=1, group_gap=0.2, bar_gap=0):
    '''
    labels : x轴坐标标签序列
    datas ：数据集，二维列表，要求列表每个元素的长度必须与labels的长度一致
    tick_step ：默认x轴刻度步长为1，通过tick_step可调整x轴刻度步长。
    group_gap : 柱子组与组之间的间隙，最好为正值，否则组与组之间重叠
    bar_gap ：每组柱子之间的空隙，默认为0，每组柱子紧挨，正值每组柱子之间有间隙，负值每组柱子之间重叠
    '''
    # x为每组柱子x轴的基准位置
    x = np.arange(len(labels)) * tick_step
    # group_num为数据的组数，即每组柱子的柱子个数
    group_num = len(datas)
    # group_width为每组柱子的总宽度，group_gap 为柱子组与组之间的间隙。
    group_width = tick_step - group_gap
    # bar_span为每组柱子之间在x轴上的距离，即柱子宽度和间隙的总和
    bar_span = group_width / group_num
    # bar_width为每个柱子的实际宽度
    bar_width = bar_span - bar_gap
    # 绘制柱子
    for index, y in enumerate(datas):
        plt.bar(x + index * bar_span, y, bar_width)
    plt.ylabel('Scores')
    plt.title('multi datasets')
    # ticks为新x轴刻度标签位置，即每组柱子x轴上的中心位置
    ticks = x + (group_width - bar_span) / 2
    plt.xticks(ticks, labels)
    plt.show()

def draw_pic_multi(xlables, ylabels, x, labels, data):
    '''
    作图
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.bar(x, data, color='steelblue');
    ax2 = ax1.twinx()
    ax2.plot(x, data,'or-');


    plt.show()