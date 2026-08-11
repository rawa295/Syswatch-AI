import subprocess
from datetime import datetime


class UsersCollector:

    def get_users(self):
        users = []

        try:
            result = subprocess.run(
                [
                    "loginctl",
                    "list-sessions",
                    "--no-legend",
                    "--no-pager"
                ],
                capture_output=True,
                text=True,
                check=True
            )

            sessions = result.stdout.strip().splitlines()

            for session in sessions:
                parts = session.split()

                if len(parts) < 3:
                    continue

                session_id = parts[0]
                uid = parts[1]
                username = parts[2]

                try:
                    session_info = subprocess.run(
                        [
                            "loginctl",
                            "show-session",
                            session_id,
                            "--property=Name",
                            "--property=Remote",
                            "--property=RemoteHost",
                            "--property=Type",
                            "--property=Timestamp"
                        ],
                        capture_output=True,
                        text=True,
                        check=True
                    )

                    info = {}

                    for line in session_info.stdout.strip().splitlines():
                        if "=" in line:
                            key, value = line.split("=", 1)
                            info[key] = value

                    users.append({
                        "name": username,
                        "terminal": info.get("Type") or None,
                        "host": info.get("RemoteHost") or None,
                        "started": info.get("Timestamp") or None
                    })

                except subprocess.CalledProcessError:
                    continue

        except (subprocess.CalledProcessError, FileNotFoundError):
            return []

        return users
