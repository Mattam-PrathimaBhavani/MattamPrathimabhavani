university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#  Print all student names and their majors
print("Student Names and Majors:")
for sid, data in university_data.items():
    print(f"{data['name']} - {data['major']}")

# Average score per course per student
print("\nAverage Score per Course per Student:")
for sid, data in university_data.items():
    print(f"{data['name']}:")
    for course, scores in data["courses"].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course}: {avg:.2f}")

# Students who scored >90 in final of Python101
print("\nStudents with >90 in Python101 Final:")
for sid, data in university_data.items():
    course = data["courses"].get("Python101")
    if course and course.get("final", 0) > 90:
        print(f"{data['name']} - Final: {course['final']}")

# Add new course AI101 for student S101
new_course = {"midterm": 95, "final": 96, "project": 98}
university_data["S101"]["courses"]["AI101"] = new_course
print("\nAdded AI101 for S101:")
print(university_data["S101"]["courses"]["AI101"])

# Print average for each course (across all students)
from collections import defaultdict

course_scores = defaultdict(list)

# Gather scores
for data in university_data.values():
    for course, scores in data["courses"].items():
        avg = sum(scores.values()) / len(scores)
        course_scores[course].append(avg)

# Compute and print averages
print("\nAverage Score per Course Across Students:")
for course, averages in course_scores.items():
    overall_avg = sum(averages) / len(averages)
    print(f"{course}: {overall_avg:.2f}")