import psutil


def bytes_to_mb(value):
    return round(value / (1024 ** 2), 2)

class NetworkCollector:
 def get_network_info(self):
  try:
    network = psutil.net_io_counters()

    bytes_sent = network.bytes_sent
    bytes_received = network.bytes_recv

    packets_sent = network.packets_sent
    packets_received = network.packets_recv


    return {
        "bytes_sent": bytes_to_mb(bytes_sent),
        "bytes_received": bytes_to_mb(bytes_received),
        "packets_sent": packets_sent,
        "packets_received": packets_received
    }
  except Exception as e:
        print(f"Error getting network information: {e}")
        return None