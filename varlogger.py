# http://www.sublimetext.com/docs/commands
# http://www.sublimetext.com/docs/2/api_reference.html

import sublime, sublime_plugin
import re

class LogvarCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.insert_with_newline(edit, 'testme')
        var_name = self.get_cursor_word()
        if var_name is not None:
            self.insert_with_newline(edit, self.log_str(var_name))

    def log_str(self, var_name):
        ws = self.leading_whitespace()

        if self.in_python():
            return (
                "{0}logger.debug('{1}:')\n" +
                "{0}logger.debug({1})\n").format(ws, var_name)

        if self.in_php():
            return (
                "{0}var_dump('{1}:');\n" +
                "{0}var_dump({1});\n").format(ws, var_name)

    def insert_with_newline(self, edit, text):
        view = self.active_view()
        eol = view.line(view.sel()[0]).end()
        self.view.insert(edit, eol, "\n{}".format(text))
        # self.view.insert(edit, eol, "\n")
        # view.run_command('insertAndDecodeCharacters', 'blah')

    def get_cursor_word(self):
        view = self.active_view()
        word = view.substr(view.sel()[0]).strip()
        if len(word) == 0:
            return None
        return word

    def leading_whitespace(self):
        view = self.active_view()
        line = view.substr(view.line(view.sel()[0]))
        matches = re.findall(r'(\s*)\S+', line)
        return matches[0]

    def in_python(self):
        view = self.active_view()
        return 'python' in self.current_scope()

    def in_php(self):
        view = self.active_view()
        return 'source.php' in self.current_scope()

    def current_scope(self):
        return self.active_view().scope_name(0)

    def active_view(self):
        return sublime.active_window().active_view()
