# indent-string [![Build Status](https://travis-ci.org/nickedes/indent.svg?branch=master)](https://travis-ci.org/nickedes/indent)
> Indent each line in a string

# Install

```
$ apt-get install python3-pip
$ pip install indent 
```

# Usage
```python
from indent.indent import indentation

indentation('Shadab\nZafar', '&', 3)
//=> &&&Shadab 
//=> &&&Zafar
```

# About

## indentation(string, indent, count)

### string

**Required**

Type: `string`

The string you want to indent.

### indent

**Required**

Type: `string`

The string to use for the indent.

### count

**Required**

Type: `number`
Default: `1`

How many times you want `indent` repeated.

# Todo
Make `count` as a default parameter.
