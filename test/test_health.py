from agent.health_check import get_system_health


healthy_system = {
    "cpu": {
        "status": "Excellent"
    },
    "ram": {
        "status": "Excellent"
    },
    "disk": {
        "status": "Excellent"
    }
}


result = get_system_health(healthy_system)

assert result == "HEALTHY"

print("HEALTHY test passed")
warning_system = {
    "cpu": {
        "status": "Excellent"
    },
    "ram": {
        "status": "High - Monitor"
    },
    "disk": {
        "status": "Normal"
    }
}
result = get_system_health(warning_system)

assert result == "WARNING"

print("WARNING test passed")
critical_system = {
    "cpu": {
        "status": "Critical - Alert"
    },
    "ram": {
        "status": "Normal"
    },
    "disk": {
        "status": "Normal"
    }
}
result = get_system_health(critical_system)

assert result == "CRITICAL"

print("CRITICAL test passed")