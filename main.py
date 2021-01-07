import threading


def import_slow_module():
    print(f'{threading.current_thread().name}: before import')
    import slow_module
    print(f'{threading.current_thread().name}: after import')


threads = [threading.Thread(target=import_slow_module) for _ in range(10)]
for t in threads:
    t.start()

for t in threads:
    try:
        t.join()
    except Exception:
        pass
