信安大赛源码(有模型)
===

# 说明
本项目属于深度学习类项目，可执行文件配置过大，并且`transformers`包配置不正确，因此本小组放弃了对可执行文件的打包，改为选择使用了一个入口文件进行运行。您只需要运行文件中的**main.py**即可运行成功，具体配置过程可阅读下面文档内容。如需知道具体的成果，可以观看目录中的成果演示视频，里边有详细的解说供您参考。

## 环境配置
### 利用`pip install -r requirements.txt`命令，将根目录中的**requirement.txt**即项目所需要的库以及依赖进行安装

*模型位于 [https://gitee.com/wxh1015/model](https://gitee.com/wxh1015/model) 链接处，在本文档中已经帮您下载完毕，您无需继续下载，下载完整个内容后，请将四个压缩包置于根目录中，再将所有的压缩包进行解压，解压时仅选择解压到当前文件夹，以防止位置不正确造成程序运行错误*

*如果配置clip中出现问题，可以直接在`./clip-install`文件夹中运行 `python setup.py install`*

## 如何运行

根目录文件夹下的**main.py**是项目的入口文件，该项目只需要运行main.py即可

## 启动main.py后项目会干什么？
1. 项目会首先打开微博账号，利用爬虫进行正常微博账号的运行，包括自动点赞、转发、抓取新闻，生成摘要再进行发送等一系列正常操作。
2. 您可以手动更改根目录下`./bit_steam/bit_stream.txt`的内容，自行确定需要隐写的内容。
3. 项目可以将需要隐写的内容嵌入到`./images`文件夹中的图片所生成的描述性文字中，并将其发送到微博。

#### 通过以上操作我们可以实现秘密的传输我们需要的信息在微博中，并且由于我们之前维护了一个正常的社交机器人，因此我们的隐写信息混淆在正常发送的信息中，从而造成一定的不可区分性。

## 备注
 
**本次实验的微博账号昵称：端庄的厄耳**

由于微博cookie的不断变化，爬虫的可行性需要不断更新根目录下`./crawler`中的 **cookie** 来保证，如需验证程序可行性时产生问题，请联系 ***QQ：390160845*** ，届时将会为您更新新的cookie。我们为给您带来的不便深表歉意。