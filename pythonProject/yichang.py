# try:
#     f=open("C:\\eula.1028.txt","r")
#     f.read("222")
# except IOError:
#     print("读取文件时出现异常")
# except:
#     print("异常")
# else:
#     print("成功")
# import requests
# import json
# url = 'https://locallhost:8080/Easy/Login'
# data = 'loginName=admin&password=123456&action=login'
# # ('POST',url=url,params=data)
# req = requests.post(url,params=data)
# print(req.text)
# #print(json.dumps(req.json(),indent=4, ensure_ascii=False))
# import requests
# import json
# import jsonpath
#
# #生成token接口
# url = "http://localhost:8000/login"
# # python 字典 --》 json
# data = {
#     "username": "admin",
#     "password": "admin"
# }
# res = requests.post(url=url, json=data)
# #使用json包,打印json格式换行并且前面空四个空格，通过ascii防止乱码
# print(json.dumps(res.json(), indent=4, ensure_ascii=False))
# # 返回值是个列表 所以要加索引
# # print(jsonpath.jsonpath(res.json(), "$..token")[0])
#
# print("*************************************************************")
#
# #登录jwt接口
# urllogin = "http://localhost:8000/auth/hello"
# #使用jsonpath来提取
# token = "Bearer " + jsonpath.jsonpath(res.json(), "$..token")[0]
# headers = {
#     "Authorization":token
# }
# res1 = requests.get(url=urllogin,headers=headers)
# print(json.dumps(res1.json(), indent=4, ensure_ascii=False))
#
# print('************************************************************')
#
# #上传文件接口
# url = "http://httpbin.org/post"
# # 准备一个文件
# file = open("C:\\Users\\1\\Desktop\you.txt", "rb")
# # 参数
# files = {
#     "file": file
# }
# res2 = requests.post(url=url, files=files)
# #print(res.json())
# print(json.dumps(res2.json(), indent=4, ensure_ascii=False))

import requests
import json
import jsonpath
url = "http://locallhost:8000/login"
data ={
        "username":"admin",
        "password":"admin"
}
res = requests.post(url=url,json=data)
print(json.dump(res.json(),indent=4,ensure_ascii=False))
print("*************************************************")
# urllogin = "http://locahost:8000/auth/hello"
# token = "Bearer"+jsonpath.jsonpath(res.json(),"$..token")[0]
# headers={"Authorization":"token"}
# res1 = requests.get(url=urllogin,headers=headers)
# print(json.dump())
