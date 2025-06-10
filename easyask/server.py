from mcp.server import FastMCP

mcp_tools = FastMCP(name="easy-ask-tools")


def serve():
    mcp_tools.run(transport='sse')
