#! /usr/bin/python3

import sys


def check_simplification(op1, op2):
    """As we have seen in the problem statement, given two Pauli operators, you could obtain the expected value
    of each of them by running a single circuit following the two defined rules. This function will determine whether,
    given two Pauli operators, such a simplification can be produced.

    Args:
        - op1 (list(str)): First Pauli word (list of Pauli operators), e.g., ["Y", "I", "Z", "I"].
        - op2 (list(str)): Second Pauli word (list of Pauli operators), e.g., ["Y", "I", "X", "I"].

    Returns:
        - (bool): 'True' if we can simplify them, 'False' otherwise. For the example args above, the third qubit does not allow simplification, so the function would return `False`.
    """

    # QHACK

    # QHACK


def join_operators(op1, op2):
    """This function will receive two operators that we know can be simplified
    and returns the operator corresponding to the union of the two previous ones.

    Args:
        - op1 (list(str)): First Pauli word (list of Pauli operators), e.g., ["Y", "I", "Z", "I"].
        - op2 (list(str)): Second Pauli word (list of Pauli operators), e.g., ["Y", "I", "X", "I"].

    Returns:
        - (list(str)): Pauli operator corresponding to the union of op1 and op2.
        For the case above the output would be ["Y", "X", "Z", "I"]
    """

    # QHACK

    # QHACK


def optimize_measurements(obs_hamiltonian):
    """This function will go through the list of Pauli words provided in the statement, grouping the operators
    following the simplification process of the previous functions.

    Args:
        - obs_hamiltonian (list(list(str))): Groups of Pauli words making up the Hamiltonian.

    Returns:
        - (list(list(str))): The chosen Pauli operators to measure after grouping.
    """

    final_solution = []

    for op1 in obs_hamiltonian:
        added = False
        for i, op2 in enumerate(final_solution):

            if check_simplification(op1, op2):
                final_solution[i] = join_operators(op1, op2)
                added = True
                break
        if not added:
            final_solution.append(op1)

    return final_solution


def compression_ratio(obs_hamiltonian, final_solution):
    """Function that calculates the compression ratio of the procedure.

    Args:
        - obs_hamiltonian (list(list(str))): Groups of Pauli operators making up the Hamiltonian.
        - final_solution (list(list(str))): Your final selection of observables.

    Returns:
        - (float): Compression ratio your solution.
    """

    # QHACK

    # QHACK


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block

    inputs = sys.stdin.read().split(",")

    obs_hamiltonian = []
    # open file and read the content in a list
    aux = []
    for i, line in enumerate(inputs):
        if i == 0:
            first = int(line)
        else:
            aux.append(line[0])
            if i % first == 0:
                obs_hamiltonian.append(aux)
                aux = []

    output = optimize_measurements(obs_hamiltonian)
    print(compression_ratio(obs_hamiltonian, output))
