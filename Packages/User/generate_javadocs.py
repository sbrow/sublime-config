import sublime
import sublime_plugin
from subprocess import call

class GenerateJavadocs(sublime_plugin.WindowCommand):
    def run(self):
        call('/home/sbrow/Code/Java/generateDocs.sh');
