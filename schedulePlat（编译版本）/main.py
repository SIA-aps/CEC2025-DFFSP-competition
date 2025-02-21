import os,time
from APS.algorithm.shcedulingforCEC import DffspForCEC
from APS import dffspCEC

if __name__ == '__main__':

    #TODO 读取案例文件，生成排产模型
    case_path = os.path.join('Competition case', 'num30_scenario_0.txt')
    # 打印当前工作目录和文件路径，以便调试
    print("当前工作目录是:", os.getcwd())
    print("尝试打开的文件路径是:", case_path)
    # 读取实例数据
    instance = dffspCEC.DFFSP()
    # 读取测试用例
    instance.loadTestFile(case_path)
    # 生成需要的info
    info = instance.generateInfo()
    start_time = time.time()

    #TODO 读取编码文件，进行排程
    file_path = os.path.join('ending_log.txt')
    lines_as_lists = []
    # 打开文件进行读取
    with open(file_path, "r") as file:
        for line in file:
            # 去掉行尾的换行符并将该行转换为列表（假设按空格或其他分隔符分割）
            line_list = [int(item) if item != "Null" else item for item in line.strip().split(",")]
            # 添加到结果列表
            lines_as_lists.append(line_list)
    #TODO 排程
    DffspForCEC(info,lines_as_lists)
    end_time = time.time()
    print(f"运行时间: {end_time - start_time:.2f} 秒")


