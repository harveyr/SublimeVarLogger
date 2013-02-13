varlogger
=========
**work in progress**

This is a little plugin for Sublime Text that quickly generates the code to log the variable that you have selected.

For a python example, if you have selected *wicked_var* in the following line:

```python
awesome_func(wicked_var)
```

The output would be:

```python
logger.debug('wicked_var: ' + str(wicked_var))
```

on a new line, properly indented.

Or in javascript:

```js
console.log('wicked_var:', wicked_var);
```

In PHP, it uses var_dump. And so on.
