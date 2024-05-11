import matplotlib.pyplot as plt
import matplotlib as mpl
def read_flow_path(new_file_name):
    file_head = 'D:\\论文资料\\网络共存论文资料\\共存网络论文资料\\new_data\\随机型数据流实验1数据\\' + new_file_name + '\\network_path'
    suffix = '.txt'
    for i in range(N):
        file_path = file_head + str(i+1) + suffix
        file_handle = open(file_path,'r')
        temp_path = []
        for line in file_handle.readlines():
            data = line.strip('\n')
            data = data.split(' ')
            temp_path.append(data)
        path.append(temp_path)
        file_handle.close()

def cal_max_hop(networkpath):
    flow_max_hop = 0 #记录所有数据流中，最长的一条数据流的跳数
    total_hop = 0 #记录所有数据流的跳数的总和
    for i in range(len(networkpath)):
        for j in networkpath[i]:
            if (len(j)-1) > flow_max_hop:
                flow_max_hop = len(j) - 1
            total_hop = total_hop + len(j) - 1
    return [flow_max_hop,total_hop]

if __name__ == '__main__':
    path = []
    N = 3
    file = "new_path"
    read_flow_path(file)
    init_flow_num = 5
    Step = 5
    C = 6
    #divide_channel = [9.0, 12.0, 16.0, 18.0, 23.0, 28.0]
    #divide_slot = [15.0, 21.0, 31.0, 36.0, 39.0, 48.0] 好的一种方式
    divide_channel = [10.0, 16.0, 26.0, 34.0, 42.0, 54.0]
    divide_slot = [15.0, 27.0, 36.0, 46.0, 57.0, 71.0]
    mdcg = [7.0, 10.0, 13.0, 15.0, 17.0, 20.0]
    x = [i for i in range(15,105,15)]
    y1 = [i for i in mdcg]
    y2 = [i for i in divide_channel]
    y3 = [i for i in divide_slot]
    plt.rcParams['font.family'] = 'Times New Roman ,SimSun '
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.tick_params(axis='both', direction='in')
    ax.plot(x, y1, '^-',markerfacecolor='none', color='c', label='JCNS', linewidth=1)
    ax.plot(x, y2, 'o-',markerfacecolor='none', color='#FFA500', label='ANC', linewidth=1)
    ax.plot(x, y3, 's-',markerfacecolor='none', color='m', label='CSA', linewidth=1)
    dashed_line = (5, 2)  # 定义虚线样式为每段长度为5、间隔为2的虚线
    plt.grid(True, linestyle='--', linewidth=0.5, dashes=dashed_line)  # 添加虚线网格
    plt.legend()
    plt.xlabel('number of flows')
    plt.ylabel('superframe length (time-slot)')
    plt.savefig('D:\\论文资料\\网络共存论文资料\\新的实验结果\\20240221\\random-delay.png', dpi=300,bbox_inches='tight')
    plt.show()
    hop_list = []
    for i in range(6):
        temp_path = [[],[],[]]
        for n in range(N):
            for j in range(init_flow_num + i * Step):
                temp_path[n].append(path[n][j])
        cur_hop = cal_max_hop(temp_path)
        hop_list.append(cur_hop[1])
    r1 = [hop_list[i] / (mdcg[i] * C) for i in range(len(hop_list))]
    r2 = [hop_list[i] / (divide_channel[i] * C) for i in range(len(hop_list))]
    r3 = [hop_list[i] / (divide_slot[i] * C) for i in range(len(hop_list))]
    plt.rcParams['font.family'] = 'Times New Roman ,SimSun '
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.tick_params(axis='both', direction='in')
    ax.plot(x, r1, '^-',markerfacecolor='none', color='c', label='JCNS', linewidth=1)
    ax.plot(x, r2, 'o-',markerfacecolor='none', color='#FFA500', label='ANC', linewidth=1)
    ax.plot(x, r3, 's-',markerfacecolor='none', color='m', label='CSA', linewidth=1)
    dashed_line = (5, 2)  # 定义虚线样式为每段长度为5、间隔为2的虚线
    plt.grid(True, linestyle='--', linewidth=0.5, dashes=dashed_line)  # 添加虚线网格
    plt.legend()
    plt.xlabel('number of flows')
    plt.ylabel('Resource utilization rate')
    plt.savefig('D:\\论文资料\\网络共存论文资料\\新的实验结果\\20240221\\random-resource.png', dpi=300,
                bbox_inches='tight')
    plt.show()
