from typing import List, Dict, Any

class TelemetryMonitor:
    def __init__(self, voltage_threshold: float = 11.2):
        self.voltage_threshold = voltage_threshold
        
    def evaluate_devices(self, telemetry_records: List[Dict[str, Any]]) -> Dict[str, Any]:
        healthy = 0
        alerts = []
        
        for r in telemetry_records:
            is_voltage_low = r.get("voltage", 12.0) < self.voltage_threshold
            is_offline = r.get("ping_loss_pct", 0) > 20.0
            
            if is_voltage_low or is_offline:
                alerts.append({
                    "device_id": r["device_id"],
                    "location": r.get("location", "UNKNOWN"),
                    "voltage": r.get("voltage"),
                    "ping_loss": r.get("ping_loss_pct"),
                    "action_required": "DISPATCH_FIELD_CREW" if is_offline else "INSPECT_BATTERY"
                })
            else:
                healthy += 1
                
        return {
            "total_devices": len(telemetry_records),
            "healthy_devices": healthy,
            "critical_alerts_count": len(alerts),
            "alerts": alerts
        }
