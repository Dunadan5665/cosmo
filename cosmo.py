import os
import csv

# Функция для проверки критериев отбора
def check_criteria(candidate):
    if "age" not in candidate:  # Проверяем наличие ключа "age"
        return False  # Возвращаем False, если ключ отсутствует

    age = int(candidate["age"])  # Только если ключ "age" существует
    height = int(candidate["height"])
    weight = float(candidate["weight"])
    eyesight = float(candidate["eyesight"])
    education = candidate["education"]
    english_language = candidate["english_language"]

    if 20 <= age <= 59 and 150 <= height <= 190 and 50 <= weight <= 90 and eyesight == 1.0 and (
        education == "Master" or education == "PhD"
    ) and english_language == "true":
        return True

    return False


# Считываем директорию с файлами
directory = input("Введите путь до директории с csv файлами: ")

# Создаем список для хранения отобранных кандидатов
selected_candidates = []

# Проходим по всем файлам в указанной директории
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        with open(os.path.join(directory, filename), "r") as file:
            csv_reader = csv.DictReader(file, delimiter="#")
            for row in csv_reader:
                if check_criteria(row):
                    selected_candidates.append(row)

# Сортируем отобранных кандидатов по критериям
selected_candidates.sort(
    key=lambda x: (
        27 <= int(x["age"]) <= 37,  # Приоритет кандидатам в возрасте от 27 до 37 лет
        float("inf") if 27 <= int(x["age"]) <= 37 else -int(x["age"]),  # Люди старше 37 сортируются по алфавиту по убыванию возраста
        x["name"] + " " + x["surname"],  # Сортировка по алфавиту имя + фамилия
    )
)
 
# Записываем отобранных кандидатов в новый csv файл
with open(os.path.join(directory, "result.csv"), "w", newline="") as file:
    csv_writer = csv.writer(file, delimiter="#")
    for candidate in selected_candidates:
        csv_writer.writerow(
            [
                candidate["id"],
                candidate["name"],
                candidate["surname"],
                candidate["height"],
                candidate["weight"],
                candidate["education"],
            ]
        )

print("Готово! Файл result.csv с отобранными кандидатами создан.")
