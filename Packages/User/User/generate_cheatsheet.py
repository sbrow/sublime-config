import sublime
import sublime_plugin


class GenerateCheatsheet(sublime_plugin.WindowCommand):
    def run(self):
        commands = open("/home/sbrow/.config/sublime-text-3/Packages/User/UserCommands.sublime-commands")
        cheat = open("/home/sbrow/.config/sublime-text-3/Packages/User/subl.cheatsheet", "w")
        cmds = commands.read().split("\n");
        commands.close()
        cheat.write(">\t Cheatsheet\n>\t\t Spencer's Cheatsheet for Sublime Text 3.\n")
        cheat.write("\n>\t Ex Commands\n>\t\t These can be invoked from the command palette.\n")
        for line in cmds:
            index = line.find(" * ")
            if index != -1:
                cheat.write("\n>\t\t " + line[index+3:] + "\n")
            index = line.find("caption")
            if index != -1:
                cheat.write(line[index+11:line.find(" - ")] + " \t " + 
                            line[line.find(" - ")+3:line.find(",")-1] + "\n")
        cheat.close()