import src.pdf_console_interface as pi


def main():
    pdf = pi.PdfConsoleInterface()
    pdf.load_file("/Users/egor/Documents/prog/python/practice/example.pdf")
    print(pdf.get_number_of_pages())
    pdf.close_file()


if __name__ == '__main__':
    main()
