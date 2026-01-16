import pytest
from attendance import calculate_attendance

def test_attendance_eligible():
    result = calculate_attendance(100, 80)
    assert result >= 75

def test_attendance_not_eligible():
    result = calculate_attendance(100, 60)
    assert result < 75

def test_exact_boundary():
    result = calculate_attendance(100, 75)
    assert result == 75

def test_zero_classes_held():
    with pytest.raises(ZeroDivisionError):
        calculate_attendance(0, 10)
