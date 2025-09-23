def calculate_total(value1, value2, value3, data_type="items"):
    """Calculate total of three values with descriptive output"""
    total = value1 + value2 + value3
    # This print statement is provided for you
    print(f"Total {data_type}: {total}")
    return total

def calculate_average(value1, value2, value3, data_type):
    """Calculate average of three values with descriptive output"""
    average = (value1 + value2 + value3) / 3
    print(f"Average {data_type}: {average:.1f}")
    return average
def process_course_data():
    """Process enrollment data for three courses"""
    print("=== Course Enrollment Processor ===")
    
    # Get course enrollment numbers
    course1 = int(input("Enter CSCI 1250 enrollment: "))
    course2 = int(input("Enter CSCI 1100 enrollment: "))
    course3 = int(input("Enter CSCI 2400 enrollment: "))
    
    # Use your pattern functions
    total_enrolled = calculate_total(course1, course2, course3, "students enrolled")
    avg_class_size = calculate_average(course1, course2, course3, "class size")
    
    return total_enrolled, avg_class_size

def process_temperature_data():
    """Process daily temperature readings"""
    print("\n=== Temperature Data Processor ===")
    
    # Get temperature data
    day1_temp = float(input("Enter Monday temperature: "))
    day2_temp = float(input("Enter Tuesday temperature: "))
    day3_temp = float(input("Enter Wednesday temperature: "))
    
    # Use your pattern functions
    total_temp = calculate_total(day1_temp, day2_temp, day3_temp, "degrees")
    avg_temp = calculate_average(day1_temp, day2_temp, day3_temp, "temperature")
    
    return total_temp, avg_temp

def main():
    """Main program demonstrating pattern reuse"""
    course_total, course_avg = process_course_data()
    

    temp_total, temp_avg = process_temperature_data()

    print("\n=== Summary Report ===")
    # TODO: Print summary information using the values you stored above
    print(f"Total students across all courses: {course_total}")
    print(f"Average class size: {course_avg:.1f}")
    print(f"Average temperature: {temp_avg:.1f}°F")
    
if __name__ == "__main__":
    main()
