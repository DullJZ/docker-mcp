# Docker-MCP

English | [简体中文](README.zh-cn.md)

Docker-MCP is an MCP server based on [Docker Manager](https://github.com/DullJZ/docker-manager), built using the FastMCP framework on top of Docker Manager's API, providing management capabilities for Docker containers.

## Getting Started

It is recommended to use the uv tool to manage dependencies:

```bash
pip install uv
source venv/bin/activate
uv run install
```

Modify the Docker Manager API address and authentication token in `docker.py`.

```python
base_url = 'YOUR_DOCKER_MANAGER_BASE_URL'
token = 'YOUR_DOCKER_MANAGER_API_TOKEN'
```

Then run:

```bash
bash start.sh
```

## Tool List

| Tool Name                  | Function                          |
|---------------------------|-----------------------------------|
| pull_image                 | Pull a specified image            |
| list_images                | List all images                   |
| create_container           | Create a container                |
| run_container_by_compose   | Run a container using a compose file |
| fetch_container_logs       | Fetch container logs              |
| stop_container             | Stop a container                  |
| start_container            | Start a container                 |
| restart_container          | Restart a container               |
| remove_container           | Remove a container                |
| fetch_container_info       | Fetch container information       |
| create_exec_session        | Create an interactive shell session|
| execute_command_in_session | Execute a command in a session    |
| close_exec_session         | Close an interactive shell session |
| get_more_session_output    | Get more session output           |
| wait_for_seconds           | Wait for a specified number of seconds |
| create_network             | Create a Docker network           |
| delete_network             | Delete a Docker network           |
| list_networks              | List all Docker networks          |
| network_info               | Get network information           |
| connect_network            | Connect a container to a network  |
| disconnect_network         | Disconnect a container from a network |
