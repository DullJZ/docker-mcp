# Docker-MCP

[English](README.md) | 简体中文

Docker-MCP 是一个基于[Docker Manager](https://github.com/DullJZ/docker-manager)的MCP服务器，使用FastMCP框架在Docker Manager的API接口之上构建，提供了对Docker容器的管理功能。

## 开始使用

推荐使用uv工具管理依赖

```bash
pip install uv
source venv/bin/activate
uv run install
```

修改`docker.py`中Docker Manager的API地址和鉴权Token

```python
base_url = 'YOUR_DOCKER_MANAGER_BASE_URL'
token = 'YOUR_DOCKER_MANAGER_API_TOKEN'
```

然后运行

```bash
bash start.sh
```

## 工具列表

| 工具名称 | 功能 |
| -------- | ---- |
| pull_image | 拉取指定镜像 |
| list_images | 列出所有镜像 |
| create_container | 创建容器 |
| run_container_by_compose | 通过compose文件运行容器 |
| fetch_container_logs | 获取容器日志 |
| stop_container | 停止容器 |
| start_container | 启动容器 |
| restart_container | 重启容器 |
| remove_container | 删除容器 |
| fetch_container_info | 获取容器信息 |
| create_exec_session | 创建交互式shell会话 |
| execute_command_in_session | 在会话中执行命令 |
| close_exec_session | 关闭交互式shell会话 |
| get_more_session_output | 获取更多会话输出 |
| wait_for_seconds | 等待指定秒数 |
| create_network | 创建Docker网络 |
| delete_network | 删除Docker网络 |
| list_networks | 列出所有Docker网络 |
| network_info | 获取网络信息 |
| connect_network | 容器连接到网络 |
| disconnect_network | 容器断开网络 |