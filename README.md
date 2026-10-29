# IoT Hardware Telemetry Monitor

Operational uptime tracker and health telemetry aggregator for mission-critical roadside cameras, weight-in-motion (WIM) sensors, and dynamic messaging boards.

## Features
- **Heartbeat Anomaly Detector**: Identifies missing pings and degraded sensor voltages.
- **Mean Time To Recovery (MTTR)**: Tracks technician dispatch and device restoration speed.
- **Maintenance Alerting Engine**: Auto-generates high-priority preventative maintenance tickets.

## Usage
```bash
pip install -r requirements.txt
python main.py
pytest tests/
```
