import zipfile as z
import pathlib as p


def zip_archive(files, destination, name):
    """
    Compress files into ZIP to a destination path.
    :param files: filepath with files to be compressed.
    :type files: list
    :param destination: destination path to compressed file.
    :type destination: str
    :param name: name of the compressed file
    :type name: str
    """
    dest_path = p.Path(destination, f'{name}.zip')

    with z.ZipFile(dest_path, 'w') as zip_file:
        for filepath in files:
            filepath = p.Path(filepath)
            zip_file.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    pass
    # zip_archive(['test_files/a.txt'], 'test_files', 'compressed')
