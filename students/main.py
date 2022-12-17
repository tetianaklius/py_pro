import student_
import group_
import logger_info

if __name__ == "__main__":
    try:
        logger_info.logger.info("Started logging")
        group = group_.Group("group", max_group=10)
        group.add_student(student_.Student("Lida", "Vasylenko", 25))  # 1
        group.add_student(student_.Student("Oksana", "Dovzhenko", 20))  # 2
        group.add_student(student_.Student("Yurii", "Kozak", 26))  # 3
        group.add_student(student_.Student("Denys", "Zhuk", 29))  # 4
        group.add_student(student_.Student("Olha", "Nesterenko", 32))  # 5
        group.add_student(student_.Student("Ostap", "Stelmakh", 18))  # 6
        group.add_student(student_.Student("Marta", "Buriak", 23))  # 7
        group.add_student(student_.Student("Hanna", "Shepit", 35))  # 8
        group.add_student(student_.Student("Serhii", "Haiduk", 22))  # 9
        # group.add_student(student_.Student("Andrii", "Melnyk", 19))   # 10
        # group.add_student(student_.Student("Ivan", "Horyn", 21))

        res_find = group.find_student("Nesterenko")
        for item in res_find:
            print(item)
        for item in res_find:
            print(item.name, item.surname, item.age, sep="_")
        print(group)
        logger_info.logger.info("Finished logging")

    except Exception as error:
        print(error)
