from docker import *

def main():
    print("Hello from docker-mcp!")
    app.run(transport="sse", port=19000)


if __name__ == "__main__":
    main()
