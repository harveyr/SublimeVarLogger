SublimeVarLogger
=========

This is a plugin for Sublime Text 3 that generates a line of code to log the variable that you have selected.

For a **Python** example, if you have selected `wicked_var` in the following line:

`def awesome_func(wicked_var):`

The output would be:

`print('wicked_var: {v}'.format(v=wicked_var))`

...on a new line, properly indented. (If you are using the logging module, it will try to find the name of your logger object and use `<loggername>.debug()` instead.)

Or in **Javascript**:

`console.log('wicked_var:', wicked_var);`

Also works in **Go** (`log.Print()`), **PHP** (`var_dump()`), and **CoffeeScript** (`console.log`).

Comments are welcome!
