#!/usr/bin/python3
"""Module 101-lazy_matrix_mul

Provides a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy.matmul.

    Args:
        m_a: first matrix (list of lists of ints/floats)
        m_b: second matrix (list of lists of ints/floats)

    Returns:
        The product of m_a and m_b as a numpy array.

    Exceptions raised by NumPy (ValueError, TypeError) are not caught,
    so they propagate with NumPy's own messages.
    """
    return np.matmul(m_a, m_b)
