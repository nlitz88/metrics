from publisherinterface import PublisherInterface

# NOTE: Again, another seemingly useless base class, but could carry some useful functionality later on.
class PublisherBase:
    def initialize(self, publisher_config_dict):
        pass
    def publish_data(self, device_data_dict):
        pass