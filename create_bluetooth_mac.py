
# Kleines hilf's Skript zur Brechung der Bluetooth MAC-Adresse von
# Spider Farmer Hardware
# Eigentlich ist die WLAN-MAC auf dem Gehäuse aufgedruckt,
# die Bluetooth MAC liegt, zwei Dezimalstellen höher.

def process_mac():
    # 1. Konsolen-Eingabe
    print('##########################################')
    print('#                                        #')
    print('#  Spider Farmer MAC-Adresse berechnen.  #')
    print('#                                        #')
    print('##########################################')
    raw_input = input("Bitte die 12-stelligen Kombination vom Gehäuse (Hex-String) eingeben: ")

    # Bereinigung (entfernt Leerzeichen/Trenner)
    clean_hex = raw_input.strip().replace(":", "").replace("-", "")

    if len(clean_hex) != 12:
        print(f"Fehler: '{clean_hex}' hat {len(clean_hex)} Zeichen statt 12.")
        return

    print(f"\n--- Verarbeitung startet für: {clean_hex} ---")

    # 2. In Bytes (Integer) umwandeln
    # Wir teilen den String in 6 Paare auf
    hex_pairs = [clean_hex[i: i +2] for i in range(0, 12, 2)]
    print(f"Schritt 1 (Gruppierung): {hex_pairs}")

    bytes_list = [int(pair, 16) for pair in hex_pairs]
    print(f"Schritt 2 (Dezimal-Werte): {bytes_list}")

    # 3. Addition am letzten Byte
    old_last_byte = bytes_list[-1]
    # % 256 stellt sicher, dass wir bei Werten < 0 wieder bei FF landen (Underflow-Schutz)
    bytes_list[-1] = (bytes_list[-1] + 2) % 256
    print(f"Schritt 3 (Addition): Letztes Byte {old_last_byte:02X}h -> {bytes_list[-1]:02X}h")

    # 4. Formatierung zur MAC-Adresse
    new_mac = ":".join(f"{b:02x}" for b in bytes_list).upper()
    print(f"Schritt 4 (Formatierung): {new_mac}")

    print(f"\nDie Bluetooth MAC sollte sein: {new_mac}")

# Skript ausführen
if __name__ == "__main__":
    process_mac()