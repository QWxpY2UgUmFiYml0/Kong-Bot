from disco.bot import Plugin
import random

###How to turn the damn thing on###
#python -m disco.cli --config config.json

class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')

class Help(Plugin):
    @Plugin.command('!help')
    def send_help(self, event):
        event.msg.reply("To hear me say dumbass monkey lines, blurt out Christian's favorite synonym for apes.")

class HardR(Plugin):
    @Plugin.listen('MessageCreate')
    def on_hard_r(self, event):
        if "nigger" in event.message.content:
            event.reply("Whoa there buddy")

class RollDie(Plugin):
    @Plugin.command('roll', '<num:int> <sides:int>')
    def roll_die(self, event, num, sides):
        event.msg.reply('rolling ''{}''d''{}''\n''{}'.format(num, sides, roll(num, sides)))

def roll(num, sides):
    list = []
    for n in range(num):
        list.insert(n, random.randint(1, sides))
    return list


        