from bcnplugs.addons.help import add_command

module_name = "Music"
commands = [
    ("/play", "play"),
    ("/vplay", "vplay"),
]
add_command(module_name, commands)
