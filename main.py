from src.monitor import TelemetryMonitor

def main():
    print("=== IoT Hardware Telemetry & Health Monitor ===")
    sample_sensors = [
        {"device_id": "CAM-01-NTH", "location": "KM 42+200", "voltage": 12.4, "ping_loss_pct": 0.0},
        {"device_id": "WIM-04-STH", "location": "KM 68+100", "voltage": 10.8, "ping_loss_pct": 5.0},
        {"device_id": "VMS-02-CTR", "location": "KM 95+400", "voltage": 12.1, "ping_loss_pct": 45.0}
    ]
    
    monitor = TelemetryMonitor()
    res = monitor.evaluate_devices(sample_sensors)
    
    print("Active Devices: " + str(res['total_devices']) + " | Healthy: " + str(res['healthy_devices']))
    print("Critical Alerts Triggered: " + str(res['critical_alerts_count']))
    for a in res["alerts"]:
        print(" - [" + a['action_required'] + "] Device " + a['device_id'] + " @ " + a['location'])

if __name__ == '__main__':
    main()
