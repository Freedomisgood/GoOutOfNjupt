

import requests
import pendulum
import re
import sys
import os

# TODO: 进入 http://bsdtlc.njupt.edu.cn/StartWorkflow?Workflow=WF_XSCXSQ 查询cookies填入即可
# cookies = {
#     'UserID': 'B17050322',
#     'JSESSIONID': '#',
#     'PortalToken': '#..',
# }

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://bsdtlc.njupt.edu.cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://bsdtlc.njupt.edu.cn/StartWorkflow?Workflow=WF_XSCXSQ',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}



def auto_apply(
            t: int, 
            c: dict,
            contact_person,
            contact_person_phonenum,
            your_phonenum,
            apply_reason
    ):
    params = (
        ('Workflow', 'WF_XSCXSQ'),
    )
    response = requests.get('http://bsdtlc.njupt.edu.cn/StartWorkflow', 
            headers=headers, 
            params=params, 
            cookies=c
        )
    content = response.text
    res = re.search("Token=(.*?)&WorkID=(.*?)&", content)
    token, work_id = res.group(1), res.group(2)

    params = (
        ('operate', 'WorkAction.4'),
        ('WorkActionID', '4'),
        ('Table', 'WF_XSCXSQ'),
        ('Token', f'{token}'),
        ('WorkID', f'{work_id}'),
        ('StepID', 'initialStep'),
        ('', ''),
        ('isSubmit', '1'),
    )

    data = {
        'operate': 'Add',
        '$C{sqr}': '0',
        'sqr': '34163',
        '$C{xh}': '0',
        '$C{xy}': '0',
        'xy': '305000',
        '$C{zy}': '0',
        'zy': '228',
        '$C{BJ}': '0',
        'BJ': '2665',
        '$C{lxdh}': '1',
        'lxdh': f'{your_phonenum}',
        '$C{qjdmc}': '0',
        '$C{sqsj}': '0',
        'sqsj': f'{t.to_datetime_string()}',
        '$C{jhcxrq}': '3',
        'jhcxrq': f'{t.to_date_string()}',
        '$C{jhfxrq}': '3',
        'jhfxrq': f'{t.to_date_string()}',
        '$C{mdd}': '2',
        'mdd': '1',
        '$C{cxsy}': '7',
        'cxsy': apply_reason,
        '$C{jjlxr}': '1',
        'jjlxr': contact_person,
        '$C{jjlxrdh}': '1',
        'jjlxrdh': contact_person_phonenum
    }
    response = requests.post('http://bsdtlc.njupt.edu.cn/OperateProcessor', headers=headers, params=params,
                             cookies=c, data=data)
    print(t.to_date_string() + "申请结果为: ", response.status_code)
    print(t.to_date_string() + "申请结果为: ", response.text)



if __name__ == "__main__":
    params = sys.argv
    len_p = len(params)
    if len_p != 10:
        print(f"参数个数不正确， 请检验是否缺少Secrets必要参数, 当前数量为{len_p-1}")
        os._exit(1)
        
    if not params[4].isdecimal():
        os._exit(1)
    cookies = {
        'UserID': params[1],
        'JSESSIONID': params[2],
        'PortalToken': params[3],
        "route": params[9],
        "TodoTasks.Group": "Workflow"
    }

    days = params[4]
    contact_person = params[5] 
    contact_person_phonenum = params[6]
    your_phonenum = params[7] 
    apply_reason = params[8] 

    print(params)

    n_day = pendulum.now()
    for i in range(int(days)):
        n_day = n_day.add(days=1)

        auto_apply(
            n_day, 
            cookies,
            contact_person,
            contact_person_phonenum,
            your_phonenum,
            apply_reason
        )
