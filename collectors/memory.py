import psutil
from config.loader import load_config

config = load_config()
ram_thresholds = config["thresholds"]["ram"]
def bytes_to_gb(value):
    return round(value / (1024**3), 2)

class MemoryCollector:
  def get_ram_info(self):
   try:
    memory = psutil.virtual_memory()

    ram = memory.percent


    if ram < ram_thresholds["excellent"]:
        status = "Excellent"

    elif ram < ram_thresholds["normal"]:
        status = "Normal"

    elif ram < ram_thresholds["moderate"]:
        status = "Moderate"

    elif ram < ram_thresholds["high"]:
        status = "High - Monitor"

    else:
        status = "Critical - Alert"


    return {
        "usage": ram,
        "status": status,
        "total": bytes_to_gb(memory.total),
        "used": bytes_to_gb(memory.used),
        "available": bytes_to_gb(memory.available)
    }
   except Exception as e:
        print(f"Error getting memory information: {e}")
        return None