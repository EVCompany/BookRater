from io import StringIO
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LTImage, LTCurve, LTFigure, LTRect


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
        print("FILE_CLOSED")
        pass

    def get_number_of_pages(self):
        j = 0

        for i in PDFPage.get_pages(self.file):
            j += 1
        return j

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
        return i

    def get_number_of_chapters(self):
        pass

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

    def print_metrics(self):
        print("Количество страниц : " + str(self.get_number_of_pages()) + "\n" +
              "Количество изображений : " + str(self.get_number_of_pictures()) + "\n" +
              "Количество глав : " + str(self.get_number_of_chapters()))



    def _check_opened_file(self):
        return self.file is not None
