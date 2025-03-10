import random

import altair as alt


def increase_font_size():
    return {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300},
            "legend": {"symbolSize": 14, "titleFontSize": 14, "labelFontSize": 14},
            "axis": {"titleFontSize": 14, "labelFontSize": 12},
            "header": {"titleFontSize": 16, "labelFontSize": 14},
            "encoding": {"x": {"scale": {"zero": False}}},
        }
    }


alt.themes.register("increase_font_size", increase_font_size)
alt.themes.enable("increase_font_size")


# def increase_chart_font_size():
#     import altair as alt
#     bigger_font = {
#         'config': {
#             'view': {'continuousWidth': 400, 'continuousHeight': 300},
#             'legend': {'symbolSize': 14, 'titleFontSize': 14, 'labelFontSize': 14},
#             'axis': {'titleFontSize': 14, 'labelFontSize': 12},
#             'header': {'titleFontSize': 16, 'labelFontSize': 14},
#             'encoding': {'x': {'scale': {'zero': False}}}}}
#     alt.themes.register('bigger_font', bigger_font)
#     alt.themes.enable('bigger_font')


def assert_chart_equal(expected, actual):
    expected_dict = expected.to_dict()
    actual_dict = actual.to_dict()
    try:
        assert_dict_equal(expected_dict, actual_dict)
        message = random.choice(["Nicely done", "Great", "Good job", "Well done"])
        emoji = random.choice(["🍀", "🎉", "🌈", "🙌", "🚀", "🌟", "✨", "💯"])
        return {"correct": True, "message": f"{message}! {emoji}"}
    except AssertionError as e:
        return {"correct": False, "message": str(e)}


def assert_dict_equal(expected_dict, actual_dict, path=""):
    # Check all keys in dict1
    for key in expected_dict:
        if key not in actual_dict:
            raise AssertionError(
                f"Key mismatch: '{path + key}' was expected, but not found."
            )
        else:
            # If both values are dictionaries, recurse into them
            if isinstance(expected_dict[key], dict) and isinstance(
                actual_dict[key], dict
            ):
                assert_dict_equal(
                    expected_dict[key], actual_dict[key], path + key + "."
                )
            # Compare the values
            elif expected_dict[key] != actual_dict[key]:
                raise AssertionError(
                    f"Value mismatch at '{path + key}': {expected_dict[key]} != {actual_dict[key]}"
                )

    # Check for any extra keys in dict2
    for key in actual_dict:
        if key not in expected_dict:
            raise AssertionError(f"Key mismatch: '{path + key}' was unexpected.")
