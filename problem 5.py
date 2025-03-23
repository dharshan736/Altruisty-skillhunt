def analyze_power_consumption(readings):
    if any(r < 10 or r > 200 for r in readings):
        print("INVALID INPUT")
        return


    sensors = [0] * 5  
    for i in range(20):
        sensors[i % 5] += readings[i]  

  
    averages = [round(total / 4) for total in sensors]

  
    max_avg = max(averages)

    if max_avg < 50:
        print("Energy consumption is optimal.")
    else:
        sensor_number = averages.index(max_avg) + 1
        print(f"Sensor Number : {sensor_number}")


readings = list(map(int, input().split()))
analyze_power_consumption(readings)
