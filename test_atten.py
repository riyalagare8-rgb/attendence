from attendance import calculate_attendance

def test_zero_attended():
    assert calculate_attendance(100, 0) == 0.0

def test_integer_attendance():
    assert calculate_attendance(100, 80) == 80.0

def test_float_attendance():
    assert calculate_attendance(40, 30) == 75.0

def test_boundary_attendance():
    assert calculate_attendance(200, 150) == 75.0
