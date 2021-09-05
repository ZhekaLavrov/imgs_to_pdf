import convert
import os

if __name__ == '__main__':
    # Получение файлов
    root_dir = "input_files"
    files = os.listdir(root_dir)
    images = list(filter(lambda x: x.endswith('.jpg'), files))

    temp = []  # Временные файлы
    # Уменьшение до а4
    for i in range(len(images)):
        input_file = f"{root_dir}/{images[i]}"
        output_file = f"output_files/{i+1}"
        convert.resize_to_a4(input_file, output_file)
        temp.append(output_file)

    # Сохранение в pdf
    convert.to_pdf(temp, f"output_files/document.pdf")

    # Удаление временных файлов
    for file in temp:
        os.remove(file)

