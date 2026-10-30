#!/usr/bin/python3
"""Module 101-lazy_matrix_mul

Multiplies two matrices using NumPy.
"""
import warnings
import numpy as np


def _shape(arr):
    """Format a shape like NumPy 1.15 does: (1,0), (2,)."""
    if len(arr.shape) == 1:
        return "({},)".format(arr.shape[0])
    return "(" + ",".join(str(d) for d in arr.shape) + ")"


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy.matmul.

    Errors are raised with the NumPy 1.15 types/messages so the
    behavior does not depend on the installed NumPy version.
    """
    seq = (list, tuple, np.ndarray)
    if not isinstance(m_a, seq) or not isinstance(m_b, seq):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    ragged = "setting an array element with a sequence."
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            a = np.array(m_a)
            b = np.array(m_b)
    except ValueError:
        # ragged lists (newer NumPy refuses to build the array)
        raise ValueError(ragged)

    if a.dtype == object or b.dtype == object:
        # ragged lists (older NumPy builds an object array)
        raise ValueError(ragged)
    if a.dtype.kind in "US" or b.dtype.kind in "US":
        raise TypeError("invalid data type for einsum")
    if a.ndim == 0 or b.ndim == 0:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    a_dim = a.ndim - 1
    b_dim = b.ndim - 2 if b.ndim > 1 else 0
    if a.shape[a_dim] != b.shape[b_dim]:
        raise ValueError(
            "shapes {} and {} not aligned: {} (dim {}) != {} (dim {})".format(
                _shape(a), _shape(b),
                a.shape[a_dim], a_dim, b.shape[b_dim], b_dim))

    return np.matmul(a, b)
