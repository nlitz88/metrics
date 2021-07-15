from host import Host
import time

# Specify path to configuration files.
# TODO: Make a general program configuration file and specify a /conf directory location where all can be located.
devices_file_path = "/home/nlitz88/repos/metrics/conf/devices.yaml"
publishers_file_path = "/home/nlitz88/repos/metrics/conf/publishers.yaml"
# deviceTypeConfigFilePath = "/home/nlitz88/repos/metrics/conf/device_type_config.yaml"

metrics_host = Host(devices_file_path, publishers_file_path)
metrics_host.initialize_devices()
metrics_host.intialize_publishers()

while True:
    metrics_host.read_device_data()
    time.sleep(1.5)