# Pre-commit OOP hooks

A set of pre-commit hooks aiming to detect if certain object oriented programming rules are followed. Those rules are from the oop course at the PUT university in Poland.

The rules that this pre-commit hook ought to check are the following:

- [ ] There should be no functions which are not object methods (utils functions)
- [X] There should be no classes which end with the suffix "er" 
    - [X] Methods should be exempt from this rule [see here](https://www.wordmom.com/verbs/that-end-with-er)
    - [X] Interfaces are exempt from this rule
- [ ] Getters and Setters should not be allowed (`getValue()`, `setPrimaryKey()`), although library functions (those imported from libraries) are exempt from this rule (`getline()` in C++)

Optionally:

- [ ] Mutator functions should be named with a verb
- [ ] Accessor functions should be named with a noun
