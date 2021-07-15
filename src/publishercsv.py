from publisherbase import PublisherBase

import csv

class PublisherCsv(PublisherBase):
    def initialize(self, publisher_config_dict):
        self.csv_filepath = publisher_config_dict["csv_filepath"]
        print("csv at " + self.csv_filepath + " loaded.")

    def publish_data(self, device_data_dict):
        with open(self.csv_filepath, 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerow(device_data_dict)