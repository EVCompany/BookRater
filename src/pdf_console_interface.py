from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class PdfConsoleInterface:

    def _file_must_be_opened(foo):
        def _check(self):
            print("WE must check function")
            if self._check_opened_file():
                foo(self)
            else:
                print("Method unavailable. Please, open a file")

        return _check

    def __init__(self):
        self.file = None

    def load_file(self, path):
        pass

    @_file_must_be_opened
    def close_file(self):
        print("FILE_CLOSED")
        pass

    def get_number_of_pages(self):
        pass

    def get_number_of_pictures(self):
        pass

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


    def _check_opened_file(self):
        return self.file is not None
