import graph_jsp_utils.jsp_instance_parser as parser
import numpy as np


def test_parser_with_ft06_instance(download_ft06, resources_path):
    jsp_std_path = resources_path.joinpath("standard")
    jsp_taillard_path = resources_path.joinpath("taillard")

    ft06_std_path = jsp_std_path.joinpath("ft06.txt")
    ft06_ta_path = jsp_taillard_path.joinpath("ft06.txt")

    jps_instance_from_std, std_matrix = parser.parse_jps_standard_specification(ft06_std_path)
    jps_instance_from_ta, taillard_matrix = parser.parse_jps_taillard_specification(ft06_ta_path)

    assert np.array_equal(jps_instance_from_std, jps_instance_from_ta)

    ft06 = np.array([[
        [2, 0, 1, 3, 5, 4],
        [1, 2, 4, 5, 0, 3],
        [2, 3, 5, 0, 1, 4],
        [1, 0, 2, 3, 4, 5],
        [2, 1, 4, 5, 0, 3],
        [1, 3, 5, 0, 4, 2]],

        [[1, 3, 6, 7, 3, 6],
         [8, 5, 10, 10, 10, 4],
         [5, 4, 8, 9, 1, 7],
         [5, 5, 5, 3, 8, 9],
         [9, 3, 5, 4, 3, 1],
         [3, 3, 9, 10, 4, 1]
         ]])

    assert np.array_equal(jps_instance_from_ta, ft06)
