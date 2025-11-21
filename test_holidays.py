from app import generate_and_transform_schedules, parse_holidays, parse_employees, parse_schedules

def test_holiday_logic():
    # 1. Setup Data
    employees = parse_employees("Anna,160\nMarco,160")
    schedules = parse_schedules("Monday,09:00 - 13:00,1")
    
    # 2. Define Holidays
    # Nov 15 is a Saturday in 2025. Let's make it CLOSED.
    # Nov 17 is a Monday in 2025. Normal schedule would be 09-13. Let's make it SPECIAL 10-12.
    holidays_text = "15/11/2025, CLOSED\n17/11/2025, 10:00 - 12:00, 1"
    holidays = parse_holidays(holidays_text)
    
    print("Parsed Holidays:", holidays)
    
    # 3. Run Generation for November 2025
    store_view, employee_view = generate_and_transform_schedules(employees, schedules, holidays, 2025, 11)
    
    # 4. Verify Results
    
    # Check Nov 15 (Closed)
    # 15th is a Saturday.
    print("\nChecking Nov 15 (CLOSED)...")
    if (15, "CLOSED") in store_view and store_view[(15, "CLOSED")] == "CLOSED":
        print("PASS: Nov 15 is CLOSED")
    else:
        print(f"FAIL: Nov 15 status is {store_view.get((15, 'CLOSED'), 'Not Found')}")
        
    # Check Nov 17 (Special)
    # 17th is a Monday.
    print("\nChecking Nov 17 (Special Shift)...")
    # We expect key (17, "10:00 - 12:00") to exist
    if (17, "10:00 - 12:00") in store_view:
        print(f"PASS: Nov 17 has special shift 10:00 - 12:00. Assigned: {store_view[(17, '10:00 - 12:00')]}")
    else:
        print("FAIL: Nov 17 special shift not found.")
        
    # Check Nov 24 (Normal Monday)
    # 24th is a Monday. Should have normal schedule 09:00 - 13:00
    print("\nChecking Nov 24 (Normal Monday)...")
    if (24, "09:00 - 13:00") in store_view:
        print(f"PASS: Nov 24 has normal shift. Assigned: {store_view[(24, '09:00 - 13:00')]}")
    else:
        print("FAIL: Nov 24 normal shift not found.")

if __name__ == "__main__":
    test_holiday_logic()
