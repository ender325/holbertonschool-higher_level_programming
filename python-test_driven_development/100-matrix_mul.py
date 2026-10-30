#!/usr/bin/python3
"""
Defines a matrix multiplication function.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices (m_a and m_b).

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of lists: The resulting product matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains non-numbers, or has rows of different sizes.
        ValueError: If m_a or m_b is empty, or if dimensions are incompatible.
    """
    # 1. Validate m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # 2. Validate m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 3. Validate m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # 4. Validate m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 5. Validate m_a is not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    # 6. Validate m_b is not empty
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 7. Validate elements of m_a are integers or floats
    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    # 8. Validate elements of m_b are integers or floats
    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    # 9. Validate m_a rows are rectangular (same size)
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    # 10. Validate m_b rows are rectangular (same size)
    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # 11. Validate matrix multiplication dimensions compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            new_row.append(sum_val)
        result.append(new_row)

    return result
