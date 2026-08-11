import platform
import subprocess

from config.loader import load_config


class ServicesCollector:

    def __init__(self):
        config = load_config()
        self.services = config["services"]

    def get_service_status(self, service_name):

        system = platform.system()

        if system == "Linux":

            try:
                result = subprocess.run(
                    ["systemctl", "is-active", service_name],
                    capture_output=True,
                    text=True
                )

                status = result.stdout.strip()

                if status == "active":
                    return "running"

                elif status == "inactive":
                    return "stopped"

                else:
                    return status

            except Exception:
                return "error"

        elif system == "Windows":

            try:
                result = subprocess.run(
                    ["sc", "query", service_name],
                    capture_output=True,
                    text=True
                )

                output = result.stdout

                if "RUNNING" in output:
                    return "running"

                elif "STOPPED" in output:
                    return "stopped"

                else:
                    return "not_found"

            except Exception:
                return "error"

        else:
            return "unsupported"

    def get_services(self):

        services_info = []

        for service_name in self.services:

            status = self.get_service_status(service_name)

            services_info.append({
                "name": service_name,
                "status": status
            })

        return services_info