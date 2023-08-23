"""
Unit tests for
"""

import logging
import unittest
import pandas as pd

from pandas.testing import assert_frame_equal

from steps.fuzzy_lookup import _preprocess_text, get_fuzzy_lookup


logging.disable(logging.CRITICAL)


class TestNoteAnalysis(unittest.TestCase):
    "Class to test functions of ."

    def test_string_manipulation(self):
        "Test correct result when calling _preprocess_text"

        data = {
            "000001": "TimE     4       TeSt!",
            "000002": "TEST.  number 2",
        }

        output = []

        for row in data.values():
            output.append(_preprocess_text(row))

        expected = ["time test", "test number"]

        self.assertEqual(output, expected)

    def test_lookup(self):
        "Test main lookup function"

        fields = ["id", "description"]

        data = [
            ["000001", "time2 TeST? making this longer, thanks black"],
            ["000002", "ANOTHer 400 ?! tests"],
            ["000003", "time for some mouldy mould old cold words"],
        ]

        input = pd.DataFrame(data, columns=fields)

        output = get_fuzzy_lookup("tbl_note_analysis_mould", input)

        fields = [
            "id",
            "description",
            "original_description",
            "one_to_one_ratio",
            "set_ratio",
            "leven_score",
            "simple_search",
            "best_score",
        ]

        # datatype = ["str", "str", "str", "float", "float", "float", "float", "float"]

        data = [
            [
                "000001",
                "time test making this longer thanks black",
                "time2 TeST? making this longer, thanks black",
                "29",
                "29",
                "3",
                "0",
                "29",
            ],
            [
                "000002",
                "another tests",
                "ANOTHer 400 ?! tests",
                "27",
                "23",
                "5",
                "0",
                "27",
            ],
            [
                "000003",
                "time for some mouldy mould words",
                "time for some mouldy mould old cold words",
                "100",
                "100",
                "0",
                "100",
                "100",
            ],
        ]

        expected = pd.DataFrame(data, columns=fields)

        expected = expected.astype(
            {
                "one_to_one_ratio": float,
                "set_ratio": float,
                "leven_score": float,
                "simple_search": float,
                "best_score": float,
            }
        )

        assert_frame_equal(output, expected)


if __name__ == "__main__":
    unittest.main(exit=False)
