import logging

from libs.vessel_finder import VesselFinder


class VesselFinderApp:
    def __init__(self):
        self.vessel_finder = VesselFinder()

    @property
    def vessels_list(self):
        return [9458028, 9458028, 9458028,9458028,9458028,9458028,9458028,9458028]

    def vessels_info(self):
        vessels = []
        logging.info("Collecting vessels informations.")
        self.vessel_finder.cookie_consent()
        try:
            for imo_number in self.vessels_list:
                vessels.append(self.vessel_finder.vessel_info(imo_number))
        finally:
            self.vessel_finder.close_page()
        return vessels

    @classmethod
    def run(cls):
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
        app = VesselFinderApp()
        vessels = app.vessels_info()
        logging.info(vessels)


if __name__ == '__main__':
    VesselFinderApp.run()
