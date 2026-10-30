#!/usr/bin/python3
"""
Defines a matrix multiplication function using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The resulting product matrix.
    """
    return np.matmul(m_a, m_b)
