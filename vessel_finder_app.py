import logging
from typing import List

from libs.vessel_finder import VesselFinder


class VesselFinderApp:
    def __init__(self):
        self.vessel_app = VesselFinder()

    @property
    def vessels_list(self) -> List[int]:
        return [9458028, 9458028, 9458028, 9458028, 9458028, 9458028, 9458028, 9458028]

    def gather_vessels_data(self) -> List[dict]:
        vessels = []
        for vessel_number in self.vessels_list:
            vessels.append(self.vessel_app.vessel_info(vessel_number))
        return vessels

    def send_vessels_data_to_db(self, vessels_data: List[dict]):
        pass

    @classmethod
    def run(cls):
        logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s', level=logging.INFO)
        app = VesselFinderApp()
        try:
            vessels = app.gather_vessels_data()
            logging.info(vessels)
        finally:
            app.vessel_app.close_page()

        app.send_vessels_data_to_db(vessels)


if __name__ == '__main__':
    VesselFinderApp.run()
