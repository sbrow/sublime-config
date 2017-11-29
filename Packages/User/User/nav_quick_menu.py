import sublime
import sublime_plugin
import functools

class QuickPanelUpCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command("move", {"by": "lines", "forward": False})

class QuickPanelDownCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command("move", {"by": "lines", "forward": True})