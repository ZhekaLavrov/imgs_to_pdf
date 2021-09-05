import img2pdf
from PIL import Image


def resize_to_a4(input_file_name, output_file_name):
    """
    Если изображение больше чем А4, то уменьшает его пропорционально до А4
    :param input_file_name: Путь к входящему файлу
    :param output_file_name: Путь к готовому файлу
    """
    image = Image.open(input_file_name)
    new_file_name = output_file_name
    new_size = (2480, 3508)
    if image.size[0] > new_size[0] or image.size[1] > new_size[1]:
        ratio = min(float(new_size[0]) / image.size[0], float(new_size[1]) / image.size[1])
        w = int(image.size[0] * ratio)
        h = int(image.size[1] * ratio)
        resized = image.resize((w, h), Image.ANTIALIAS)
        resized.save(new_file_name, format='JPEG', quality=85, optimize=True)
    else:
        image.save(new_file_name, format='JPEG', quality=85, optimize=True)


def to_pdf(input_files: list, output_file_name):
    """
    Конвертирует любое количество изображений в pdf
    :param input_files: Список входящих файлов
    :param output_file_name: Сгенерированный pdf файл
    """
    a4_page_size = [img2pdf.in_to_pt(8.3), img2pdf.in_to_pt(11.7)]
    layout_function = img2pdf.get_layout_fun(a4_page_size)

    pdf = img2pdf.convert(
        input_files,
        layout_fun=layout_function
    )
    with open(output_file_name, 'wb') as f:
        f.write(pdf)
