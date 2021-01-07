# POC for import race condition when iterating over module globals

## Test run

```
% python3 main.py
Traceback (most recent call last):
  File "/home/hyperair/src/import-race/slow_module.py", line 14, in <module>
    for x in globals():
RuntimeError: dictionary changed size during iteration
Thread-1: before import
Thread-2: before import
Thread-3: before import
Thread-4: before import
Thread-5: before import
Thread-6: before import
Thread-7: before import
Thread-8: before import
Thread-9: before import
Thread-10: before import
Thread-1: before loop ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'random', 'threading', 'traceback', 'time', 'foo', 'bar', 'baz', 'asdf']
Thread-1: before sleep ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'random', 'threading', 'traceback', 'time', 'foo', 'bar', 'baz', 'asdf', 'x']
Thread-1: during loop ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'random', 'threading', 'traceback', 'time', 'foo', 'bar', 'baz', 'asdf', 'x']
Thread-1: caught exception ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'random', 'threading', 'traceback', 'time', 'foo', 'bar', 'baz', 'asdf', 'x', 'e']
Thread-1: after import
Thread-2: after import
Thread-3: after import
Thread-4: after import
Thread-5: after import
Thread-6: after import
Thread-7: after import
Thread-8: after import
Thread-9: after import
Thread-10: after import
```
