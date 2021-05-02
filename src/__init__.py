import config
from discord.ext.commands import Bot as botBase
from discord import Embed
from datetime import datetime

COGS = ["parser", "clgen", "pdfmerger", "cvedit"]

class Bot(botBase):
    def __init__(self):
        self.ready = False
        super().__init__(command_prefix=config.BOT_PREFIX)

    def setup(self):
      print(COGS)
      for cog in COGS:
        self.load_extension(f"src.cogs.{cog}")
        print(f" {cog} cog loaded")

    def run(self):
      print("running setup...")
      self.setup()
      
      print("running bot...")
      super().run(config.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print("bot ready")
            channel = self.get_channel(838523813414961174)
            embed = Embed(title="Now Online!", description="lumos is now online.",
                          colour=0xFF0000, timestamp=datetime.utcnow())
            fields = [("!parse", "Parses a resume and returns a result in .json and formatted text.\nParameters: <.pdf attachment>", False), ("!edit", "Edits a cover letter for grammatical errors returns a result in formatted text.\nParameters: <.docx/.pdf/.txt attachment>", False), ("!merge", "Creates a .pdf file with all all .pdfs in the .zip merged \nParameters: filename <.zip attachment>", False), ("!generate", "Generates a cover letter with with the tags replaced with it's values\nParameters:\n{TAG1}=text1\n{TAG2}=text2\n...\n<.pdf attachment>", False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_footer(text="RUHacks 2021")
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/838162213566021682/838190098654822460/unknown.png")
            await channel.send(embed=embed)
        else:
            print("bot reconnected")


bot = Bot()
