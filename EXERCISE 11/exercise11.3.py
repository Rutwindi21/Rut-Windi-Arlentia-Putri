import pytest
from Exercise11.exercise3 import Employee

@pytest.fixture
def employee_instance():
    """Membuat objek Employee untuk digunakan dalam pengujian."""
    return Employee('Budi', 'Santoso', 50000)

def test_give_default_raise(employee_instance):
    """Menguji apakah kenaikan gaji default ($5,000) bekerja dengan benar."""
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 55000

def test_give_custom_raise(employee_instance):
    """Menguji apakah kenaikan gaji kustom bekerja dengan benar."""
    employee_instance.give_raise(10000)
    assert employee_instance.annual_salary == 60000