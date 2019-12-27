## 教育研究方法网站爬题脚本

- 使用环境

  ```
  python3.0+
  配置MySQL数据库
  ```

- python库安装

  ```
  requirements.txt
  ```

- 使用方法

1. F12打开控制台查看当前的cookie和URL

   ![](/img/1.png)

2. 替换save_problem.py中的cookie和URL

![](/img/2.png)

3. 运行脚本成功成功爬取网站题目，并插入数据库

![](/img/3.png)

4. 使用select_to_save.py将数据库中的题库查询出来并保存到TXT文本里面