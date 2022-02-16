def score_for_student(student):
    return student.passed * 11 - student.failed * 5 - student.year * 2


def process_students_list(students):
    ...

    students_ranking = sorted(students, key=score_for_student)

    # 학생별 순위 출력
    for student in students_ranking:
        print(
            f"이름: {student.name}, 점수: {score_for_student(student)}"
        )
