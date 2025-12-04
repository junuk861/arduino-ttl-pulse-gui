# Arduino TTL Pulse GUI

This repository contains a simple Python-based GUI for generating TTL pulse trains using an Arduino Uno.  
It was developed to synchronize fluorescence imaging hardware—such as sCMOS cameras and LED illumination systems—for experiments including Fluo-4 and Fura-2 calcium imaging.

The GUI is built using `tkinter` and communicates with the Arduino via `pyfirmata`.  
It is a lightweight, single-file solution for precise timing control during live-cell imaging.

---

## Features

- Intuitive graphical user interface (start/stop toggle)
- Two independent TTL outputs  
  - **TTL1 → D2**  
  - **TTL2 → D4**
- User-defined TTL pulse duration (ms)
- User-defined interval between pulses (ms)
- On-screen counter for the number of TTL pulses emitted
- Minimal dependencies and easy installation
- Designed for live-cell imaging synchronization (camera ↔ LED ↔ acquisition software)

---

## Hardware Requirements

- **Arduino Uno** (or any Firmata-compatible Arduino board)
- USB cable
- Devices capable of receiving **5 V TTL input**  
- TTL wiring:
  - **D2 → TTL1**
  - **D4 → TTL2**

Before running the GUI, upload **StandardFirmata** to the Arduino:

1. Open **Arduino IDE**
2. Go to: `File → Examples → Firmata → StandardFirmata`
3. Select the correct board and port
4. Click **Upload**

This enables Python to communicate with the Arduino via the Firmata protocol.

---

## Software Requirements

- Python **3.8 or later**
- `pyfirmata`  
- `tkinter` (included with most Python installations)

Install Python dependencies:

```bash
pip install pyfirmata
```

---

## Usage

1. **Connect the Arduino Uno** to your computer via USB.

2. **Set your Arduino serial port** in the script:

```python
board = pyfirmata.Arduino('COM6')   # Example for Windows
```

Typical port examples:
- Windows → `COM3`, `COM6`, ...
- macOS → `/dev/tty.usbmodemXXXX` or `/dev/ttyACM0`

3. **Run the GUI:**

```bash
python arduino_ttl_pulse_gui.py
```

4. **Using the GUI:**
   - Set **TTL Duration (ms)** (e.g., 30)
   - Set **Interval (ms)** between pulses (e.g., 1000)
   - Click **Toggle TTL ON/OFF** to start or stop pulse generation

**Pulse behavior:**
- TTL pins go HIGH for the specified duration  
- Then LOW for the interval  
- This repeats until you stop the pulse train

---

## Example Imaging Setup

A typical configuration for calcium imaging:

```
TTL1 (D2) → Camera exposure trigger input  
TTL2 (D4) → LED controller or excitation system trigger  
```

This setup synchronizes:
- Camera exposure  
- LED illumination  
- Frame timing in Micro-Manager or similar software  

It allows stable, reproducible timing important for ratiometric or time-resolved fluorescence imaging.

---

## Citation / Acknowledgment

If this GUI is used in published work, please cite or acknowledge as follows:

> “TTL timing for fluorescence imaging synchronization was controlled by a custom Python GUI using an Arduino Uno (J. Lee, Northwestern University). Source code available at: https://github.com/junuk861/arduino-ttl-pulse-gui”

---

## Author

**Junuk Lee**  
Northwestern University  
Developer of electrophysiology and imaging synchronization tools

For questions or contributions, feel free to open an issue or pull request.

