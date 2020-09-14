import logging

from libs.vessel_finder import VesselFinder


class VesselFinderApp:
    def __init__(self):
        self.vessel_app = VesselFinder()

    @property
    def vessels_list(self):
        return [9458028, 9458028, 9458028, 9458028, 9458028, 9458028, 9458028, 9458028]

    def gather_vessels_data(self):
        vessels = []
        for vessel_number in self.vessels_list:
            vessels.append(self.vessel_app.vessel_info(vessel_number))
        return vessels

    def send_vessels_data_to_db(self, vessels_data):
        pass

    @classmethod
    def run(cls):
        logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s', level=logging.INFO)
        app = VesselFinderApp()
        vessels = app.gather_vessels_data()
        logging.info(vessels)
        app.send_vessels_data_to_db(vessels)


if __name__ == '__main__':
    VesselFinderApp.run()
