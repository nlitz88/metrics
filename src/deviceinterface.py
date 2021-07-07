class DeviceInterface:
    # This operation is used to initialize the device instance. Accepts a dictionary that is read in from the device's yaml definition.
    # This device_config_yaml may contain any number of parameters/fields necessary to initialize/setup the instance for data collection.
    def initialize(self, device_config_dict):
        pass
    # This is a standard operation that will return a dictionary to be converted to the appropriate format (json, plaintext, etc) for
    # use by endpoints or other publishing methods.
    def get_device_data(self):
        pass