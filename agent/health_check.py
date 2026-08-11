def get_system_health(system_info):

    cpu_status = system_info["cpu"]["status"]
    ram_status = system_info["ram"]["status"]
    disk_status = system_info["disk"]["status"]

    statuses = [cpu_status, ram_status, disk_status]

    if all(status in ["Excellent", "Normal"] for status in statuses):
        return "HEALTHY"

    elif any(status == "Critical - Alert" for status in statuses):
        return "CRITICAL"

    else:
        return "WARNING"