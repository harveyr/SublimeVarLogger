import sublime_plugin
import re


class LogVarCommand(sublime_plugin.TextCommand):
    @property
    def current_scope(self):
        return self.view.scope_name(self.view.sel()[0].begin())

    def run(self, edit):
        cursor_text = self.get_cursor_text()
        if cursor_text is not None:
            self.insert_with_newline(edit, self.log_str(cursor_text))

    def log_str(self, log_text):
        """Return the code to log the variable."""
        ws = self.leading_whitespace()
        trimmed = self.trim_quoted_output(log_text)

        if self.in_python():
            log_cmd = self.get_python_log_command()
            return ("{ws}{cmd}('{trimmed}: {{v}}'.format(v={var}))").format(
                ws=ws, cmd=log_cmd, trimmed=trimmed, var=log_text)

        if self.in_js():
            return ("{0}console.log('{1}:', {2});").format(
                ws, trimmed, log_text)

        if self.in_coffee():
            return ("{0}console.log '{1}:', {2}").format(ws, trimmed, log_text)

        if self.in_go():
            return('{0}log.Print("{1}: ", {2})'.format(ws, trimmed, log_text))

        if self.in_php():
            return (
                '{0}print("\\n-----\\n" . \'{1}:\'); ' +
                'var_dump({2}); ' +
                'print("\\n-----\\n"); ' +
                "ob_flush();").format(ws, trimmed, log_text)

    def trim_quoted_output(self, output):
        return re.sub(r'\'|\"', '', output)

    def insert_with_newline(self, edit, text):
        eol = self.view.line(self.view.sel()[0]).end()
        self.view.insert(edit, eol, "\n{}".format(text))

    def get_python_log_command(self):
        """Get the log command to use (print vs. use of logging module)."""
        match = self.view.find(r'(\w+) = logging\.getLogger', 0)
        if match.a >= 0:
            word = self.view.substr(self.view.word(match.a))
            return '{logger}.debug'.format(logger=word)
        return 'print'

    def get_cursor_text(self):
        selection_region = self.view.sel()[0]
        if selection_region.size() == 0:
            word = self.view.substr(self.view.word(selection_region.begin()))
        else:
            word = self.view.substr(self.view.sel()[0]).strip()
        return word

    def leading_whitespace(self):
        line = self.view.line(self.view.sel()[0])
        line_str = self.view.substr(line)
        matches = re.findall(r'(\s*)\S+', line_str)
        whitespace = matches[0]
        if line_str.strip()[-1] in [':', '{', '(', '[']:
            whitespace += '    '
        return whitespace

    def in_python(self):
        return 'python' in self.current_scope

    def in_php(self):
        return 'source.php' in self.current_scope

    def in_js(self):
        return 'source.js' in self.current_scope

    def in_coffee(self):
        return 'source.coffee' in self.current_scope

    def in_go(self):
        return 'source.go' in self.current_scope
