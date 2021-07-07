from subprocess import check_output

from devicebase import DeviceBase

class DeviceHdd(DeviceBase):
    def initialize(self, device_config_dict):
        # Assign yaml dictionary to instance variable for device config data.
        self.device_config_data = device_config_dict
        # Initialize dev_location based on provided serial number.
        hdd_serial = self.device_config_data["serial_number"]
        command = "lsblk -o NAME,SERIAL | grep %s | cut -c 1-3"
        dev_location = check_output([command % hdd_serial], shell=True, universal_newlines=True)
        self.device_config_data["dev_location"] = dev_location
    def get_device_data(self):
        dev_location = self.device_config_data["dev_location"]
        # TODO: Use some sort of regular expression here to parse the temperature rather than cut.
        temperature = check_output(["hddtemp /dev/%s" % dev_location], shell=True, universal_newlines=True)
        result = {"temperature": temperature}
        return result