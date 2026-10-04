# IR Keyfob Intercom Controller

This project is a starter Python implementation for using an IR keyfob to trigger the door-release circuit of a traditional wired intercom.

It assumes a Raspberry Pi connected to:
- an IR receiver module (for example, a 38 kHz IR sensor)
- a relay module connected to the intercom's door release line

The controller listens for a configured IR keyfob code and then briefly energizes the relay to simulate the door unlock signal.

## Hardware assumptions

- IR receiver connected to GPIO 17
- Relay module connected to GPIO 27
- Relay contact wired to the intercom's door release circuit, or to a suitable dry-contact trigger
- Door release pulse duration: 2-4 seconds

## What this does

- decodes a standard NEC IR keyfob signal
- compares the received code against a configured whitelist
- triggers a relay pulse when the code matches
- logs the detected code and unlock event

## Safety warning

This project is for experimentation and controlled automation. A traditional intercom release circuit may be connected to mains voltage or to a security system. Only wire relay contacts into a circuit you understand and that is safe to control.

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Edit the target code in `app.py` to match your keyfob's real IR code.
5. Run the program:

```bash
python app.py
```

6. Press the keyfob button and test the relay output.

## Example output

```text
Waiting for IR signal...
Received code: 0x1FE48B7
MATCHED allowed code: 0x1FE48B7
Unlocking intercom relay for 3 seconds...
Door release triggered.
```

## Notes

- NEC is the most common protocol for simple IR remotes, but some remotes use Sony, RC5, or proprietary encoding.
- If your keyfob is not NEC, update the decoder in `app.py` to match your protocol.
- If you want the relay pulse to mimic an actual door-release contact, use a relay with the correct contact arrangement for your intercom.

## Repository files

- `app.py` — main logic and signal processing
- `requirements.txt` — Python dependencies
- `README.md` — overview
