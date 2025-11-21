import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
import io

class TestHolidayInput(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_generate_with_holidays(self):
        # Prepare form data
        data = {
            'employees_input': 'Anna,160\nMarco,160',
            'month': '11',
            'year': '2025',
            'day[]': ['Monday', 'Tuesday'],
            'start_time[]': ['09:00', '09:00'],
            'end_time[]': ['17:00', '17:00'],
            'staff_count[]': ['2', '2'],
            # Holiday data
            'holiday_date[]': ['2025-11-15', '2025-11-20'],
            'holiday_type[]': ['CLOSED', 'SPECIAL'],
            'holiday_start[]': ['', '10:00'],
            'holiday_end[]': ['', '14:00'],
            'holiday_staff[]': ['', '1']
        }
        
        # Send POST request
        response = self.app.post('/generate', data=data, content_type='multipart/form-data')
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        print("Test passed: Excel file generated successfully with structured holiday data.")

if __name__ == '__main__':
    unittest.main()
