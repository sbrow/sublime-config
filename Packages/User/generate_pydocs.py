import sublime
import sublime_plugin
from subprocess import call

class GeneratePydocs(sublime_plugin.WindowCommand):
    def run(self):
        call('/home/sbrow/Code/Python/gen_py_docs.sh')