# GoOutOfNjupt

> 一次性高批量申请离校: NJUPT

采用Github Action执行， 只需将代码Fork到自己仓库，然后设置Secrets值，再开启workflow就行了

需要的Secrets值为:
- UserID
- JSESSIONID
- PortalToken
- days      # 设置需要申请的天数, 这个是根据自己的需求填的

进入 http://bsdtlc.njupt.edu.cn/StartWorkflow?Workflow=WF_XSCXSQ 打开浏览器的开发者工具查询cookies填入即可

操作教程见： https://github.com/Freedomisgood/wyycg-autocheckin

![](./pics/20210319140834.jpg)