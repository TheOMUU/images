[![Interface RFID Module RC522 with Raspberry Pi 4 - The Engineering Projects](https://images.openai.com/thumbnails/url/UPp5cHicu1mUUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw5xyrDUDXc2cS2MSi7McqtMKvY3zk12DTBJNigyLjAzsDQLL_ROKc4rtsgLsMhMDElJrQxI9_VyLvRWKwYAsa0o4Q)](https://www.theengineeringprojects.com/2023/01/interface-rfid-module-rc522-with-raspberry-pi-4.html?utm_source=chatgpt.com)

To interface an RFID module (such as the RC522) with a Raspberry Pi, you can follow these steps:

---

### 🛠️ Hardware Required

* **Raspberry Pi** (any model with SPI support)
* **RC522 RFID Module** (reader and tags)
* **Jumper wires**
* **Breadboard** (optional but recommended)

---

### 🔌 Wiring the RC522 to Raspberry Pi

Connect the RC522 module to the Raspberry Pi as follows:

| RC522 Pin | Raspberry Pi GPIO Pin |
| --------- | --------------------- |
| SDA       | GPIO 24 (Pin 18)      |
| SCK       | GPIO 23 (Pin 16)      |
| MOSI      | GPIO 19 (Pin 15)      |
| MISO      | GPIO 21 (Pin 13)      |
| IRQ       | Not connected         |
| GND       | Ground (Pin 6)        |
| RST       | GPIO 22 (Pin 15)      |
| 3.3V      | 3.3V (Pin 1)          |

---

### ⚙️ Enabling SPI on Raspberry Pi

1. Open the terminal and run:

   ```bash
   sudo raspi-config
   ```

2. Navigate to **Interface Options** → **SPI** and enable it.

3. Reboot the Raspberry Pi:

   ```bash
   sudo reboot
   ```

---

### 📦 Installing Required Libraries

Install the necessary Python libraries:

```bash
sudo apt-get update
sudo apt-get install python3-dev python3-pip
python3 -m pip install spidev mfrc522
```

---

### 📝 Sample Python Code to Read RFID Tags

Create a Python script (`read_rfid.py`) with the following content:

```python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place your tag near the reader")
    id, text = reader.read()
    print(f"ID: {id}")
    print(f"Text: {text}")
finally:
    GPIO.cleanup()
```

Run the script:

```bash
python3 read_rfid.py
```

This script will display the ID and any stored text of the scanned RFID tag.

---

### ✅ Additional Resources

* [Pi My Life Up – RFID RC522 Tutorial](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
* [The Engineering Projects – RC522 with Raspberry Pi 4](https://www.theengineeringprojects.com/2023/01/interface-rfid-module-rc522-with-raspberry-pi-4.html)
* [Instructables – RFID RC522 with Raspberry Pi](https://www.instructables.com/RFID-RC522-Raspberry-Pi/)



