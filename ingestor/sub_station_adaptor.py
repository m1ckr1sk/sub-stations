class SubstationAdaptor:

    def __init__(self, data_loader, event_interface) -> None:
        self.data_loader = data_loader
        self.event_interface = event_interface

    def load_substation_data(self):
        self.data_loader.load_single_data_row()
        self.event_interface.raise_event()
