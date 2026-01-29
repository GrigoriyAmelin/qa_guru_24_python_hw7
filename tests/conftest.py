import os
from zipfile import ZipFile

import pytest


@pytest.fixture(scope='function')
def zip_files():
    current_directory_path = os.path.dirname(os.path.abspath(__file__))
    resources_directory_path = os.path.join(current_directory_path, 'resources')
    pdf_file_path = os.path.join(resources_directory_path, 'pdf_example.pdf')
    xlsx_file_path = os.path.join(resources_directory_path, 'xlsx_example.xlsx')
    csv_file_path = os.path.join(resources_directory_path, 'csv_example.csv')
    zip_archive_path = os.path.join(resources_directory_path, 'zip_archive.zip')

    with ZipFile(zip_archive_path, mode='w') as zip_archive:
        zip_archive.write(filename=pdf_file_path, arcname="data/pdf_example.pdf")
        zip_archive.write(filename=xlsx_file_path, arcname="data/xlsx_example.xlsx")
        zip_archive.write(filename=csv_file_path, arcname="data/csv_example.csv")
        print(f'\nАрхив создан: {zip_archive.namelist()}')

    yield zip_archive_path

    os.remove(zip_archive_path)