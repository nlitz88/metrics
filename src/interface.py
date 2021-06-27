import yaml
from subprocess import check_output

# Specify path to configuration files.
# TODO: Make a general program configuration file and specify a /conf directory location where all can be located.
devicesFilePath = "/home/nlitz88/metrics/conf/devices.yaml"
deviceTypeConfigFilePath = "/home/nlitz88/metrics/conf/device_type_config.yaml"


# Load configuration files as dictionaries.
with open(devicesFilePath) as f:
    devicesFile = yaml.safe_load(f)

with open(deviceTypeConfigFilePath) as f:
    deviceTypeConfigs = yaml.safe_load(f)

# Map drives by serial numbers to their current name (/dev/sd*). Add this key to the devices dictionary.
# NOTE: Might consider implementing this in a way that is more generic across different device types.
#       Could just be specificly for drives, but what if needed for PCIE devices, for instance?
#       Maybe custom python modules could be an option for this just to keep it out of the main file.
for device in devicesFile["disks"]:
    diskSerial = device["serial_number"]
    devLocation = check_output(["lsblk -o NAME,SERIAL | grep %s | cut -c 1-3" % diskSerial], shell=True, universal_newlines=True)
    device["devLocation"] = "/dev/" + str(devLocation).rstrip()




# NOTE: Kind of a big design decision:
#       Should I move all of the grouping capabilities (like devicegroups and zones) to the controller?
#       If this service is to truly just be an adaptable data broker/interface, then why should it have any knowledge of the grouping of devices?
#       It won't be doing any of those calculations, only the controller has to have knowledge of these groupings/assignments.
#       
#       The only things that should be defined in this should be devices.yaml. devices.yaml should basically just list all of the devices
#       (and device types) that the user wants the interface to make available via the module or the eventual API.
#       THEREFORE:
#       The controller should specify a similar list (almost identical) that outlines the drives that it wants to use to make its determinations.
#       Additionally, this should include the groupings and zones that are currently specified here.
#       
#       The point is to make this interface service as generic as possible so that it can be expanded or used as a lightweight metrics
#       collector for future projects/applications/adapters (as an alternative to something like netdata).
#       For instance, my load indication LEDs, rather than depending on an instance of netdata, I could use the interface.
#
# TODO: Make this interface a class.
#       Then make a flask REST API that serves up data from the class.
#       Also, can publish data on mqtt topics from the class.
#       This way, the class can be what interfaces with both the API server and mqtt broker.