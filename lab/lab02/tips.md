lab02/Q8: I Heard You Liked Functions...

Python treats variables in functions differently depending on whether you assign values to them from inside or outside the function. If a variable is assigned within a function, it is treated by default as a local variable. Therefore, when you uncomment the line, you are trying to reference the local variable before any value has been assigned to it.

```python
nonlocla n
```

> reference:https://stackoverflow.com/questions/370357/unboundlocalerror-trying-to-use-a-variable-supposed-to-be-global-that-is-rea