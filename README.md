# burp_intruder_result_payload
如何将Burpsuite的intruder的payload导出来，几句python就可以，当利用burpsuite爆破出用户名或者其他关键信息时，可以利用python去摘取。
比如mobile参数是我们的目标
![image](https://user-images.githubusercontent.com/63894044/146546842-321058ff-5e25-44a8-b87d-5d7e6951ec36.png)
可以先将intruder结果保存至本地
![image](https://user-images.githubusercontent.com/63894044/146547027-b64c2393-52ae-463e-a68c-19efeac30f0f.png)
python burp_intruder_result_payload.py 参数 burp保存的文件
<img width="1106" alt="图片1" src="https://user-images.githubusercontent.com/63894044/146546675-307bb31f-b31a-4ff2-8b84-7e28e91a9d71.png">
