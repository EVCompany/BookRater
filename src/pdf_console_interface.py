from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import re
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

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
        self.document = None

    def load_file(self, path):
        self.file = open(path, 'rb')
        parser = PDFParser(self.file)
        self.document = PDFDocument(parser)
        pass

    def close_file(self):
        print("FILE CLOSED")
        pass

    def get_number_of_pages(self):
        j = 0
        for i in PDFPage.get_pages(self.file):
            j += 1
        return j

    def get_number_of_pictures(self):
        pass

    def get_number_of_chapters(self):
        a = list(filter(lambda x: len(x) > 0, re.findall(self._get_charpter_regex(), self.get_text())))
        return len(a)

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


    def _check_opened_file(self):
        return self.file is not None

    def _get_charpter_regex(self):
        return r'Глава||ГЛАВА'
