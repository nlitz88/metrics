from host import Host

# Specify path to configuration files.
# TODO: Make a general program configuration file and specify a /conf directory location where all can be located.
devices_file_path = "/home/nlitz88/repos/metrics/conf/devices.yaml"
deviceTypeConfigFilePath = "/home/nlitz88/repos/metrics/conf/device_type_config.yaml"

metrics_host = Host(devices_file_path)
metrics_host.initialize_devices()
metrics_host.read_device_data()