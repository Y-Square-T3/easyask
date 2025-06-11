from typing import Any, List, Dict

from mcp.server import FastMCP

from easyask.tools import chart

mcp = FastMCP(name="easy-ask-tools")


@mcp.tool(
    name="get_chart_options",
    description="based on the dataset, generate chart options using the specified generator class",
)
def get_chart_options(dataset: List[List[Any]]) -> Dict:
    return chart.get_chart_options(dataset)


def serve():
    mcp.run(transport='sse')
