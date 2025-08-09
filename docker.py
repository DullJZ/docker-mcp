import asyncio
import json
import httpx
from fastmcp import FastMCP

base_url = 'YOUR_DOCKER_MANAGER_BASE_URL'
token = 'YOUR_DOCKER_MANAGER_API_TOKEN'

# 初始化 FastMCP 服务器
app = FastMCP('docker')

@app.tool()
def pull_image(image_name: str):
    """
    从指定的远程地址拉取镜像。
    参数：image_name（字符串）：镜像名称
    返回：镜像详细信息和 status
    """
    url = f'{base_url}/api/pull_image'
    response = httpx.post(url, json={'image_name': image_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def list_images():
    """
    列出所有镜像。
    参数：无
    返回：镜像详细信息和 status
    """
    url = f'{base_url}/api/list_images'
    response = httpx.post(url, headers={'Authorization': token})
    return response.json()

@app.tool()
def create_container(image_name: str, container_name: str, cmd: str = "", add_caps: list[str] = [], host_name: str = "", ports_map: list[str] = []):
    """
    创建容器。
    参数：image_name（字符串）：镜像名称
    container_name（字符串）：容器名称
    cmd（字符串）：容器启动命令
    add_caps（列表）：添加的capabilities
    host_name（字符串）：主机名
    ports_map（列表）：端口映射（例如：["8080:8080"]）
    返回：容器详细信息和 status
    """
    url = f'{base_url}/api/run_container'
    response = httpx.post(url, json={'image_name': image_name, 'container_name': container_name, 'cmd': cmd, 'add_caps': add_caps, 'host_name': host_name, 'ports_map': ports_map}, headers={'Authorization': token})
    return response.json()

@app.tool()
def run_container_by_compose(compose_file: str, other_files: str = "{}"):
    """
    根据compose文件运行容器。
    参数：compose_file（字符串）：compose文件内容
    other_files（json字符串）：其他文件内容（包括Dockerfile或启动必需的脚本等），键名为文件名字符串，键值为文件内容字符串，没有则填空字符串
    返回：容器详细信息和 status
    """
    
    url = f'{base_url}/api/run_container_by_compose'
    other_files_dict = {}
    if other_files == "{}" or other_files == "":
        other_files_dict = {}
    else:
        other_files_dict = json.loads(other_files)
    assert isinstance(other_files_dict, dict), "other_files must be a json object"
    
    request_data = {'compose_file': compose_file, 'other_files': other_files_dict, 'delete_temp_dir': False}
    
    response = httpx.post(url, json=request_data, headers={'Authorization': token})
    result = response.json()
    
    return result



@app.tool()
def fetch_container_logs(container_name: str):
    """
    获取容器日志。
    参数：container_name（字符串）：容器名称
    返回：日志和 status
    """
    url = f'{base_url}/api/fetch_container_logs'
    response = httpx.post(url, json={'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def stop_container(container_name: str):
    """
    停止容器。
    参数：container_name（字符串）：容器名称
    返回：状态
    """
    url = f'{base_url}/api/stop_container'
    response = httpx.post(url, json={'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def start_container(container_name: str):
    """
    启动容器。
    参数：container_name（字符串）：容器名称
    返回：状态
    """
    url = f'{base_url}/api/start_container'
    response = httpx.post(url, json={'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def restart_container(container_name: str):
    """
    重启容器。
    参数：container_name（字符串）：容器名称
    返回：状态
    """
    url = f'{base_url}/api/restart_container'
    response = httpx.post(url, json={'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def remove_container(container_name: str):
    """
    删除容器。
    参数：container_name（字符串）：容器名称
    返回：状态
    """
    url = f'{base_url}/api/delete_container'
    response = httpx.post(url, json={'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def fetch_container_info(container_name: str):
    """
    获取容器信息。
    参数：container_name（字符串）：容器名称
    返回：容器详细信息和 status
    """
    url = f'{base_url}/api/fetch_container_info'
    response = httpx.post(url, json={'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def create_exec_session(container_name: str):
    """
    创建一个新的交互式 shell 会话。推荐使用。
    参数：container_name（字符串）：容器名称
    返回：包含 exec_session_id 的响应和 status
    """
    url = f'{base_url}/api/create_exec_session'
    response = httpx.post(url, json={'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def execute_command_in_session(container_name: str, cmd: str, exec_session_id: str):
    """
    在已存在的 shell 会话中执行命令。推荐使用。
    参数：container_name（字符串）：容器名称
    cmd（字符串）：要执行的命令
    exec_session_id（字符串）：会话ID（由 create_exec_session 返回）
    返回：命令输出和 status
    """
    url = f'{base_url}/api/execute_command_in_session'
    response = httpx.post(url, json={'container_name': container_name, 'cmd': cmd, 'exec_session_id': exec_session_id}, headers={'Authorization': token})
    return response.json()

@app.tool()
def close_exec_session(container_name: str, exec_session_id: str):
    """
    关闭交互式 shell 会话。
    参数：container_name（字符串）：容器名称
    exec_session_id（字符串）：会话ID（由 create_exec_session 返回）
    返回：状态
    """
    url = f'{base_url}/api/close_exec_session'
    response = httpx.post(url, json={'container_name': container_name, 'exec_session_id': exec_session_id}, headers={'Authorization': token})
    return response.json()

@app.tool()
def get_more_session_output(container_name: str, exec_session_id: str):
    """
    获取更多的交互式 shell 会话输出。当你认为仍有输出未被获取时，可以调用此接口。
    参数：exec_session_id（字符串）：会话ID（由 create_exec_session 返回）
    container_name（字符串）：容器名称
    返回：会话输出
    """
    url = f'{base_url}/api/get_more_session_output'
    response = httpx.post(url, json={'exec_session_id': exec_session_id, 'container_name': container_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
async def wait_for_seconds(seconds: int):
    """
    等待指定的秒数。
    参数：seconds（整数）：等待的秒数
    返回：状态
    """
    await asyncio.sleep(seconds)
    return {"status": "success"}

@app.tool()
def create_network(network_name: str, is_internal: bool, subnet: str, ip_range: str, gateway: str):
    """
    创建一个新的 Docker 网络。
    参数：
        network_name（字符串）：网络名称
        is_internal（布尔值）：是否为内部网络
        subnet（字符串）：子网，例如 "172.20.0.0/16"
        ip_range（字符串）：IP 地址范围，例如 "172.20.10.0/24"，可选
        gateway（字符串）：网关地址，例如 "172.20.0.1"，可选
    返回：网络创建结果和 status
    """
    url = f'{base_url}/api/create_network'
    response = httpx.post(url, json={
        'network_name': network_name,
        'is_internal': is_internal,
        'subnet': subnet,
        'ip_range': ip_range,
        'gateway': gateway
    }, headers={'Authorization': token})
    return response.json()

@app.tool()
def delete_network(network_name: str):
    """
    删除指定的 Docker 网络。
    参数：network_name（字符串）：网络名称
    返回：删除结果和 status
    """
    url = f'{base_url}/api/delete_network'
    response = httpx.post(url, json={'network_name': network_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def list_networks():
    """
    列出所有 Docker 网络。
    参数：无
    返回：所有网络的详细信息和 status
    """
    url = f'{base_url}/api/list_networks'
    response = httpx.get(url, headers={'Authorization': token})
    return response.json()

@app.tool()
def network_info(network_name: str):
    """
    获取指定 Docker 网络的信息。
    参数：network_name（字符串）：网络名称
    返回：网络详细信息和 status
    """
    url = f'{base_url}/api/network_info'
    response = httpx.post(url, json={'network_name': network_name}, headers={'Authorization': token})
    return response.json()

@app.tool()
def connect_network(network_name: str, container_name: str, ipv4_address: str = ""):
    """
    将容器连接到指定网络。
    参数：
        network_name（字符串）：网络名称
        container_name（字符串）：容器名称
        ipv4_address（字符串）：容器的IPv4地址，可选
        如果不提供IPv4地址，则使用Docker自动分配的地址。
    返回：连接结果和 status
    """
    url = f'{base_url}/api/connect_network'
    response = httpx.post(url, json={
        'network_name': network_name,
        'container_name': container_name,
        'ipv4_address': ipv4_address
    }, headers={'Authorization': token})
    return response.json()

@app.tool()
def disconnect_network(network_name: str, container_name: str):
    """
    将容器从指定网络断开连接。
    参数：
        network_name（字符串）：网络名称
        container_name（字符串）：容器名称
    返回：断开结果和 status
    """
    url = f'{base_url}/api/disconnect_network'
    response = httpx.post(url, json={
        'network_name': network_name,
        'container_name': container_name
    }, headers={'Authorization': token})
    return response.json()
