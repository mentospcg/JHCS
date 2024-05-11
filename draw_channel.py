import matplotlib.pyplot as plt
import matplotlib as mpl
if __name__ == '__main__':
    divide_channel = [52,46,45,38,34,33,31,29,28,27,27,27,27,26]
    divide_slot = [68,63,62,62,61,61,60,62,61,62,60,61,60,60]
    mdcg = [49,38,32,28,27,26,26,25,25,24,24,24,24,24]
    x = [i for i in range(3,17)]
    plt.rcParams['font.family'] = 'Times New Roman ,SimSun '
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.tick_params(axis='both', direction='in')
    ax.plot(x, mdcg, '^-',markerfacecolor='none',color='c', label='JCNS', linewidth=1)
    ax.plot(x, divide_channel, 'o-',markerfacecolor='none', color='#FFA500', label='ANC', linewidth=1)
    ax.plot(x, divide_slot, 's-', markerfacecolor='none',color='m', label='CSA', linewidth=1)
    dashed_line = (5, 2)  # 定义虚线样式为每段长度为5、间隔为2的虚线
    plt.grid(True, linestyle='--', linewidth=0.5, dashes=dashed_line)  # 添加虚线网格
    plt.legend()
    plt.xlabel('number of channels')
    plt.ylabel('superframe length (time-slot)')
    plt.savefig('D:\\论文资料\\网络共存论文资料\\新的实验结果\\20240221\\channel-lab.png', dpi=300, bbox_inches='tight')
    plt.show()


