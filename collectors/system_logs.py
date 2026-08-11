import subprocess


class SystemLogsCollector:

    def get_logs(self, limit=10):
        try:
            result = subprocess.run(
                [
                    "journalctl",
                    "-n",
                    str(limit),
                    "--no-pager",
                    "-o",
                    "short-iso",
                    "-q",
                    "_SYSTEMD_UNIT!=syswatch-ai.service",
                ],
                capture_output=True,
                text=True,
                check=True
            )

            logs = []

            for line in result.stdout.splitlines():
                line = line.strip()

                if not line:
                    continue

                logs.append({
                    "message": line
                })

            return logs

        except subprocess.CalledProcessError:
            return []

        except FileNotFoundError:
            return []
