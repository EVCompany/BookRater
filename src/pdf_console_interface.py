from io import StringIO
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import re
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LTFigure
from multiprocessing import Process, Pool


class PdfConsoleInterface:

    def _file_must_be_opened(foo):
        def _check(self):
            if self._check_opened_file():
                foo(self)
            else:
                print("Method unavailable. Please, open a file")

        return _check

    def __init__(self):
        self.file = None
        self.number_of_chapters = 0
        self.number_of_pages = 0
        self.number_of_pictures = 0
        self.document = None
        self.year = 0
        self.count_of_literature = 0

    def load_file(self, path):
        self.file = open(path, 'rb')
        parser = PDFParser(self.file)
        self.document = PDFDocument(parser)

    def close_file(self):
        print("FILE CLOSED")
        pass

    def get_number_of_pages(self):
        for i in PDFPage.get_pages(self.file):
            self.number_of_pages += 1

    def get_number_of_pictures(self):
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        i = 0
        for page in PDFPage.get_pages(self.file):
            interpreter.process_page(page)
            layout = device.get_result()
            for element in layout:
                if isinstance(element, LTFigure):
                    i += 1
                    self.number_of_pictures += 1

    def get_number_of_chapters(self):
        a = list(filter(lambda x: len(x) > 0, re.findall(self._get_charpter_regex(), self.get_text())))
        print(a)
        self.number_of_chapters = len(a) // 2

    def get_literature(self):
        a = list(filter(lambda x: len(x) > 0, re.findall(self._get_literature_regex(), self.get_text())))[-1]
        print(a)

    def get_text(self):
        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        for page in PDFPage.get_pages(self.file):
            interpreter.process_page(page)

        converter.close()
        text = output.getvalue()
        output.close()

        return text

    def get_last_page_text(self):
        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        pages = []
        for page in PDFPage.get_pages(self.file):
            pages.append(page)
        interpreter.process_page(pages[-1])
        converter.close()
        text = output.getvalue()
        output.close()
        return text

    def get_year(self):
        self.year = max(map(lambda x: int(x), re.findall(self._get_literature_year_regex(), self.get_last_page_text())))


    def get_number_of_literature(self):
        self.count_of_literature = len(list(filter(lambda x: len(x) > 0, re.findall(self._get_literature_count_regex(), self.get_last_page_text()))))

    def _check_opened_file(self):
        return self.file is not None

    def _get_metrics(self):
        t1 = Process(target=self.get_number_of_chapters())
        t1.start()
        t2 = Process(target=self.get_number_of_pictures())
        t2.start()
        t3 = Process(target=self.get_number_of_pages())
        t3.start()
        t4 = Process(target=self.get_number_of_literature())
        t4.start()
        t5 = Process(target=self.get_year())
        t5.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()

    def get_metrics(self):
        self._get_metrics()
        return (self.number_of_pages, self.number_of_pictures, self.number_of_chapters, self.count_of_literature, self.year)

    def _get_charpter_regex(self):
        return r'(ГЛАВА|Глава)'

    def _get_literature_regex(self):
        return r'((Литература|литературы|ЛИТЕРАТУРА|ЛИТЕРАТУРЫ)(\n|.)*)'

    def _get_literature_count_regex(self):
        return r'\n\d{1,2}\.'

    def _get_literature_year_regex(self):
        return r'\d{4}'

