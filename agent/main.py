from collectors.cpu import CPUCollector
from collectors.memory import MemoryCollector
from collectors.disk import DiskCollector
from collectors.network import NetworkCollector
from collectors.processes import ProcessesCollector
from collectors.services import ServicesCollector
from agent.health_check import get_system_health

from utils.formatter import format_report

from database.database import insert_metrics

from datetime import datetime
from collectors.users import UsersCollector
from collectors.system_logs import SystemLogsCollector
from logger.logger import (
    log_info,
    log_warning,
    log_error,
    log_critical
)


cpu = CPUCollector()
ram = MemoryCollector()
disk = DiskCollector()
network = NetworkCollector()
processes = ProcessesCollector()
services = ServicesCollector()
users = UsersCollector()
system_logs = SystemLogsCollector()


def run_monitoring():

    try:
        log_info("Monitoring cycle started")

        # Collect system information
        cpu_info = cpu.get_cpu_info()
        ram_info = ram.get_ram_info()
        disk_info = disk.get_disk_info()
        network_info = network.get_network_info()

        # Collect top processes
        top_processes = processes.get_top_processes()
        #Services running
        services_info = services.get_services()
        #Users
        users_info = users.get_users()
         #System Logs
        logs_info = system_logs.get_logs(limit=10)
        # Combine all system information
        system_info = {
            "cpu": cpu_info,
            "ram": ram_info,
            "disk": disk_info,
            "network": network_info,
            "processes": top_processes,
            "services": services_info,
            "users": users_info,
            "logs": logs_info
        }

        # Check system health
        system_status = get_system_health(system_info)

        # Current timestamp
        timestamp = datetime.now().isoformat()

        # Save metrics to SQLite
        insert_metrics(
            timestamp,
            cpu_info["usage"],
            ram_info["usage"],
            disk_info["usage"],
            network_info["bytes_sent"],
            network_info["bytes_received"],
            system_status
        )

        # Logging
        log_info(f"System status: {system_status}")

        if system_status == "WARNING":
            log_warning("System requires attention")

        elif system_status == "CRITICAL":
            log_critical("System is in critical condition")

        # Format and print system report
        report = format_report(
            system_info,
            system_status
        )

        print(report)

       
        
    except Exception as e:
        log_error(f"Monitoring error: {e}")
        print(f"Monitoring error: {e}")


if __name__ == "__main__":
    run_monitoring()
