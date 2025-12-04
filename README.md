# Arduino TTL Pulse GUI

This repository provides a simple Python GUI to generate TTL pulses using an Arduino Uno board for synchronizing fluorescence imaging hardware (e.g., camera exposure and LED illumination).

The GUI is built using `tkinter` and communicates with the Arduino via `pyfirmata`.  
It was originally developed for Fluo-4 and Fura-2 calcium imaging experiments.

---

## Features
- Graphical interface (start/stop toggle)
- Two independent TTL outputs  
  - **TTL1 → D2**, **TTL2 → D4**
- User-defined pulse duration (ms)
- User-defined interval between TTL pulses (ms)
- On-screen counter for emitted pulses
- Single-file Python script

---

## Hardware Requirements
- **Arduino Uno** (or any Firmata-compatible board)
- USB cable
- Devices accepting **5 V TTL inputs**
- TTL wiring:
  - D2 → TTL1
  - D4 → TTL2

Before running the GUI, upload **StandardFirmata** to the Arduino:

1. Open Arduino IDE  
2. File → Examples → Firmata → **StandardFirmata**
3. Select board + port  
4. Upload

---

## Software Requirements
- Python 3.8+
- `pyfirmata`
- `tkinter` (included with Python)

Install dependencies:

```bash
pip install pyfirmata
