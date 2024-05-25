#
# # 导入柱状图的包
# from pyecharts.charts import Bar
#
# # 创建一个柱状图
# bar1 = Bar()
# bar1.add_xaxis(["中国", "美国", "英国"])
# bar1.add_yaxis("1900年GDP总量", [10, 20, 30])
#
# # 生成图
# bar1.render()
#
# # 导入时间图的包
# from pyecharts.charts import Bar
# from pyecharts.options import VisualMapOpts
# from pyecharts.charts import Timeline
# from pyecharts.globals import ThemeType
#
# # 根据时间点创建多个坐标图
# bar1 = Bar()
# bar1.add_xaxis(["中国", "美国", "英国"])
# bar1.add_yaxis("GDP", [10, 20, 30])
#
# bar2 = Bar()
# bar2.add_xaxis(["中国", "美国", "英国"])
# bar2.add_yaxis("GDP", [40, 120, 85])
#
# bar3 = Bar()
# bar3.add_xaxis(["中国", "美国", "英国"])
# bar3.add_yaxis("GDP", [500, 600, 430])
#
# # 创建时间轴
# timeline = Timeline({"theme": ThemeType.LIGHT})
# timeline.add(bar1, "1900年GDP总量")
# timeline.add(bar2, "1949年GDP总量")
# timeline.add(bar3, "2024年GDP总量")
#
# # 调整时间轴播放
# timeline.add_schema(
#     play_interval=3000,
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=True
# )
#
# # 生成时间轴图
# timeline.render("从清朝到现在的三国GDP变化.html")


# 最后一舞(1960-2019年全球GDP top8变化图)
# 导包
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ThemeType

# 读取数据文件信息
GDP_f = open("1960-2019全球GDP数据.csv", "r", encoding="GB2312")
GDP_data = GDP_f.readlines()  # GDP_data 是列表

# 关闭文件
GDP_f.close()

# 规整数据文件信息
GDP_data.pop(0)

# 定义一个字典来存储数据
GDP_data_dict = {}
for line in GDP_data:
    year = int(line.split(",")[0])  # 得到年份
    country = line.split(",")[1]  # 得到国家
    GDP = float(line.split(",")[2])  # 得到GDP(因为有些数字是科学计数法,所以说转化为float来用)
    try:
        GDP_data_dict[year].append([country, GDP])
    except KeyError:
        GDP_data_dict[year] = []
        GDP_data_dict[year].append([country, GDP])

# 构建timeline对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序数据对象
sort_year = sorted(GDP_data_dict.keys())

for years in sort_year:
    GDP_data_dict[years].sort(key=lambda element: element[1], reverse=True)
    year_data = GDP_data_dict[years][0:8]  # 只取得某一年中GDP前八的国家
    x_data = []
    y_data = []
    for country_gdp in year_data:     # 从GDP前8的国家里面再取，作为柱状图的x-y轴
        x_data.append(country_gdp[0])  # 国家名字
        y_data.append(country_gdp[1] / 100000000)  # 国家当年的GDP

    # 建立柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))

    # 反转x-y轴
    bar.reversal_axis()

    # 设置每一年的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{years}年全球前八国家的GDP")
    )

    # 创建时间线
    timeline.add(bar, str(years))  # 添加一个时间线

# 调整时间轴播放
timeline.add_schema(
    play_interval=3000,  # 时间移动的时间
    is_timeline_show=True,  # 展示时间线
    is_auto_play=True,  # 自动播放
    is_loop_play=True  # 循环播放
)

# 生成柱状图
timeline.render("1960-2019年全球GDP top8变化图.html")

