"""Utility to generate ECharts option objects."""

from typing import Any, Dict, Iterable, Mapping


def generate_option(chart_type: str, data: Any) -> Dict[str, Any]:
    """Generate an ECharts option dictionary for a chart.

    Parameters
    ----------
    chart_type:
        Type of the chart: ``"line"``, ``"pie"`` or ``"bar"``.
    data:
        Data for the chart. ``data`` should be a mapping containing ``labels``
        and ``values`` sequences as well as an optional ``name``. ``labels``
        correspond to category names (used for the x-axis of line and bar
        charts or as slice names for pie charts) while ``values`` provide the
        numeric values.

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
    if not isinstance(data, Mapping) or "labels" not in data or "values" not in data:
        raise ValueError("data must contain 'labels' and 'values'")

    labels = list(data["labels"])
    values = list(data["values"])
    series_name = str(data.get("name", ""))

    if chart_type == "line":
        return {
            "xAxis": {"type": "category", "data": labels},
            "yAxis": {"type": "value"},
            "series": [
                {
                    "type": "line",
                    "name": series_name,
                    "data": values,
                }
            ],
        }
    elif chart_type == "bar":
        return {
            "xAxis": {"type": "category", "data": labels},
            "yAxis": {"type": "value"},
            "series": [
                {
                    "type": "bar",
                    "name": series_name,
                    "data": values,
                }
            ],
        }
    elif chart_type == "pie":
        pie_data = [
            {"name": label, "value": value} for label, value in zip(labels, values)
        ]
        return {
            "series": [
                {
                    "type": "pie",
                    "data": pie_data,
                }
            ]
        }

    raise ValueError(f"Unsupported chart type: {chart_type}")
