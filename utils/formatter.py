from utils.colors import color_status

def format_report(system_info, system_status):

    cpu_usage = system_info["cpu"]["usage"]
    cpu_status = color_status(system_info["cpu"]["status"])

    ram_usage = system_info["ram"]["usage"]
    ram_status = color_status(system_info["ram"]["status"])

    disk_usage = system_info["disk"]["usage"]
    disk_status = color_status(system_info["disk"]["status"])

    network_send = system_info["network"]["bytes_sent"]
    network_receive = system_info["network"]["bytes_received"]

    report = f"""
CPU       {cpu_usage}%      {cpu_status}
RAM       {ram_usage}%      {ram_status}
DISK      {disk_usage}%     {disk_status}
NETWORK   Sent: {network_send} MB | Received: {network_receive} MB

---

## System Status: {color_status(system_status)}

"""

    # Top Processes
    report += "\n## Top Processes\n\n"
    report += (
        f'{"PID":<8}'
        f'{"NAME":<20}'
        f'{"CPU":<10}'
        f'{"RAM":<10}'
        f'{"STATUS"}\n'
    )

    for process in system_info.get("processes", []):
        report += (
            f'{process["pid"]:<8}'
            f'{process["name"]:<20}'
            f'{process["cpu"]:<10.1f}'
            f'{process["memory"]:<10.2f}'
            f'{process["status"]}\n'
        )

    # Services
    report += "\n## Services\n\n"
    report += (
        f'{"NAME":<20}'
        f'{"STATUS"}\n'
    )

    for service in system_info.get("services", []):
        report += (
            f'{service["name"]:<20}'
            f'{service["status"]}\n'
        )

    # Users
    report += "\n## Users\n\n"
    report += (
        f'{"NAME":<20}'
        f'{"TERMINAL":<15}'
        f'{"HOST":<20}'
        f'{"STARTED"}\n'
    )

    for user in system_info.get("users", []):
        report += (
            f'{user["name"]:<20}'
            f'{str(user["terminal"]):<15}'
            f'{str(user["host"]):<20}'
            f'{user["started"]}\n'
        )

    # System Logs
    report += "\n## System Logs\n\n"
    for log in system_info.get("logs", []):
        report += f'{log.get("message", "No message")}\n'

    return report
