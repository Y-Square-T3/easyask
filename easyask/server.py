from typing import Any, List, Dict

from mcp.server import FastMCP

from easyask.settings import get_settings
from easyask.tools import chart

settings = get_settings()
mcp = FastMCP(name="easy-ask-tools", host=settings.host, port=settings.port)


@mcp.tool(
    name="get_chart_options",
    description="based on the dataset, generate chart options using the specified generator class",
)
def get_chart_options(dataset: List[List[Any]]) -> Dict:
    return chart.get_chart_options(dataset)


def serve():
    mcp.run(transport='sse')
