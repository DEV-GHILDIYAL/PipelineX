from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

# Initialize psutil CPU measurements to prevent 0.0 on the first web request.
psutil.cpu_percent(interval=None)

@app.route("/")
def index():
    """Renders the DevOps Dashboard homepage."""
    return render_template("index.html")

@app.route("/health")
def health():
    """
    Returns JSON with system health metrics:
    - CPU usage percentage
    - Memory usage percentage
    - Disk usage percentage
    """
    try:
        cpu = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        
        return jsonify({
            "status": "healthy",
            "cpu": cpu,
            "cpu_percent": cpu,
            "memory": memory,
            "memory_percent": memory,
            "disk": disk,
            "disk_percent": disk
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

@app.route("/deployments")
def deployments():
    """
    Returns a hardcoded list of fake deployment history entries.
    """
    # 5 fake deployment entries as requested
    mock_history = [
        {
            "id": "DEP-005",
            "service": "Authentication API",
            "version": "v1.4.2",
            "status": "Success",
            "timestamp": "2026-06-23 10:15:30",
            "duration": "45s"
        },
        {
            "id": "DEP-004",
            "service": "Payment Gateway",
            "version": "v2.0.1",
            "status": "Success",
            "timestamp": "2026-06-23 09:42:10",
            "duration": "1m 12s"
        },
        {
            "id": "DEP-003",
            "service": "Frontend Portal",
            "version": "v3.1.0-rc1",
            "status": "Failed",
            "timestamp": "2026-06-23 08:30:15",
            "duration": "28s"
        },
        {
            "id": "DEP-002",
            "service": "Notification Service",
            "version": "v1.0.8",
            "status": "Success",
            "timestamp": "2026-06-23 07:11:05",
            "duration": "50s"
        },
        {
            "id": "DEP-001",
            "service": "Data Aggregator",
            "version": "v0.9.15",
            "status": "Success",
            "timestamp": "2026-06-22 23:45:00",
            "duration": "2m 5s"
        }
    ]
    return jsonify(mock_history), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
