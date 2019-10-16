# BNU Network keep online
## 项目需求

最近1年以来，师大网关默认一段时间之后就会被信息网络中心切断（间隔约4小时无响应）。这对长时间下载数据及需要网络的人物极其不友好，因此寻求通过一种途径使得网络保持internet持续在线。

## 功能介绍
本工具通过python3,使得bnu登录网关保持持续在线。默认网络状态查询间隔60秒（每1分钟检查一次，减少信息网络中心负担）
## 工具依赖项
> python，版本要求3.x（推荐**3.6**及以后版本）
> 第三方依赖库**requests**
## 各文件说明
|文件名|用途|
|--|--|
| bnu.network.userinfo | 存储网关登录信息 |
| bnu.network.connect.py | 用于连接网关 |
| bnu.network.disconnect.py | 用于断开网关连接 |
| add_to_system_service | 添加为系统服务的工具 |

## 使用方法

> python3 bnu.network.connect.py       

> python3 bnu.network.disconnect.py     

## 附加说明
将此段代码加入开启启动服务，可以做到开机自动连接网络，并保持登录状态（^_^）。
> windows下推荐使用[winsw,使用方法详见](https://github.com/kohsuke/winsw/blob/master/doc/installation.md)

> Linux下可将系统命令写到系统启动服务（service），详细请Google/Baidu关键字"Linux Systemd"

注:"add_to_system_service" 目录下提供了windows/Linux系统下的工具模板，请自行定制
