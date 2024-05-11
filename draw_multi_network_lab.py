import matplotlib.pyplot as plt
import matplotlib as mpl
if __name__ == '__main__':
    divide_channel = [16,19,25,28,29]
    divide_slot = [19,32,43,54,66]
    mdcg = [10, 14, 14, 16, 18]
    x = [2,3,4,5,6]
    plt.rcParams['font.family'] = 'Times New Roman ,SimSun '
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.tick_params(axis='both', direction='in')
    ax.plot(x, mdcg, '^-',markerfacecolor='none', color='c', label='JCNS', linewidth=1)
    ax.plot(x, divide_channel, 'o-',markerfacecolor='none', color='#FFA500', label='ANC', linewidth=1)
    ax.plot(x, divide_slot, 's-',markerfacecolor='none', color='m', label='CSA', linewidth=1)
    dashed_line = (5, 2)  # 定义虚线样式为每段长度为5、间隔为2的虚线
    plt.grid(True, linestyle='--', linewidth=0.5, dashes=dashed_line)  # 添加虚线网格
    plt.legend()
    plt.xlabel('number of flows')
    plt.ylabel('superframe length (time-slot)')
    plt.savefig('D:\\论文资料\\网络共存论文资料\\新的实验结果\\20240221\\multi-network-lab.png', dpi=300, bbox_inches='tight')
    plt.show()
