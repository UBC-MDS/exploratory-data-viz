import random
import altair as alt
import numpy as np
import pandas as pd


np.set_printoptions(linewidth=400)
pd.set_option("display.width", 350)
pd.set_option("display.max_columns", 8)
pd.set_option("display.max_rows", 6)


@alt.theme.register("increase_font_size", enable=True)
def increase_chart_font_size() -> alt.theme.ThemeConfig:
    return {
    'config': {
        'view': {'continuousWidth': 300, 'continuousHeight': 300},
        'legend': {'symbolSize': 14, 'titleFontSize': 14, 'labelFontSize': 12},
        'axis': {'titleFontSize': 14, 'labelFontSize': 12},
        'header': {'titleFontSize': 16, 'labelFontSize': 14}
        }
    }


def assert_chart_equal(expected, actual):
    expected_dict = expected if isinstance(expected, dict) else expected.to_dict()
    actual_dict = actual if isinstance(actual, dict) else actual.to_dict()
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


def remove_keys_inplace(spec, keys):
    if isinstance(spec, dict):
        for key in list(spec.keys()):
            if key in keys:
                del spec[key]
            else:
                remove_keys_inplace(spec[key], keys)
    elif isinstance(spec, list):
        for item in spec:
            remove_keys_inplace(item, keys)
