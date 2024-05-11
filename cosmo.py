import os
import csv
import zipfile

# Функция для проверки критериев отбора
def check_criteria(candidate):
    age = int(candidate[3])
    height = int(candidate[4])
    weight = int(candidate[5])
    eyesight = float(candidate[6])
    education = candidate[7]
    english_language = candidate[8]

    if 20 <= age <= 59 and 150 <= height <= 190 and 50 <= weight <= 90 and eyesight == 1.0 and (education == "Master" or education == "PhD") and english_language == "true":
        return True
    return False

# Считываем директорию с файлами
directory = input("Введите путь до директории с csv файлами и zip архивами: ")

# Создаем список для хранения отобранных кандидатов
selected_candidates = []

# Проходим по всем файлам в указанной директории
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        with open(os.path.join(directory, filename), "r", newline='') as file:
            csv_reader = csv.reader(file, delimiter='#')
            next(csv_reader)  # Пропускаем заголовок

            for row in csv_reader:
                if check_criteria(row):
                    selected_candidates.append(row)
    
    elif filename.endswith(".zip"):
        with zipfile.ZipFile(os.path.join(directory, filename), "r") as zip_ref:
            zip_files = zip_ref.namelist()
            for zip_file in zip_files:
                if zip_file.endswith(".csv"):
                    with zip_ref.open(zip_file, "r") as file:
                        csv_reader = csv.reader(file, delimiter='#')
                        next(csv_reader)  # Пропускаем заголовок

                        for row in csv_reader:
                            if check_criteria(row):
                                selected_candidates.append(row)

# Сортируем отобранных кандидатов по критериям
selected_candidates.sort(key=lambda x: (27 <= int(x[3]) <= 37, x[1], x[2]))

# Записываем отобранных кандидатов в новый csv файл
with open(os.path.join(directory, "result.csv"), "w", newline='') as file:
    csv_writer = csv.writer(file, delimiter='#')
    csv_writer.writerow(["id", "name", "surname", "height", "weight", "education"])

    for candidate in selected_candidates:
        csv_writer.writerow([candidate[0], candidate[1], candidate[2], candidate[4], candidate[5], candidate[7]])

print("Готово! Файл result.csv с отобранными кандидатами создан.")
