import unittest
from main import tinh_diem_gpa

class TestGpaFunctions(unittest.TestCase):

    def test_gpa_he_muoi(self):
        self.assertEqual(tinh_diem_gpa(8.5), 4.0)

    def test_gpa_tuyen_tinh(self):
        self.assertEqual(tinh_diem_gpa(7.0), 2.8)

if __name__ == '__main__':
    unittest.main()