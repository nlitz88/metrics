import yaml
from subprocess import check_output

# Each device class must be imported here. 
from devicehdd import DeviceHdd

# class Host(HostInterface):
class Host:

    def __init__(self, devices_file_path):
        self.devices_file_path = devices_file_path
        # Load device configuration file as dictionary.
        with open(self.devices_file_path) as f:
            self.devices_file = yaml.safe_load(f)
        self.devices = []
        self.publishers = []

    def initialize_devices(self):
        for device_yaml_dict in self.devices_file:
            newHdd = DeviceHdd()
            newHdd.initialize(device_yaml_dict)
            self.devices.append(newHdd)
        print("Finished intiailizing devices.")

    def read_device_data(self):
        for device in self.devices:
            device_data = device.get_device_data()
            # Give to publisher to publish to redis, mqtt topics, mongo, etc.
            print(device_data)
        print("Finished reading device data.")

# Map drives by serial numbers to their current name (/dev/sd*). Add this key to the devices dictionary.
# NOTE: Might consider implementing this in a way that is more generic across different device types.
#       Could just be specificly for drives, but what if needed for PCIE devices, for instance?
#       Maybe custom python modules could be an option for this just to keep it out of the main file.
# Actually, I could do this by adding an array of "initialization" commands to run for each device type,
# if need be. 

# for device in devicesFile["disks"]:
#     diskSerial = device["serial_number"]
#     devLocation = check_output(["lsblk -o NAME,SERIAL | grep %s | cut -c 1-3" % diskSerial], shell=True, universal_newlines=True)
#     device["devLocation"] = "/dev/" + str(devLocation).rstrip()

# Device initialization.
# for device in devicesFile:
#     deviceType = device["device_type"]
#     # For each device value in the init_sequence, run the corresponding command with any keys and assign the value
#     for initSeq in deviceTypeConfigs[deviceType]["init_sequences"]:
#         # TODO If init_type == "set_value"...implement this later.
#         command = initSeq["command"]
#         keys = initSeq["keys"]
#         if len(keys) > 0:
#             keyValues = [device[keys[x]] for x in range(len(keys))]
#         deviceValue = initSeq["device_value"]
#         value = check_output([command % ",".join(keyValues)], shell=True, universal_newlines=True)
#         if isinstance(value, str):
#             value = value.rstrip()
#         device[deviceValue] = value
#         print(device)

# for deviceType in deviceTypeConfigs:
#     for device in devicesFile:
#         for init_seq in deviceTypeConfigs[deviceType]["init_sequences"]:
#             print(init_seq)




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
#
# TODO: I think it would also actually be better to "hardcode" or "embed" new device_types as new python modules or classes.
#       This would work very similarly to how ESPHome requires users to custom implement functionality to interface with new/unknown devices.
#       So for all common devices, I could just write modules that allow us to get data. They would just have to implement the operations of a
#       "device-type" interface that would have operations like "initialize" and "getStatXXXX." Kind of backwards from the "make-everything-configurable"
#       mindset, but I think it might just be more practical for anyone who actually wants to use this. Right now, I was aiming for more of a "no-code"
#       kind of extensible application, but for most people, it would be no-code. And for those that really need more out of it,
#       there would be an easy interface to implement against. Just a thought though.