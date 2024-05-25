# # 导入地图构建使用的包
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
#
# # 创建一个地图
# China_map = Map()
#
# # 给地图准备数据
# data = [
#     ("北京市", 100),
#     ("上海市", 95),
#     ("深圳市", 90),
#     ("重庆市", 80),
#     ("四川省", 15)
# ]
#
# # 给地图添加数据
# China_map.add("中国城市发展地图", data, "china")
#
# # 设置全局变量
# China_map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min": 1, "max": 19, "label": "1-19", "color": "#CCFFFF"},
#             {"min": 20, "max": 39, "label": "20-39", "color": "#FFFF99"},
#             {"min": 40, "max": 59, "label": "40-59", "color": "#FF9966"},
#             {"min": 60, "max": 79, "label": "60-79", "color": "#FF6666"},
#             {"min": 80, "max": 100, "label": "80-99", "color": "#CC3333"}
#         ]
#     )
# )
#
# # 生成地图
# China_map.render()


# # 导入疫情地图需要的包
# import json
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
#
# # 打开需要的数据文件
# China_map = open("疫情.txt", "r", encoding="UTF-8")
# Ch_map = China_map.read()
#
# # 关闭文件
# China_map.close()
#
# # 得到所有地区数据
# area_map = json.loads(Ch_map)
# area_map = area_map["areaTree"][0]["children"]
#
# # 将数据成对封装成元组,然后再将元组封装至列表中,然后用列表给地图提供数据
# China_list = []
# for province in area_map:
#     province_name = province["name"] + "省"
#     province_confirm = province["total"]["confirm"]
#
#     China_list.append((province_name, province_confirm))
#
# # 创建一个疫情地图
# China_Map = Map()
#
# # 为疫情地图加入数据
# China_Map.add("中国全国新冠确诊人数图", China_list, "china")
#
# # 为疫情地图调整全局设置,使得更加美观
# China_Map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min": 1, "max": 99, "label": "1-99人确诊", "color": "#CCFFFF"},
#             {"min": 100, "max": 1999, "label": "100-1999人确诊", "color": "#FFFF99"},
#             {"min": 2000, "max": 9999, "label": "2000-9999人确诊", "color": "#FF9966"},
#             {"min": 10000, "max": 39999, "label": "10000-39999人确诊", "color": "#FF6666"},
#             {"min": 40000, "label": "40000人以上确诊", "color": "#CC3333"}
#         ]
#     )
# )
#
# # 生成疫情地图
# China_Map.render()

# 导入生成重庆疫情地图的包
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 读数据文件
cq_file = open("疫情.txt", "r", encoding="UTF-8")
cq_data = cq_file.read()

# 关闭文件
cq_file.close()

# 将数据定位到重庆
cq_data = json.loads(cq_data)
cq_data = cq_data["areaTree"][0]["children"][18]["children"]

# 将区县名字取出,和每个区县的确诊人数构成元组存入列表
cq_list = []
for area in cq_data:
    area_name = area["name"]
    area_confirm = area["total"]["confirm"]
    cq_list.append((area_name, area_confirm))

# 创造一个地图
cq_map = Map()

# 向重庆疫情地图中加入值
cq_map.add("重庆新冠确诊人数图", cq_list, "重庆")

# 调整重庆疫情地图的全局设置(主要是改变颜色)
cq_map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人确诊", "color": "#FFFF99"},
            {"min": 10, "max": 19, "label": "10-19人确诊", "color": "#FF9966"},
            {"min": 20, "max": 29, "label": "20-29人确诊", "color": "#FF6666"},
            {"min": 30, "label": "30人以上确诊", "color": "#CC3333"},
        ]
    )
)

# 生成重庆的疫情地图
cq_map.render()




















