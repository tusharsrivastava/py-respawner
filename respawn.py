#!/usr/bin/env python
import os
import sys
import signal

def respawn(*args):
    try:
        _pid, sig = os.waitpid(0, 0)
        print(f"Received {sig} signal from child")
        if sig == 0:
            sys.exit(0)
    except Exception as e:
        pass

    os.execl(__file__, *sys.argv)
    sys.exit(0)


pid = os.fork()

if __name__ == '__main__':
    if pid == 0:
        print(f"I'm child {os.getpid()}")
        try:
            script = sys.argv[1]
            os.execl(script, *sys.argv[1:])
        except (KeyboardInterrupt, EOFError):
            pass
        except Exception:
            print("Well! Your fault now you forgot to provide a script man!")
        sys.exit(0)
    else:
        print(f"Hi I'm {os.getpid()}")

        signal.signal(signal.SIGINT, respawn)

        try:
            _pid, sig = os.waitpid(0, 0)
            print(f"\nReceived {sig} signal from child")
            if sig != 0:
                respawn()
        except (Exception, KeyboardInterrupt) as e:
            sys.exit(0)

