# AlexScript by justcats12
This is a language I made for the fun, it's not a good programming language but you can make silly stuff and it's a nice challenge to try and make something in this language.

# Run a script

From repository folder

make a script first or use an example from the /scripts/ folder

```
python3 ./interpreter.py path/to/file
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
- That's about it