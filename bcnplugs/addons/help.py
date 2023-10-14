from pyrogram import Client
from pyrogram.types import Message

CMD_HELP = {}

def add_command(module_name, commands):
    if module_name in CMD_HELP:
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}
    for command in commands:
        if len(command) == 2:  # Ensure each command has a name and description
            command_name, command_description = command
            command_dict[command_name] = command_description
    CMD_HELP[module_name] = command_dict

module_name = "help"
commands = [("/help", "Description of command 1"), ("/ghelp", "Description of command 2")]

add_command(module_name, commands)
