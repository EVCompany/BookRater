#!/usr/bin/env python3

import src.pdf_console_interface as pi
import time
import sys


PAGES_OUTPUT_TEXT = "Страниц в документе: "
CHAPTERS_OUTPUT_TEXT = "Глав в документе: "
PICTURES_OUTPUT_TEXT = "Рисунков в документе: "
YEAR_OUTPUT_TEXT = "Год: "
LITCOUNT_OUTPUT_TEXT = "Количество использованной литературы: "
PICTURES_PER_PAGE_TEXT = "Количество рисунков на страницу: "
CHAPTERS_DEVIATION_TEXT = "Отклонение кол-ва глав от 'идеального': "
COUNT_OF_SYMBOLS_TEXT = "Частотное распределение символов: "
COUNT_OF_WORDS_TEXT = "Частотное распределение слов: "
COUNT_OF_PAGES_IN_CHAPTERS = "Количество страниц в главах: "
PERCANTAGE_OF_PAGES_IN_CHAPTERS = "Процент страниц в главах: "

def print_metrics(pdf):
    metrics = pdf.get_metrics()
    print(PAGES_OUTPUT_TEXT + str(metrics[0]) + "\n" +
          PICTURES_OUTPUT_TEXT + str(metrics[1]) + "\n" +
          CHAPTERS_OUTPUT_TEXT + str(metrics[2]) + "\n" +
          CHAPTERS_DEVIATION_TEXT + str(metrics[5]) + "\n" +
          YEAR_OUTPUT_TEXT + str(metrics[4]) + "\n" +
          LITCOUNT_OUTPUT_TEXT + str(metrics[3]) + "\n" +
          PICTURES_PER_PAGE_TEXT + str(metrics[6]) + "\n" +
          COUNT_OF_SYMBOLS_TEXT + str(metrics[7]) + "\n" +
          COUNT_OF_WORDS_TEXT + str(metrics[8]) + "\n" +
          COUNT_OF_PAGES_IN_CHAPTERS + str(metrics[9]) + "\n" +
          PERCANTAGE_OF_PAGES_IN_CHAPTERS + str(metrics[10]) + "\n"
          )

def main():
    start = time.time()
    pdf = pi.PdfConsoleInterface()
    file_name = sys.argv[1]
    pdf.load_file(file_name)
    print_metrics(pdf)
    pdf.close_file()
    end = time.time()
    print("Время обработки --- %s секунд ---" % (end - start))
    
if __name__ == '__main__':
    main()
