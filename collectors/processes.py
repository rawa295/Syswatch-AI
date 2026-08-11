import psutil


class ProcessesCollector:
    def get_processes(self):
        processes = []

        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
            try:
                processes.append({
                    "pid": process.info['pid'],
                    "name": process.info['name'],
                    "cpu": process.info['cpu_percent'],
                    "memory": process.info['memory_percent'],
                    "status": process.info['status']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        return processes
    def get_top_processes(self, limit=3):
        processes = self.get_processes()

        processes.sort(
            key=lambda process: process["memory"],
            reverse=True
        )

        return processes[:limit]