import src.pdf_console_interface as pi

PAGES_OUTPUT_TEXT = "Страниц в документе: "
CHAPTERS_OUTPUT_TEXT = "Глав в документе: "
PICTURES_OUTPUT_TEXT = "Рисунков в документе: "

def main():
    pdf = pi.PdfConsoleInterface()
    pdf.load_file("/Users/egor/Documents/prog/python/practice/example.pdf")
    print(PAGES_OUTPUT_TEXT + str(pdf.get_number_of_pages()))
    print(CHAPTERS_OUTPUT_TEXT + str(pdf.get_number_of_chapters()))
    pdf.close_file()


if __name__ == '__main__':
    main()
