import src.pdf_console_interface as pi


def main():
    pdf = pi.PdfConsoleInterface()
    pdf.load_file("/Users/vetas/example.pdf")
    pdf.print_metrics()
    #print(pdf.get_number_of_pages())
    #text = pdf.get_text()
    #print(text)
    #print(pdf.get_number_of_pictures())
    #pdf.close_file()


if __name__ == '__main__':
    main()
