from unittest.mock import Mock
from unit_test_project.src.alarm import Alarm, Sensor

class StubSensor:
    def sample_pressure(self):
        return 17.0

def test_alarm_is_off_by_default():
    alarm = Alarm()
    assert not alarm.is_alarm_on

def test_alarm_is_on_at_lower_threshold():
    alarm = Alarm(StubSensor())  # Use StubSensor to simulate low pressure
    alarm.check()
    assert alarm.is_alarm_on

def test_alarm_is_on_at_higher_threshold():
    # Use Mock for Sensor
    stub = Mock(spec=Sensor)  # Mock the Sensor class
    stub.sample_pressure = Mock(return_value=21.0)  # Simulate high pressure
    alarm = Alarm(stub)
    alarm.check()
    assert alarm.is_alarm_on
