import src.pdf_console_interface as pi
import time


PAGES_OUTPUT_TEXT = "Страниц в документе: "
CHAPTERS_OUTPUT_TEXT = "Глав в документе: "
PICTURES_OUTPUT_TEXT = "Рисунков в документе: "
YEAR_OUTPUT_TEXT = "Год: "
LITCOUNT_OUTPUT_TEXT = "Количество использованной литературы: "

def print_metrics(pdf):
    metrics = pdf.get_metrics()
    print(PAGES_OUTPUT_TEXT + str(metrics[0]) + "\n" +
          PICTURES_OUTPUT_TEXT + str(metrics[1]) + "\n" +
          CHAPTERS_OUTPUT_TEXT + str(metrics[2]) + "\n" +
          YEAR_OUTPUT_TEXT + str(metrics[4]) + "\n" +
          LITCOUNT_OUTPUT_TEXT + str(metrics[3]) + "\n")

def main():
    start = time.time()
    pdf = pi.PdfConsoleInterface()
    pdf.load_file("/Users/egor/Documents/prog/python/practice/FIRST_PROG_ALG.pdf")
    print_metrics(pdf)
    pdf.close_file()
    end = time.time()
    print("Время обработки --- %s секунд ---" % (end - start))
    
if __name__ == '__main__':
    main()
