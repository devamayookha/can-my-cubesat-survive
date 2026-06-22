def run_simulation(
        altitude,
        battery_capacity,
        solar_panel_area,
        payload_power):

    battery = battery_capacity

    daily_log = []

    altitude_factor = 1 + ((altitude - 400) / 2000)

    altitude_factor = max(0.8, min(1.2, altitude_factor))

    mission_failed = False
    failure_day = None

    for day in range(1, 31):

        generation = solar_panel_area * 0.02 * 24
        generation *= altitude_factor

        consumption = (payload_power + 1) * 24

        battery = battery + generation - consumption

        if battery < 0:
            battery = 0

        daily_log.append({
            "day": day,
            "generation": round(generation, 2),
            "consumption": round(consumption, 2),
            "battery": round(battery, 2)
        })

        if battery <= 0:
            mission_failed = True
            failure_day = day
            break

    if mission_failed:

        # Add one extra point so the graph always
        # has at least two points to draw

        if len(daily_log) == 1:
            daily_log.insert(0, {
                "day": 0,
                "generation": 0,
                "consumption": 0,
                "battery": battery_capacity
            })

        return {
            "status": "FAILED",
            "failure_day": failure_day,
            "reason": "Battery Depleted",
            "log": daily_log
        }

    return {
        "status": "SURVIVED",
        "failure_day": None,
        "reason": None,
        "log": daily_log
    }