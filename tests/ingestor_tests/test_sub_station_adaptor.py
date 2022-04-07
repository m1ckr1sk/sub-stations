from mock import Mock
from ingestor.sub_station_adaptor import SubstationAdaptor  # noqa: E402


def test_ingestor_raises_event_on_load():
    mock_data_loader = Mock()
    mock_event_interface = Mock()

    substation_adaptor = SubstationAdaptor(
        data_loader=mock_data_loader,
        event_interface=mock_event_interface
    )
    substation_adaptor.load_substation_data()

    mock_data_loader.load_single_data_row.assert_called()
    mock_event_interface.raise_event.assert_called()
