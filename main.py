from pprint import pprint

from echarts import generate_option


def main() -> None:
    """Demonstrate generation of ECharts option objects."""
    line_data = {"x": ["Mon", "Tue", "Wed"], "y": [820, 932, 901], "name": "demo"}
    pie_data = [
        {"value": 1048, "name": "Search Engine"},
        {"value": 735, "name": "Direct"},
    ]

    pprint(generate_option("line", line_data))
    pprint(generate_option("pie", pie_data))


if __name__ == "__main__":
    main()
