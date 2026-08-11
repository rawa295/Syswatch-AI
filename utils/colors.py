GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
def color_status(status):

    if status in ["HEALTHY", "Excellent", "Normal"]:
        return GREEN + "●" + RESET + " " + status

    elif status in ["WARNING", "Moderate", "High - Monitor"]:
        return YELLOW + "●" + RESET + " " + status

    elif status in ["CRITICAL", "Critical - Alert"]:
        return RED + "●" + RESET + " " + status
  

