# # 导入数据处理的包
# # from pyecharts.charts import Line
# # from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
# # import json
# #
# # # 打开文件
# # file_us = open("美国.txt", "r", encoding="UTF-8")
# # file_jp = open("日本.txt", "r", encoding="UTF-8")
# # file_in = open("印度.txt", "r", encoding="UTF-8")
# #
# # # 读文件
# # us_data = file_us.read()
# # jp_data = file_jp.read()
# # in_data = file_in.read()
# #
# # # 规整文件内容
# # us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# # jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
# # in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# #
# # us_data = us_data[:-2:]
# # jp_data = jp_data[:-2:]
# # in_data = in_data[:-2:]
# #
# # # json 转化为字典
# # us_data = json.loads(us_data)
# # jp_data = json.loads(jp_data)
# # in_data = json.loads(in_data)
# #
# # # 得到trend数据
# # us_trend_data = us_data["data"][0]["trend"]
# # jp_trend_data = jp_data["data"][0]["trend"]
# # in_trend_data = in_data["data"][0]["trend"]
# #
# # # 得到x轴的数据(x轴是2020全年)
# # us_x_data = us_trend_data["updateDate"][:314]
# # jp_x_data = jp_trend_data["updateDate"][:314]
# # in_x_data = in_trend_data["updateDate"][:314]
# #
# # # 得到y轴的数据(y轴数据是三个国家的数据)
# # us_y_data = us_trend_data["list"][0]["data"][:314]
# # jp_y_data = jp_trend_data["list"][0]["data"][:314]
# # in_y_data = in_trend_data["list"][0]["data"][:314]
# #
# # # 开始绘图
# # # 创建一个图
# # line = Line()
# #
# # # 创建图的x轴
# # line.add_xaxis(us_x_data)
# #
# # # 创建图的y轴
# # line.add_yaxis("美国确诊人数是", us_y_data, label_opts=LabelOpts(is_show=False))
# # line.add_yaxis("日本的确诊人数是", jp_y_data, label_opts=LabelOpts(is_show=False))
# # line.add_yaxis("印度的确诊人数是", in_y_data, label_opts=LabelOpts(is_show=False))
# #
# # # 配置图的全局设置
# # line.set_global_opts(
# #     title_opts=TitleOpts(title="2020年美国、日本、印度新冠日感染人数", pos_left="center", pos_bottom="1%"),
# #     legend_opts=LegendOpts(is_show=True),
# #     toolbox_opts=ToolboxOpts(is_show=True),
# #     visualmap_opts=VisualMapOpts(is_show=True)
# # )
# #
# # # 生成图
# # line.render()
# #
# # # 关闭文件
# # file_us.close()
# # file_jp.close()
# # file_in.close()
#
#
# # 导入要用到的包
# import json
# from pyecharts.charts import Line
# from pyecharts.options import LabelOpts, TitleOpts, ToolboxOpts, VisualMapOpts, LegendOpts
#
# # 读文件
# file_us = open("美国.txt", "r", encoding="UTF-8")
# file_jp = open("日本.txt", "r", encoding="UTF-8")
# file_in = open("印度.txt", "r", encoding="UTF-8")
# us_data = file_us.read()
# jp_data = file_jp.read()
# in_data = file_in.read()
#
# # 读取完毕,关闭文件
# file_us.close()
# file_jp.close()
# file_in.close()
#
# # 规整文件内容
# us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
# in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# us_data = us_data[:-2:]
# jp_data = jp_data[:-2:]
# in_data = in_data[:-2:]
#
# # json转化为字典
# us_data = json.loads(us_data)
# jp_data = json.loads(jp_data)
# in_data = json.loads(in_data)
#
# # 得到每个国家的trend
# us_trend = us_data["data"][0]["trend"]
# jp_trend = jp_data["data"][0]["trend"]
# in_trend = in_data["data"][0]["trend"]
#
# # 得到x轴内容
# us_x = us_trend["updateDate"][:314:]
# jp_x = jp_trend["updateDate"][:314:]
# in_x = in_trend["updateDate"][:314:]
#
# # 得到y轴内容
# us_y = us_trend["list"][0]["data"][:314:]
# jp_y = jp_trend["list"][0]["data"][:314:]
# in_y = in_trend["list"][0]["data"][:314:]
#
# #开始画线
# line = Line()
#
# # 创建x轴
# line.add_xaxis(us_x)
#
# # 创建y轴
# line.add_yaxis("美国确诊新冠的人数", us_y, label_opts=LabelOpts(is_show=False))
# line.add_yaxis("日本确诊新冠的人数", jp_y, label_opts=LabelOpts(is_show=False))
# line.add_yaxis("印度确诊新冠的人数", in_y, label_opts=LabelOpts(is_show=False))
#
# # 调整全局设置
# line.set_global_opts(
#     title_opts=TitleOpts(title="2020年美国、日本、印度每日确诊新冠人数", pos_left="center", pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
#
# # 生成图
# line.render()




