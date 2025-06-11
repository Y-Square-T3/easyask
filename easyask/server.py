import logging
from typing import Any, List, Dict

from mcp.server import FastMCP

from easyask.logging_config import LOGGING_CONFIG
from easyask.settings import get_settings
from easyask.tools import chart

logging.config.dictConfig(LOGGING_CONFIG)
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


if __name__ == "__main__":
    res = chart.get_chart_options([
        ['product', '2015', '2016', '2017'],
        ['Matcha Latte', 43.3, 85.8, 93.7],
        ['Milk Tea', 83.1, 73.4, 55.1],
        ['Cheese Cocoa', 86.4, 65.2, 82.5],
        ['Walnut Brownie', 72.4, 53.9, 39.1]
    ])

    print(res)
