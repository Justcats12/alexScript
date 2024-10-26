# AlexScript by justcats12
This is a language I made for the fun, it's not a good programming language but you can make silly stuff and it's a nice challenge to try and make something in this language.

# Requirements

Python 3.12.7 or later, some earlier versions might also work

# Run a script

From repository folder

make a script first or use an example from the /scripts/ folder

```
python3 ./interpreter.py path/to/file
```

## Linux easier sytax

```
chmod u+x ./interpreter.py
```
From now no longer need the python3
```
./interpreter.py path/to/file
```

# Syntax

- `END` program end
- `JUMP <line>` jump to line
- `JUMP NEXT|PREV` jump to the next or previous line
- `SET INT|BOOL|STR <name> = <value>` set a vareable
- `SUM <varname> <x> <y> <z> ...` make a new vareable that is a sum of x y z ...
- access a vareable with `@<varname>`
- `PRINT <anything>` print to terminal
- `INPUT INT|BOOL|STR <varname>` input into vareable
- `IF (<condition>) <line1> ELSE <line2>` if statement, jumps to line1 if true, line2 if anything else
- `LIST <name>` to create a list
- `INDEX <list> <index>` to be able to access the indexed value wiht @INDEX
- `POP <list> [<index>]` to pop a list at index
- `APPEND <list> INT|BOOL|STR <value>` to add a value to a list
- Comment with everything else, you can write `COMMENT <comment>` or `-- <comment>` or `# comment`, which ever suits you best
- That's about it