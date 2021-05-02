import os, glob, json, requests, io, sys
from discord import File
from discord.ext.commands import Cog
from discord.ext.commands import command


class Parser(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command()
    async def parse(self, ctx):
      await ctx.message.attachments[0].save("./src/cogs/in/in.pdf", seek_begin=True, use_cached=False)
      file  = glob.glob('./src/cogs/in/in.pdf')[0]
      url = 'https://jobs.lever.co/parseResume'
      resume = open(file, 'rb')
      response = requests.post(url, files={'resume': resume}, headers={'referer': 'https://jobs.lever.co/', 'origin': 'https://jobs.lever.co/'}, cookies={'lever-referer': 'https://jobs.lever.co/'})
      parsed = json.dumps(response.json(), indent=4)
      res = open("./src/cogs/out/out.json", 'w')
      res.write(parsed)
      res.close()
      await ctx.send(file= File(r'./src/cogs/out/out.json'))
      output = get_all_values2(response.json())
      print("****************************************")
      print(output)
      await ctx.send("```\n" + output[0:1980] + "\n```")
      await ctx.send("```\n" + output[1981:3900] + "\n```")
    @Cog.listener()
    async def on_ready(self):
        print("parser is ready!")
    
def get_all_values2(nested_dictionary):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values2(value)
        elif key == "names":
            print(key, ":", value[0])
        elif type(value) is list:
            print(key, "--:")
            get_all_values2(value[0])

        else:
            print(key, ":", value)
    output = new_stdout.getvalue()

    sys.stdout = old_stdout
    print(output)
    return(output)

        



def setup(bot):
	bot.add_cog(Parser(bot))
