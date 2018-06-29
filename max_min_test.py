import max_min


def test_empty_circ_list():
    circ_list = []
    bw_list = []
    assert max_min.max_min_bw(circ_list, bw_list) == []


def test_single_circuit():
    circ_list = [[0], [1], [2]]
    bw_list = [10, 20, 30]
    assert max_min.max_min_bw(circ_list, bw_list) == bw_list


def test_complex_case():
    circ_list = [{0, 1}, {1, 2}, {2, 3}, {3, 4}]
    bw_list = [10, 22, 30, 40, 50]
    # circuit 0: bottlenecked at relay 0, 10.0
    # circuit 1: bottlenecked at relay 1, 12.0 left (after circuit 0 removed)
    # circuit 2: bottlenecked at relay 2, 18.0 left (after circuit 1 removed)
    # circuit 3: bottlenecked at relay 3, 22.0 left (after circuit 2 removed)
    assert max_min.max_min_bw(circ_list, bw_list) == [10.0, 12.0, 18.0, 22.0]


def test_generated():
    # this testcase was generated using a previous implementation of the flow simulator
    bw_list = [80, 83, 22, 74, 18, 16, 45, 36, 66, 37, 26, 30, 52, 76, 73, 79, 72, 31, 95, 29, 92, 90, 47, 26, 98, 33,
               23, 62, 53, 29, 51, 95, 19, 96, 41, 18, 71, 49, 89, 18, 20, 83, 86, 99, 84, 78, 74, 98, 37, 97, 47, 30,
               23, 44, 25, 22, 82, 31, 90, 11, 79, 39, 53, 92, 85, 59, 69, 29, 15, 94, 45, 56, 48, 83, 79, 98, 92, 12,
               53, 30, 38, 41, 23, 72, 54, 28, 25, 70, 22, 59, 92, 75, 31, 51, 97, 62, 28, 20, 75, 26]
    bw_list = [x * 3 for x in bw_list]
    circ_list = [[17, 25, 39], [46, 27, 91], [25, 94, 58], [48, 14, 67], [50, 66, 13], [91, 45, 44], [44, 98, 10],
                 [62, 92, 94], [53, 3, 90], [98, 13, 28], [80, 14, 46], [79, 68, 76], [28, 90, 42], [58, 46, 16],
                 [38, 75, 62], [7, 79, 37], [43, 74, 77], [13, 78, 81], [83, 58, 10], [76, 62, 16], [38, 13, 74],
                 [13, 47, 42], [60, 92, 78], [42, 93, 76], [9, 67, 41], [42, 40, 96], [7, 30, 10], [0, 26, 65],
                 [1, 47, 84], [3, 15, 67]]
    expected = [49.5, 74., 49.5, 29., 45.6, 151., 26., 46.5, 132., 45.6, 74., 45., 76.2, 74., 56.25, 45., 36., 45.6,
                26., 56.25, 45.6, 45.6, 46.5, 76.2, 29., 60., 26., 69., 162., 29.]
    result = max_min.max_min_bw(circ_list, bw_list)
    assert expected == result
