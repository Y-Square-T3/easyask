"""Utility to generate ECharts option objects."""

from typing import Any, Dict, Sequence


def generate_option(chart_type: str, data: Any) -> Dict[str, Any]:
    """Generate an ECharts option dictionary for a chart.

    Parameters
    ----------
    chart_type:
        Type of the chart: ``"line"``, ``"pie"`` or ``"bar"``.
    data:
        Data for the chart. For ``line`` and ``bar`` charts, ``data`` should be
        a mapping with ``x`` and ``y`` sequences and an optional ``name`` for
        the series. For ``pie`` charts, ``data`` should be a sequence of
        dictionaries with ``"value"`` and ``"name"`` keys.

    Returns
    -------
    Dict[str, Any]
        ECharts option dictionary suitable for ``setOption``.

    Raises
    ------
    ValueError
        If ``chart_type`` is unsupported.
    """

    chart_type = chart_type.lower()
    if chart_type == "line":
        if not isinstance(data, dict) or "x" not in data or "y" not in data:
            raise ValueError("line chart data must be a dict with 'x' and 'y'")
        series_name = data.get("name", "")
        return {
            "xAxis": {"type": "category", "data": list(data["x"])},
            "yAxis": {"type": "value"},
            "series": [
                {
                    "type": "line",
                    "name": series_name,
                    "data": list(data["y"]),
                }
            ],
        }
    elif chart_type == "bar":
        if not isinstance(data, dict) or "x" not in data or "y" not in data:
            raise ValueError("bar chart data must be a dict with 'x' and 'y'")
        series_name = data.get("name", "")
        return {
            "xAxis": {"type": "category", "data": list(data["x"])},
            "yAxis": {"type": "value"},
            "series": [
                {
                    "type": "bar",
                    "name": series_name,
                    "data": list(data["y"]),
                }
            ],
        }
    elif chart_type == "pie":
        if not isinstance(data, Sequence):
            raise ValueError("pie chart data must be a sequence of dicts")
        return {
            "series": [
                {
                    "type": "pie",
                    "data": list(data),
                }
            ]
        }

    raise ValueError(f"Unsupported chart type: {chart_type}")
