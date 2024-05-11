import matplotlib.pyplot as plt
import matplotlib as mpl
if __name__ == '__main__':
    network3 = [234.0, 238.0, 239.5, 240.5, 244.0, 247.0, 251.0, 253.0, 255.0, 254.0]
    network1 = [250.5, 255.0, 262.0, 267.0, 269.5, 271.0, 270.5, 273.0, 272.0, 275.5]
    network2 = [280.0, 271.5, 263.0, 257.0, 251.0, 246.5, 243.5, 238.5, 237.5, 235.0]
    x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    plt.rcParams['font.family'] = 'Times New Roman ,SimSun '
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.tick_params(axis='both', direction='in')
    ax.plot(x, network2, '^-',markerfacecolor='none', color='c', label='network B', linewidth=1)
    ax.plot(x, network1, 'o-',markerfacecolor='none', color='#FFA500', label='network A', linewidth=1)
    ax.plot(x, network3, 's-',markerfacecolor='none', color='m', label='network C', linewidth=1)
    dashed_line = (5, 2)  # 定义虚线样式为每段长度为5、间隔为2的虚线
    plt.grid(True, linestyle='--', linewidth=0.5, dashes=dashed_line)  # 添加虚线网格
    plt.legend()
    plt.xlabel('weight value')
    plt.ylabel('average delay (ms)')
    plt.savefig('D:\\论文资料\\网络共存论文资料\\新的实验结果\\20240221\\weight-lab.png', dpi=300,
                bbox_inches='tight')
    plt.show()
