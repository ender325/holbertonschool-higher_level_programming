#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        A NumPy array containing the product of the matrices.
    """
    return np.matmul(m_a, m_b)
