#!/usr/bin/python3
"""Module 101-lazy_matrix_mul

Provides a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy.matmul.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        The product of m_a and m_b as a numpy array.
    """
    seq = (list, tuple, np.ndarray)
    if not isinstance(m_a, seq) or not isinstance(m_b, seq):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    return np.matmul(m_a, m_b)
