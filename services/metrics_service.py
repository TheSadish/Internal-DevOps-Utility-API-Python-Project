import psutil # type: ignore

def get_system_metrics():
    '''
    This API gets system metrics like CPU, Memory, Disk usage based on CPU threshold i.e 10 (Configurable)
    '''
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    cpu_threshold = 10
    cpu_status = "High CPU Usage" if cpu_percent > cpu_threshold else "Normal CPU Usage"
    memory_status = "High Memory Usage" if memory_percent > 80 else "Normal Memory Usage"
    disk_status = "High Disk Usage" if disk_usage > 80 else "Normal Disk Usage"

    return {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_usage": disk_usage,
        "cpu_threshold": cpu_threshold,
        "cpu_status": cpu_status,
        "memory_status": memory_status,
        "disk_status": disk_status
    }