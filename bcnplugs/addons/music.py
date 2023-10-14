from bcnplugs.addons.help import add_command

module_name = "Help"
commands = [
    ("/help", "help"),
    ("/ghelp", "ghelp"),
]
add_command(module_name, commands)
