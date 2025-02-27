import sys


jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):

    try:
        with open(file_name, 'rb') as file:
            return file.read(header_length)
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}")
        return b''


def is_jpeg(file_name):

    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):

    header = read_header(file_name, max(len(gif_header1), len(gif_header2)))
    return header.startswith(gif_header1) or header.startswith(gif_header2)


def is_png(file_name):

    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):

    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print("Zadejte cestu k souboru jako argument.")
        else:
            file_name = sys.argv[1]
            print_file_type(file_name)
    except Exception as e:
        print(f"Nastala chyba: {e}")
