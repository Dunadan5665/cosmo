import os
import csv
import zipfile

def check_criteria(candidate):
    age = int(candidate['age'])
    height = int(candidate['height'])
    weight = int(candidate['weight'])
    eyesight = float(candidate['eyesight'])
    education = candidate['education']
    english_language = candidate['english_language']

    if age < 20 or age > 59:
        return False
    if height < 150 or height > 190:
        return False
    if weight < 50 or weight > 90:
        return False
    if eyesight != 1.0:
        return False
    if education not in ['Master', 'PhD']:
        return False
    if english_language != 'true':
        return False

    return True

def process_zip_file(zip_path):
    candidates = []
    
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_name in zip_file.namelist():
            if file_name.endswith('.csv'):
                with zip_file.open(file_name, 'r') as file:
                    reader = csv.DictReader(file, delimiter='#')
                    for row in reader:
                        if len(row) == 9:
                            if check_criteria(row):
                                candidates.append(row)
    
    return candidates

def main():
    directory = input("Введите путь до директории с zip файлами: ")
    all_candidates = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.zip'):
            zip_candidates = process_zip_file(os.path.join(directory, filename))
            all_candidates.extend(zip_candidates)
    
    sorted_candidates = sorted(all_candidates, key=lambda x: (27 <= int(x['age']) <= 37, int(x['age']), x['name'], x['surname']))

    with zipfile.ZipFile(os.path.join(directory, 'result.zip'), 'w') as archive:
        with archive.open('result.csv', 'w') as file:
            writer = csv.writer(file, delimiter='#')
            writer.writerow(['id', 'name', 'surname', 'height', 'weight', 'education', 'age'])
            for candidate in sorted_candidates:
                writer.writerow([candidate['id'], candidate['name'], candidate['surname'], candidate['height'], candidate['weight'], candidate['education'], candidate['age']])

    print("Результат сохранен в файл result.zip")

if __name__ == "__main__":
    main()
