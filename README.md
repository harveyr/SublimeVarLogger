varlogger
=========
*work in progress*

This is a little plugin for Sublime Text that quickly generates the code to log the variable under your cursor.

For a python example, if your cursor is the pipe on the following line:

```python
awesome_func(wicked_var|)
```

The output would be:

```python
logger.debug('wicked_var:')
logger.debug(wicked_var)
```

on new lines, properly indented.

Or in javascript:

```js
console.log('wicked_var:', wicked_var);
```

And so on.
