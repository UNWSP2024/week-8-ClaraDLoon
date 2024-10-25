#Program #5: Course Info
#Clara Riley
#Luke Snell
#10/24/24

def main():
    courses = {}

    while True:
        course_id = input("Enter a course ID (or 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter a course name: ")
        courses[course_id] = course_name

    subject = input("Enter the subject that you want to search for: ")

    print(f"Courses with subject '{subject}':")
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")


if __name__ == "__main__":
    main()
