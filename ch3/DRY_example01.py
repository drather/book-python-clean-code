def process_students_list(students):
    ...

    students_ranking = sorted(students, key=lambda s: s.passed * 11 - s.failed * 5 - s.years * 2)

    # 학생별 순위 출력
    for student in students_ranking:
        print(
            f"이름: {student.name}, 점수: {student.passed * 11 - student.failed * 5 - student.year * 2}"
        )
