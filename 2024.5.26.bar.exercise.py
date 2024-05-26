# # 导入包
# from pyecharts.charts import Bar, Timeline
# from pyecharts.options import LabelOpts, TitleOpts
# from pyecharts.globals import ThemeType
#
# # 从文件中读取信息
# GDP_file = open("1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# GDP_data = GDP_file.readlines()
#
# # 关闭文件
# GDP_file.close()
#
# # 规整文件
# GDP_data.pop(0)
#
# # 定义一个字典来存文件
# GDP_dict = {}
# for line_data in GDP_data:
#     GDP_year = int(line_data.split(",")[0])
#     GDP_country = line_data.split(",")[1]
#     GDP = float(line_data.split(",")[2])
#     try:
#         GDP_dict[GDP_year].append([GDP_country, GDP])
#     except KeyError:
#         GDP_dict[GDP_year] = []
#         GDP_dict[GDP_year].append([GDP_country, GDP])
#
# # 创建时间线(并且设置其主题)
# GDP_line = Timeline({"theme": ThemeType.ROMA})
#
# # 排序数据对象
# sort_years = sorted(GDP_dict.keys())
#
# for year in GDP_dict:
#     GDP_dict[year].sort(key=lambda element: element[1], reverse=True)
#     year_data = GDP_dict[year][:8:]
#     x_data = []
#     y_data = []
#     # 为x,y准备数据
#     for country_data in year_data:
#         x_data.append(country_data[0])
#         y_data.append(country_data[1] / 100000000)
#     # 建立柱状图
#     GDP_bar = Bar()
#     x_data.reverse()
#     y_data.reverse()
#     GDP_bar.add_xaxis(x_data)
#     GDP_bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
#
#     # 反转x-y轴
#     GDP_bar.reversal_axis()
#
#     # 设置每一年的标题
#     GDP_bar.set_global_opts(
#         title_opts=TitleOpts(title=f"{year}年全球前八国家的GDP")
#     )
#
#     # 创建时间线
#     GDP_line.add(GDP_bar, str(year))
#
# # 调整时间轴播放
# GDP_line.add_schema(
#     play_interval=3000,  # 时间移动的时间
#     is_timeline_show=True,  # 展示时间线
#     is_auto_play=True,  # 自动播放
#     is_loop_play=True  # 循环播放
# )
#
# # 生成柱状图
# GDP_line.render("1960-2019年全球GDP top8变化图(new).html")

# 导入包
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ThemeType

# 从文件中得到GDP数据
GDP_file = open("1960-2019全球GDP数据.csv", "r", encoding="GB2312")
GDP_data = GDP_file.readlines()

# 关闭文件
GDP_file.close()

# 规整数据
GDP_data.pop(0)

# 创建GDP字典,便于读数据
GDP_dict = {}

# 为字典读数据
for line in GDP_data:
    year = int(line.split(",")[0])  # 得到年份数据
    country = line.split(",")[1]  # 得到国家数据
    GDP = float(line.split(",")[2])  # 得到GDP数据
    # 每一年的第一个数据进入字典的时候是没有列表的,所以说要先try一下
    try:
        GDP_dict[year].append([country, GDP])  # 假如列表已经存在,则可以直接append
    except KeyError:
        GDP_dict[year] = []  # 假如列表不存在,则先创造再添加
        GDP_dict[year].append([country, GDP])

# 排序年份
sort_year = sorted(GDP_dict.keys())

# 创建时间线(并且对其进行初始设置)
GDP_timeline = Timeline({"theme": ThemeType.CHALK})

# 准备创造柱状图
for year in GDP_dict:
    GDP_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = GDP_dict[year][:8:]
    x_data = []
    y_data = []
    for country in year_data:
        x_data.append(country[0])
        y_data.append(country[1] / 100000000)

    # 创建柱状图
    GDP_bar = Bar()
    x_data.reverse()
    y_data.reverse()
    GDP_bar.add_xaxis(x_data)
    GDP_bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))

    # 反转x-y轴
    GDP_bar.reversal_axis()

    # 设置每年的标题
    GDP_bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP排名前八国家")
    )

    # 时间线增加
    GDP_timeline.add(GDP_bar, str(year))

# 设置时间线
GDP_timeline.add_schema(
    play_interval=3000,  # 时间移动的时间
    is_timeline_show=True,  # 展示时间线
    is_auto_play=True,  # 自动播放
    is_loop_play=True  # 循环播放
)

# 生成柱状图
GDP_timeline.render("1960-2019年全球GDP top8变化图(mine).html")














