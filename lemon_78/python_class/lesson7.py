"""



Python的项目实战

注意：Excel表格读取的数字---文本---字符串
eval():从字符串里面获取Python的表达式




"""
import requests,pprint,jsonpath
from python_class import lesson6 #导入

def execute_fun(filename,sheetname):
    cases = lesson6.read_data(filename,sheetname)  #调用读取数据的函数
    for case in cases:
        case_id = case.get("case_id")
        url = case.get("url")   #取url地址
        data = case["data"] #取测试参数
        data = eval(data) #转化为字典类型/从字符串里面获取Python表达式
        print(type(case_id))
        expected_result = eval(case.get("expected_result"))  #从字符串里面获取Python表达式---字典
        expected_msg = expected_result.get("msg")

        real_result = lesson6.func_api(url_api=url,data_api=data) #调用接口发送的参数
        real_msg = real_result.get("msg")
        print(type(case_id))
        print(expected_result)
        print(real_result)
        print("真实执行结果:{}".format(real_msg))
        print("预期执行结果:{}".format(expected_msg))
        if real_msg == expected_msg:
            final_result = "Passed"
            print("第{}条用例通过".format(case_id))
        else:
            final_result = "Failed"
            print("第{}条用例执行不通过".format(case_id))
        lesson6.write_data(filename,sheetname,final_result,case_id+1,8) #调用写入结果函数



if __name__ == '__main__':
    re = execute_fun("test_case_api.xlsx","login")
    print(re)






















