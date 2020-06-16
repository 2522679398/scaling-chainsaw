#coding:utf-8
"""
综合项目:世行历史数据基本分类及其可视化
作者：李嘉行
日期:2020.06.10
"""

import csv
import math
import pygal
import pygal_maps_world  #导入需要使用的库


def read_csv_as_nested_dict(filename, keyfield, separator, quote): #读取原始csv文件的数据，格式为嵌套字典
    """
    输入参数:
      filename:csv文件名
      keyfield:键名
      separator:分隔符
      quote:引用符

    输出:
      读取csv文件数据，返回嵌套字典格式，其中外层字典的键对应参数keyfiled，内层字典对应每行在各列所对应的具体值
    """
    result={}

    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row

    return result

def reconcile_countries_by_name(plot_countries, gdp_countries): #返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
    """
    输入参数:
    plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
    gdp_countries:世行各国数据，嵌套字典格式，其中外部字典的键为世行国家代码，值为该国在世行文件中的行数据（字典格式)

    输出：
    返回元组格式，包括一个字典和一个集合。其中字典内容为在世行有GDP数据的绘图库国家信息（键为绘图库各国家代码，值为对应的具体国名),
    集合内容为在世行无GDP数据的绘图库国家代码
    """

    # 不要忘记返回结果
    
    set1= set()
    dict1={}
    for k,v in plot_countries.items():#分别取出代码和国家名称
        if v in gdp_countries:#如果字典中含有国家
            dict1[k] = plot_countries[k]#输入字典
        else:
            set1.add(k)#如果不含有则输入集合
    tuple1 = tuple([dict1,set1])
    return tuple1#返回元组

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    输入参数:
    gdpinfo: gdp信息字典
    plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
    year: 具体年份值

    输出：
    输出包含一个字典和二个集合的元组数据。其中字典数据为绘图库各国家代码及对应的在某具体年份GDP产值（键为绘图库中各国家代码，值为在具体年份（由year参数确定）所对应的世行GDP数据值。为
    后续显示方便，GDP结果需转换为以10为基数的对数格式，如GDP原始值为2500，则应为log2500，ps:利用math.log()完成)
    2个集合一个为在世行GDP数据中完全没有记录的绘图库00国家代码，另一个集合为只是没有某特定年（由year参数确定）世行GDP数据的绘图库国家代码
    """

    a=read_csv_as_nested_dict(gdpinfo['gdpfile'], gdpinfo['country_name'], gdpinfo['separator'],gdpinfo['quote'])
    dict1={}             
    b,c=reconcile_countries_by_name(plot_countries,a)       
    set1=set()     
    dict2={}
    for n in a.values():
        i=dict(zip(n.keys(), n.values()))#将有数值的存放在dict2中
        dict2[i['Country Name']]=i
    for code, country in b.items():#取出国家代码和名称
        if country in dict2.keys():#判断是否有数值
            yg=dict2[country][str(year)]#判断是否当年存在数值
            if yg :
                dict1[code]=math.log10(float(yg))    #利用math.log()将GDP结果转换为以10为基数的对数格式并存入字典中
            else:
                set1.add(code) 
    
    tuple2= tuple([dict1,c ,set1])
    return tuple2

def render_world_map(gdpinfo, plot_countries, year, map_file): #将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
    """

      gdpinfo:gdp信息字典
      plot_countires:绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
      year:具体年份数据，以字符串格式程序，如"1970"
      map_file:输出的图片文件名

    目标：将指定某年的世界各国GDP数据在世界地图上显示，并将结果输出为具体的的图片文件
    提示：本函数可视化需要利用pygal.maps.world.World()方法
    """

    A_countries,B_countries,C_countries = build_map_dict_by_name(gdpinfo, plot_countries, year)#三种国家
    worldmap_chart = pygal.maps.world.World()#构建地图
    worldmap_chart.title = '世界银行%d年国家GDP数据'%float(year)#标题
    worldmap_chart.add('该年在绘图库及世行有数据的国家及其GDP数据', A_countries)
    worldmap_chart.add('在绘图库中没有数据的国家',B_countries)
    worldmap_chart.add('该年在世行没有GDP数据的国家',C_countries)
    worldmap_chart.render()
    worldmap_chart.render_to_file(map_file)

def test_render_world_map(year):  #测试函数
    """
    对各功能函数进行测试
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    } #定义数据字典
    
    
    
    pygal_countries = pygal.maps.world.COUNTRIES   # 获得绘图库pygal国家代码字典

    # 测试时可以1970年为例，对函数继续测试，将运行结果与提供的svg进行对比，其它年份可将文件重新命名
    render_world_map(gdpinfo, pygal_countries, year, "isp_gdp_world_name_%d.svg"%float(year))


#程序测试和运行
print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year=input("请输入需查询的具体年份:")

while float(year) < 1960 or float(year) > 2015 :#判断年份是否符合范围
    print('对不起，不能查询到该年的数据')
    print('---------------------------')
    year=input("请输入需查询的具体年份:")
else :
    test_render_world_map(year)
