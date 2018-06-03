from disco.bot import Plugin


class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')

class Help(Plugin):
    @Plugin.command('!help')
    def send_help(self, event):
        event.msg.reply("To hear me say dumbass monkey lines, blurt out Christian's favorite synonym for apes.")