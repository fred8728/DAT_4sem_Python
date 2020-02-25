import matplotlib.pyplot as plt

student_attendance = {'day1': 33, 'day2': 34, 'day3': 29,
                      'day4': 31, 'day5': 28, 'day6': 26, 'day7': 30}

plt.figure()
plt.plot(list(student_attendance.keys()), list(
    student_attendance.values()))

plt.title("Attendance for week")
plt.xlabel("Days")
plt.ylabel("Attendance")

plt.show()