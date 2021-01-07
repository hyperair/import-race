# POC for import race condition when iterating over module globals

## Test run

```
% python3 main.py
[2021-01-07 19:42:36,339]   Thread-1: before import
[2021-01-07 19:42:36,340]   Thread-2: before import
[2021-01-07 19:42:36,341]   Thread-3: before import
[2021-01-07 19:42:36,341]   Thread-4: before import
[2021-01-07 19:42:36,342]   Thread-5: before import
[2021-01-07 19:42:36,342]   Thread-6: before import
[2021-01-07 19:42:36,342]   Thread-7: before import
[2021-01-07 19:42:36,342]   Thread-8: before import
[2021-01-07 19:42:36,342]   Thread-9: before import
[2021-01-07 19:42:36,343]  Thread-10: before import
[2021-01-07 19:42:37,008]   Thread-1: before loop: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals']
[2021-01-07 19:42:37,009]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'x']
[2021-01-07 19:42:38,010]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'x']
[2021-01-07 19:42:38,010]   Thread-1: caught exception: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'x', 'e']
Traceback (most recent call last):
  File "/home/hyperair/src/import-race/slow_module.py", line 22, in <module>
    for x in globals():
RuntimeError: dictionary changed size during iteration
[2021-01-07 19:42:38,010]   Thread-1: after import
[2021-01-07 19:42:38,011]   Thread-2: after import
[2021-01-07 19:42:38,011]   Thread-3: after import
[2021-01-07 19:42:38,011]   Thread-4: after import
[2021-01-07 19:42:38,011]   Thread-5: after import
[2021-01-07 19:42:38,011]   Thread-6: after import
[2021-01-07 19:42:38,011]   Thread-7: after import
[2021-01-07 19:42:38,012]   Thread-8: after import
[2021-01-07 19:42:38,012]   Thread-9: after import
[2021-01-07 19:42:38,012]  Thread-10: after import

```
