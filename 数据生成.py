import random
import string

from faker import Faker
import csv
import time
import threading

# 定义全局变量
fake = Faker(locale='zh_CN')
lock = threading.Lock()
sex = ['男', '女']
education = ['小学', '初中', '高中', '本科', '硕士']
risk_level = ["低", "中", "高"]
fund_type = ["股票型", "混合型", "债券型", "指数型", "FOF型", "QDLL型", "货币型"]
premium = ["0.001", "0.0015", "0.015"]
risk = ["r1", "r2", "r3", "r4", "r5"]

fund_name = ["华宝沪深300指数增强A", "嘉实中证50OETF联接A", "招商中小板指数分级", "银华新兴成长混合", "鹏华沪深300股票",
             "华富中证100指数", "国投瑞银中证全指可选消费ETF",
             "汇忝富货币A", "华夏上证5OETF联接A", "易方达消费行业混合", "民生加银中证5O0指数A", "招商中小板策路混合",
             "景顺长城中证50OETF联接A", "国泰华夏科技创新混合",
             "银华永续纯债A", "景倾长城核心成长混合", "富国中证基本面50指数A", "嘉实沪深30O指数增强",
             "泰达宏利精选混合", "华安标普500指数增强A", "易方达收益增强混合",
             "博时盛世债券A", "国投瑞银纳指中国消费ETF", "易方达核心优选混合", "华安中证5OO指数", "华夏上证180ETF联接A",
             "招商中证医药100", "南方中证5O0指数", "华宝湾湾深10指数A",
             "易方达中证红利旨数交易型", "中海稳健增利混合", "嘉实高端装备制造业指数A", "招商MSCI中国A指数ETF",
             "南方品质消费混合", "国投瑞银中证红利指数ETF", "博时新动力混合",
             "华宝深证400指数", "德邦收益增强混合", "华宝纳指中国消费ETF", "东吴恒生国企指数",
             "国联安标普金融行业指数A", "长盛聚鑫纯债A", "易方达360行业指数分级", "鹏华中证煤炭指数",
             "国投瑞银中证军工指数ETF", "国海富兰克林沪深300指数", "国金中小板指数A", "长盛多策略灵活配置混合",
             "华夏上证180等权重指数A", "富国天惠灵活配置混合", "工银新能源产业混合",
             "国投瑞银上证5OETF联接A", "国投瑞银中证100指数ETF", "国泰沪深300指数增强", "南方医药行业A", "东方明珠混合",
             "国投瑞银可选消费ETF", "中欧安瑞混合", "华宝核心优选混合",
             "国投瑞银中证500ETF联接A", "富国中小盘精选混合", "招商中小板指数增强A", "多利优选混合",
             "国投瑞银中证消费行业ETF", "国海富兰克林沪深30ETF联接A", "景顺长城核心低波动混合",
             "招商移动互联网混合", "华宝中小板指数", "易方达中证智能家居指数A", "招商中证养老产业指数",
             "富国中证全指医药ETF", "工银上证50增强", "景顺长城信用增强混合", "嘉实标普50等权重指数",
             "朋鹏鸣华创业板指娄数A", "华宝沪深300指数", "国泰核心优选混合", "国投瑞银新兴市场指数ETF",
             "嘉实消费行业混合", "华宝沪深300指数增强A", "国投瑞银中证全指责任投资ETF",
             "华夏上证5OETF联技", "嘉实低碳环保混合", "招商新动力混合", "华宝湾湾深100指数"]


def create_data(num, thread_id):
    """生成数据"""
    data = []
    for i in range(num):
        buy = random.randint(500, 20000)
        rate = fake.pyfloat(left_digits=1, right_digits=2, positive=False)
        sell = int(buy * (1 + rate / 100))

        data.append([i, fake.name(), random.choice(sex), str(random.randint(18, 70)), random.choice(education),
                     str(random.randint(1, 25)),
                     fake.job(), str(random.randint(8, 40)), random.choice(risk_level),
                     fake.date_between(start_date='-1y', end_date='today'), random.choice(fund_type),
                     random.choice(fund_name), random.choice(premium), rate,
                     str(random.randint(-10, 10)), buy, sell, str(random.randint(1, 5)), str(random.randint(0, 7)),
                     fake.date_between(start_date='-10y', end_date='-2y'),
                     fake.date_between(start_date='-15y', end_date='-7y'),
                     random.choice(risk), fake.company(), str(random.randint(5, 30)), str(random.randint(10, 90))])
    return data


def save_data(num, thread_id):
    """保存数据到csv文件中"""
    data = create_data(num, thread_id)
    filename = f"data_{time.strftime('%Y%m%d%H%M%S')}_{thread_id}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "sex", "age", "education", "femoral_age",
                         "occupation", "year_come", "risk_level",
                         "data", "fund_type", "fund_name", "premium", "rate",
                         "this_year", "buy", "sell", "cxrank", "dividends",
                         "data_fund", "data_company",
                         "risk", "company", "count_fund", "manage_scale"])
        for row in data:
            writer.writerow(row)
    with lock:
        print(f"Thread {thread_id} finished, data saved to {filename}")


def main():
    """主函数"""
    # 设置每个线程生成的数据量
    num_per_thread = 10000000
    # 设置线程数
    num_threads = 3
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=save_data, args=(num_per_thread, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("All threads finished")


if __name__ == "__main__":
    main()