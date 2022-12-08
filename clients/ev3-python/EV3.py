from enum import Enum
from ev3api.apis.tags.motor_api import MotorApi
from ev3api.apis.tags.power_api import PowerApi
from ev3api.apis.tags.sensor_api import SensorApi
from ev3api.apis.tags.sound_api import SoundApi
from ev3api.apis.tags.led_api import LedApi
from ev3api.model.led import LED
from ev3api.model.tone import Tone
from ev3api.model.text import Text
from ev3api.exceptions import ApiException
from ev3api.configuration import Configuration
from ev3api.api_client import ApiClient


class EV3:
    class Motors(Enum):
        A = "A"
        B = "B"
        C = "C"
        D = "D"

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    def __init__(self, host_address):
        self.configuration = Configuration(
            host=f"http://{host_address}/api/v1"
        )
        self.hostAddress = host_address
        self.api_client = ApiClient(self.configuration)
        self.motorApi = MotorApi(self.api_client)
        self.powerApi = PowerApi(self.api_client)
        self.sensorApi = SensorApi(self.api_client)
        self.soundApi = SoundApi(self.api_client)
        self.ledApi = LedApi(self.api_client)

    """
    This method returns the ip-adress from the EV3
    @return the ip-adress   
    """

    def get_host_address(self):
        return self.hostAddress

    """
    The EV3 will do a beep sound.
    """

    def beep(self):
        try:
            self.soundApi.sound_beep_post()
        except ApiException as e:
            print(e)

    """
    * The EV3 will play a tone.
    * @param frequency the specific frequenz for the tone
    * @param lengthMs the specific duration of the tone
    """

    def play_tone(self, frequenz, lengthMs):
        try:
            self.soundApi.sound_tone_post(Tone(
                frequency=frequenz,
                length_ms=lengthMs,
            ))
        except ApiException as e:
            print(e)

    """
    The EV3 will speak a specific text.
    @param text the spoken text for the EV3
    """

    def speak(self, text):
        try:
            self.soundApi.sound_speak_post(Text(
                content_type=text,
            ))
        except ApiException as e:
            print(e)

    """
    This method always returns immediately, whether or not the battery voltage level exists.
    @return the battery voltage level.
    """

    def voltage(self):
        try:
            return self.powerApi.power_get().body["voltage"]
        except ApiException as e:
            print(e)
        return -1

    """
    This method always returns immediately, whether or not the battery current level exists.
    @return the battery current level.
    """

    def current(self):
        try:
            return self.powerApi.power_get().body["current"]
        except ApiException as e:
            print(e)
        return -1

    """
    This method always returns immediately, whether or not the maximal battery voltage exists.
    @return the maximal battery voltage
    """

    def max_voltage(self):
        try:
            return self.powerApi.power_get().body["voltage_max"]
        except ApiException as e:
            print(e)
        return -1

    """
    This method always returns immediately, whether or not the minimal battery voltage exists.
    @return the minimal battery voltage.
    """

    def min_voltage(self):
        try:
            return self.powerApi.power_get().body["voltage_min"]
        except ApiException as e:
            print(e)
        return -1

    """
    This method always returns immediately, whether or not the battery technology description exists.
    @return the battery technology description
    """

    def technology(self):
        try:
            return self.powerApi.power_get().body["technology"]
        except ApiException as e:
            print(e)
        return None

    """
    This method returns an flag, if the button is pressed or not
    @return the boolean if pressed or not
    """

    def button(self):
        try:
            return self.ledApi.button_pressed_get()
        except ApiException as e:
            print(e)
        return None

    """
    The EV3 will flash the LEDs immediately.
    """

    def flash(self):
        body = [
            LED(
                device="device_example",
                red=1,
                green=1,
            )
        ]
        try:
            return self.ledApi.led_flash_post(
                body=body,
            )
        except ApiException as e:
            print(e)
        return None

    """
    This method will set the LEDs of from the EV3
    """

    def led(self):
        # TODO
        return None

    """
    This method will switch off the LEDs of from the EV3.
    """

    def led_off(self):
        # TODO
        return None

    """
    This method will turn on the monitor from the EV3
    """

    def monitor_on(self):
        # TODO
        return None

    """
    This method will turn off the monitor from the EV3
    """

    def monitor_off(self):
        # TODO
        return None
