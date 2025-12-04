import pyfirmata
import tkinter as tk
import time

# Connect to Arduino (set the port to COM6)
board = pyfirmata.Arduino('COM6')  # Change to your port
ttl1_pin = board.get_pin('d:2:o')  # TTL1 pin
ttl2_pin = board.get_pin('d:4:o')  # TTL2 pin

is_ttl_active = False  # Whether TTL signal is active or not
ttl1_counter = 0  # TTL1 activation counter

# Create the GUI window
root = tk.Tk()
root.title("TTL Pulse Generator")
root.geometry("400x450")

# Function to toggle TTL ON/OFF
def toggle_ttl():
    global is_ttl_active, ttl1_counter
    if is_ttl_active:
        is_ttl_active = False
        set_ttl_state(0)  # Turn off both TTL signals
        status_label.config(text="TTL Signals OFF")
    else:
        is_ttl_active = True
        ttl1_counter = 0  # Reset the counter
        status_label.config(text="TTL Signals ON")
        pulse_ttl()

# Function to set the state of both TTL signals simultaneously
def set_ttl_state(state):
    ttl1_pin.write(state)
    ttl2_pin.write(state)

# Function to generate TTL pulse
def pulse_ttl():
    global ttl1_counter
    if is_ttl_active:
        try:
            ttl_duration = int(duration_entry.get())  # Get TTL duration from input
            pulse_interval = int(interval_entry.get())  # Get pulse interval from input
        except ValueError:
            # If input is not a number, use default values
            ttl_duration = 30
            pulse_interval = 1000

        # Turn on both TTL signals simultaneously
        set_ttl_state(1)
        ttl1_counter += 1
        counter_label.config(text=f"TTL1 Activation Count: {ttl1_counter}")

        # Turn off both TTL signals after the specified duration
        root.after(ttl_duration, lambda: set_ttl_state(0))

        # Generate the next pulse after the specified interval
        root.after(pulse_interval, pulse_ttl)

# Set up the GUI widgets
toggle_button = tk.Button(root, text="Toggle TTL ON/OFF", command=toggle_ttl)
toggle_button.pack(pady=20)

status_label = tk.Label(root, text="TTL Signals OFF", font=("Helvetica", 16))
status_label.pack(pady=10)

counter_label = tk.Label(root, text="TTL1 Activation Count: 0", font=("Helvetica", 16))
counter_label.pack(pady=10)

# TTL duration input field
duration_label = tk.Label(root, text="TTL Duration (ms):")
duration_label.pack(pady=5)
duration_entry = tk.Entry(root)
duration_entry.insert(0, "30")  # Set default value (30ms)
duration_entry.pack(pady=5)

# TTL interval input field
interval_label = tk.Label(root, text="Pulse Interval (ms):")
interval_label.pack(pady=5)
interval_entry = tk.Entry(root)
interval_entry.insert(0, "1000")  # Set default value (1000ms)
interval_entry.pack(pady=5)

# Add signature at the bottom
signature_label = tk.Label(root, text="by DuLu labs at Northwestern Univ (Junuk Lee)", font=("Helvetica", 10, "italic"))
signature_label.pack(side="bottom", pady=10)

# Run the GUI
root.mainloop()

# Close the connection to Arduino
board.exit()
