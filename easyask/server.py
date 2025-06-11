from mcp.server import FastMCP

mcp = FastMCP(name="easy-ask-tools")


def serve():
    mcp.run(transport='sse')
