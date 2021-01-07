# POC for import race condition when iterating over module globals

## Test run

```
$ python3 main.py
[2021-01-07 19:48:14,516]   Thread-1: before import
[2021-01-07 19:48:14,518]   Thread-2: before import
[2021-01-07 19:48:14,518]   Thread-3: before import
[2021-01-07 19:48:14,518]   Thread-4: before import
[2021-01-07 19:48:14,518]   Thread-5: before import
[2021-01-07 19:48:14,518]   Thread-6: before import
[2021-01-07 19:48:14,519]   Thread-7: before import
[2021-01-07 19:48:14,519]   Thread-8: before import
[2021-01-07 19:48:14,519]   Thread-9: before import
[2021-01-07 19:48:14,519]  Thread-10: before import
[2021-01-07 19:48:15,179]   Thread-1: before loop: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:15,179]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:16,120]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:16,120]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:16,658]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:16,658]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:17,506]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:17,506]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:18,171]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:18,171]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:18,517]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:18,517]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:19,306]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:19,306]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:19,604]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:19,605]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:20,600]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:20,600]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:20,646]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:20,646]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:21,554]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:21,554]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:22,269]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:22,270]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:22,726]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:22,726]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:22,899]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:22,899]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:23,645]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:23,645]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,109]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,109]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,459]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,459]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,613]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,613]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,950]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:24,950]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:25,430]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:25,431]   Thread-1: in loop before sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:26,066]   Thread-1: in loop after sleep: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'logging', 'random', 'threading', 'traceback', 'time', 'logger', 'foo', 'bar', 'baz', 'asdf', 'list_globals', 'run_loop']
[2021-01-07 19:48:26,066]   Thread-1: after import
[2021-01-07 19:48:26,067]   Thread-2: after import
[2021-01-07 19:48:26,067]   Thread-3: after import
[2021-01-07 19:48:26,068]   Thread-4: after import
[2021-01-07 19:48:26,068]   Thread-5: after import
[2021-01-07 19:48:26,068]   Thread-6: after import
[2021-01-07 19:48:26,069]   Thread-7: after import
[2021-01-07 19:48:26,069]   Thread-8: after import
[2021-01-07 19:48:26,070]   Thread-9: after import
[2021-01-07 19:48:26,070]  Thread-10: after import

```
