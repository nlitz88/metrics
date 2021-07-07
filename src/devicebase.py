from deviceinterface import DeviceInterface
# NOTE: Right now, this base class is kind of useless, more of just here for good practice. May keep if it becomes useful later.
class DeviceBase:
    def initialize(self, device_config_dict):
        pass
    def get_device_data(self):
        pass

# Consider adding a static method here responsible for loading the devices.yaml file and serving yaml from it. Maybe not quite
# the right application, bust just a thought.