import os
from discord import File
from discord.ext.commands import Cog
from discord.ext.commands import command
from gingerit.gingerit import GingerIt
import PyPDF2
import docx
import os.path


class CVedit(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command()
    async def edit(self, ctx):
      fname = ctx.message.attachments[0].url
      extension = os.path.splitext(fname)[1]
      source = "./src/cogs/in/in"

      await ctx.message.attachments[0].save(source+extension, seek_begin=True, use_cached=False)

      editor = Corrections(source+extension)
      result = editor.checkExtension()
      await ctx.message.channel.send('```\n'+result+'\n```')



    @Cog.listener()
    async def on_ready(self):
        print("CVedit is ready!")



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
        text.replace('!', '. ').replace('?', '. ').replace(':', '. ')
        sentences=text.split(". ")
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
    

def setup(bot):
	bot.add_cog(CVedit(bot))
