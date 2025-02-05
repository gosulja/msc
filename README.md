# msc

A lightweight scripting language interpreter written in Python.
It's purpose is nothing but a way of learning for myself or others.

# things

### 05/02/2025
written a tokenizer (lexer, scanner) and a parser.
the semantics currently follow the rules: `<id> = <stmt>`
statements can be references to identifiers, such as other variables.
and statements also refer to binop (binary operations), and numeric literals:

heres an example, take this source:
```
hello = 1 + 1 
```

the generated AST for this program would be:

```
{'kind': 'Program', 'body': [{'kind': 'VarDecl', 'name': 'hello', 'init': {'kind': 'binop', 'left': {'kind': 'NumericLiteral', 'value': 1}, 'op': '+', 'right': {'kind': 'NumericLiteral', 'value': 1}}}]}
```

as we can see here, the root AST node is of the type "Program", it has a field "body", which obviously houses our code.
then we can see our variable declaration, the name "hello" is given to it, which is correct; and the init value of the var is a binop, the left being a NumericLiteral with the value of 1, the operator being "+" and the right being the same as the left, just like in the original source. So this program has been successfully parsed.
