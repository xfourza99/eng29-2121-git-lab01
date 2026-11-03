def analyze_dc(voltage_v, resistance_ohm):
    current_a = voltage_v / resistance_ohm
    power_w = voltage_v * current_a
    return {"current_a": current_a, "power_w": power_w}


if __name__ == "__main__":
    voltage_v = float(input("Enter voltage (V): "))
    resistance_ohm = float(input("Enter resistance (ohm): "))
    result = analyze_dc(voltage_v, resistance_ohm)
    print(f"Current: {result['current_a']} A")
    print(f"Power: {result['power_w']} W")