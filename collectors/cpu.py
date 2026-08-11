import psutil
from config.loader import load_config

config = load_config()
cpu_thresholds = config["thresholds"]["cpu"]

class CPUCollector:

    def get_cpu_info(self):
        try:
            cpu = psutil.cpu_percent(interval=1)

            physical_cores = psutil.cpu_count(logical=False)
            logical_cores = psutil.cpu_count(logical=True)

            freq = psutil.cpu_freq()

            core_usage = psutil.cpu_percent(interval=1, percpu=True)

            if cpu < cpu_thresholds["excellent"]:
                status = "Excellent"
            elif cpu < cpu_thresholds["normal"]:
               status = "Normal"
            elif cpu < cpu_thresholds["moderate"]:
               status = "Moderate"
            elif cpu < cpu_thresholds["high"]:
               status = "High - Monitor"
            else:
                status = "Critical - Alert"

            return {
                "usage": cpu,
                "physical_cores": physical_cores,
                "logical_cores": logical_cores,
                "frequency": freq.current if freq else None,
                "core_usage": core_usage,
                "status": status
            }

        except Exception as e:
            print(f"Error getting CPU information: {e}")
            return None
 