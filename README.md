SublimeVarLogger
=========

This is a plugin for Sublime Text that generates a line of code to log the variable that you have selected.

For a python example, if you have selected *wicked_var* in the following line:

`python awesome_func(wicked_var)`

The output would be:

`python logger.debug('wicked_var: ' + str(wicked_var))`

on a new line, properly indented.

(If you have imported logging, that is. Otherwise it will use print).

Or in javascript:

`js console.log('wicked_var:', wicked_var);`

Also works in PHP (`var_dump()`) and CoffeeScript (`console.log`).
