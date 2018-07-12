from typing import Set, List, Sequence, Collection, Union

from sortedcontainers import SortedList

from math import inf


def max_min_bw(circ_list: Sequence[Collection[int]], bw: List[float]) -> List[float]:
    """
    Calculates the bandwidth allocated to each circuit in `circ_list` using the max-min bandwidth allocation.
    :param circ_list: A list of circuits. Each circuit is a list (or set) of relay indices. There are no constraints
    on the lengths of the circuits, but each relay index should appear at most once in a circuit
    :param bw: A list of bandwidth values for each relay
    :return: Returns a list of bandwidth values for each circuit, ordered the same as `circ_list`
    """

    num_relays = len(bw)
    # relay_to_circ maps from relay number to a set of circuit (indices) that go through this relay
    relay_to_circ: List[Set[int]] = [set() for _ in range(num_relays)]
    for circ_id, circ in enumerate(circ_list):
        for relay_id in circ:
            relay_to_circ[relay_id].add(circ_id)

    # initialize allocation to 0
    bw_alloc: List[Union[int, None]] = [None for _ in range(len(circ_list))]

    # copy of bandwidth list
    remaining_bw = bw.copy()

    bw_array = [[relay_to_circ[i] and remaining_bw[i] / len(relay_to_circ[i]) or inf, i]
                for i in range(num_relays)]
    bw_list = SortedList(x for x in bw_array if x[0] < inf)

    # iterate until relay_to_circ empty
    while any(relay_to_circ):
        # select the relay with the smallest bandwidth in the list
        bn_bw, bn_relay = bw_list.pop(0)

        update_relays = set()
        for circ_id in relay_to_circ[bn_relay]:
            # we're the bottleneck relay for these circuits
            bw_alloc[circ_id] = bn_bw
            for other_relay in circ_list[circ_id]:
                if other_relay != bn_relay:
                    # remove the circuit and bandwidth from other relays it goes through
                    # and note that we need to adjust this relay
                    update_relays.add(other_relay)
                    remaining_bw[other_relay] -= bn_bw
                    relay_to_circ[other_relay].remove(circ_id)
        relay_to_circ[bn_relay] = set()
        remaining_bw[bn_relay] = 0
        for relay in update_relays:
            bw_list.remove(bw_array[relay])
            if relay_to_circ[relay]:
                # update bandwidth and reinsert
                bw_array[relay][0] = remaining_bw[relay] / len(relay_to_circ[relay])
                bw_list.add(bw_array[relay])

    return bw_alloc
