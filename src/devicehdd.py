from subprocess import check_output
import re

from devicebase import DeviceBase

# TODO: Come up with a better documentation scheme for these classes. At the moment, this is a hard drive class that is dependent on the hddtemp package.
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
        # Use regex pattern specific to hddtemp to extract temperature.
        temperature = re.search("[0-9]{1,}°C$", temperature).group(0)
        temperature = re.search("[0-9]{1,}", temperature).group(0)
        result = {"temperature": temperature, "unit": "C"}
        return result