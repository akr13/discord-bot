from gingerit.gingerit import GingerIt
import PyPDF2
import docx
import os.path


class Corrections:

    def __init__(self, file):
        self.file = file

    def checkExtension(self):
        extension = os.path.splitext(self.file)[1]
        if extension == '.txt':
            return self.openText()
        elif extension == '.docx':
            return self.openDOC()
        elif extension == '.pdf':
            return self.openPDF()
        else:
            return 'Unknown file format. Please use either a PDF, DOC/DOCX, or text file'

    def openText(self):
        f = open(self.file, "r")
        text = f.read()
        return self.correctText(text)

    def openPDF(self):
        f = open(self.file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(f)
        text = pdfReader.getPage(0).extractText()
        return self.correctText(text)

    def openDOC(self):
        doc = docx.Document(self.file)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        text = '\n'.join(fullText)
        return self.correctText(text)

    def correctText(self, text):
        sentences = text.split(". ")
        edits = ''
        for sentence in sentences:
            result = GingerIt().parse(sentence)
            for i in range(len(result['corrections'])):
                if len(result['corrections'][i]['text']) > 1:
                    edits += '\n' + sentence
                edits += '\nText: ' + result['corrections'][i]['text']
                edits += '\nCorrection: ' + result['corrections'][i]['correct']
                edits += '\n'
        return edits