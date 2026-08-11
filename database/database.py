import sqlite3

DATABASE = "database/syswatch.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    return connection


def create_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu_usage REAL,
            ram_usage REAL,
            disk_usage REAL,
            bytes_sent REAL,
            bytes_received REAL,
            system_status TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_metrics(
    timestamp,
    cpu_usage,
    ram_usage,
    disk_usage,
    bytes_sent,
    bytes_received,
    system_status
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO system_metrics (
            timestamp,
            cpu_usage,
            ram_usage,
            disk_usage,
            bytes_sent,
            bytes_received,
            system_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        cpu_usage,
        ram_usage,
        disk_usage,
        bytes_sent,
        bytes_received,
        system_status
    ))

    connection.commit()
    connection.close()
def get_metrics():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM system_metrics
        ORDER BY id DESC
    """)

    metrics = cursor.fetchall()

    connection.close()

    return metrics

create_database()

