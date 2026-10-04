# IR keyfob intercom controller

A practical Python project for using an IR keyfob to trigger a wired intercom unlock relay.

This repository contains a starter implementation for:
- reading NEC IR remote signals from an IR receiver
- matching a configured keyfob code
- energizing a relay for a short unlock pulse

## Main script

```python
from app import main

if __name__ == "__main__":
    main()
```

## Typical wiring

- IR receiver data pin -> GPIO 17
- Relay control pin -> GPIO 27
- Relay common/NO contacts -> intercom release circuit or door strike trigger

## Important notes

- Replace the sample matching code in `app.py` with your own remote's actual code.
- This project is designed for a Raspberry Pi environment.
- Use relay contacts only in circuits that are safe to control.
