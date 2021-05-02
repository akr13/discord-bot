import zipfile, glob
from PyPDF2 import PdfFileMerger
from discord import File
from discord.ext.commands import Cog
from discord.ext.commands import command


class PDFmerger(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command()
    async def merge(self, ctx, *, message):
      await ctx.message.attachments[0].save("./src/cogs/in/in.zip", seek_begin=True, use_cached=False)
      with zipfile.ZipFile("./src/cogs/in/in.zip", 'r') as zip_ref:
        zip_ref.extractall("./src/cogs/in")

      pdfs = glob.glob("src/cogs/in/*/*.pdf")
      
      merger = PdfFileMerger()

      for pdf in pdfs:
        merger.append(pdf)
      
      merger.write('./src/cogs/out/'+ message + '.pdf')
      merger.close()

      await ctx.send(file= File(r'./src/cogs/out/' + message + '.pdf'))

    @Cog.listener()
    async def on_ready(self):
        print("pdfmerger is ready!")
    

def setup(bot):
	bot.add_cog(PDFmerger(bot))
