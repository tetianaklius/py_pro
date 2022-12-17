import student_
import exception_
import logger_info


class Group:
    def __init__(self, title: str, max_group):
        if not isinstance(max_group, int):
            raise TypeError()
        if max_group <= 0:
            raise ValueError()
        self.title = title
        self.group = []
        self.max_group = max_group

    def add_student(self, student: student_.Student):
        """
        :param student:
        :return:
        """
        if student in self.group:
            raise exception_.DublicateStudentError(student, self.title)
        if len(self.group) >= self.max_group:
            raise exception_.GroupLimitError(self.max_group)
        self.group.append(student)
        logger_info.logger.info("Add student " + str(student.surname))

    def remove_student(self, student: student_.Student):
        """
        :param student:
        :return:
        """
        if student in self.group:
            self.group.remove(student)

    def find_student(self, surname: str):
        """
        :param surname:
        :return:
        """
        res = []
        for student in self.group:
            if student.surname == surname:
                res.append(student)
        return res

    def __str__(self):
        return f"{self.title}:\n" + '\n'.join(map(str, self.group))