from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=100, width=500,
           sizing_mode='scale_width', title="Motion Graph")
p.yaxis.minor_tick_line_color = None  # 去掉y轴的标签
p.yaxis.ticker.desired_num_ticks = 1  # 去掉y轴中的虚线

hover = HoverTool(
    tooltips=[("Start", "@Start_String"), ("End", "@End_String")])  # 悬停
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0,
           top=1, color="green", source=cds)  # 做一个直方图quad

output_file("5_app2 webcamCtrlAndObjectsDetect\plotting.pyGraph2.html")
show(p)
