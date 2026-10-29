from src.monitor import TelemetryMonitor

def test_monitor():
    m = TelemetryMonitor()
    res = m.evaluate_devices([
        {"device_id": "D1", "voltage": 12.0, "ping_loss_pct": 0}
    ])
    assert res["healthy_devices"] == 1
    assert res["critical_alerts_count"] == 0
