import psutil
from config.loader import load_config

config = load_config()
disk_thresholds = config["thresholds"]["disk"]

def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)

class DiskCollector:
 def get_disk_info(self):
    try:
        disk = psutil.disk_usage('/')

        if disk.percent < disk_thresholds["excellent"]:
            status = "Excellent"

        elif disk.percent < disk_thresholds["normal"]:
            status = "Normal"

        elif disk.percent < disk_thresholds["high"]:
            status = "High - Monitor"

        else:
            status = "Critical - Alert"

        return {
            "status": status,
            "total": bytes_to_gb(disk.total),
            "used": bytes_to_gb(disk.used),
            "free": bytes_to_gb(disk.free),
            "usage": disk.percent
        }

    except Exception as e:
        print(f"Error getting disk information: {e}")
        return None