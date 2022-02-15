#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


def compare_circuits(angles):
   return abs(circuit1(angles[0],angles[1])-circuit2(angles[0],angles[1]))
    """Given two angles, compare two circuit outputs that have their order of operations flipped: RX then RY VERSUS RY then RX.
    
    Args:
        - angles (np.ndarray): Two angles

    Returns:
        - (float): | < \sigma^x >_1 - < \sigma^x >_2 |
    """

    # QHACK #

    # define a device and quantum functions/circuits here
dev1 = qml.device("default.qubit", wires=1)


@qml.qnode(dev1)
def circuit1(x,y):
    qml.RX(x, wires=0)
    qml.RY(y, wires=0)
    return qml.expval(qml.PauliX(0))

@qml.qnode(dev1)
def circuit2(x,y):
    qml.RY(y, wires=0)
    qml.RX(x, wires=0)
    return qml.expval(qml.PauliX(0))

    # QHACK #




if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    angles = np.array(sys.stdin.read().split(","), dtype=float)
    output = compare_circuits(angles)
    print(f"{output:.6f}")
