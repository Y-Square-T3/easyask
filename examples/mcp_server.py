from easyask import generate_option
from mcp.server.fastmcp.server import FastMCP
import uvicorn

server = FastMCP(name="easy-ask")

@server.tool()
def generate_option_tool(chart_type: str, data: dict) -> dict:
    """Generate an ECharts option dictionary."""
    return generate_option(chart_type, data)

if __name__ == "__main__":
    uvicorn.run(server.app, host="0.0.0.0", port=8000)
