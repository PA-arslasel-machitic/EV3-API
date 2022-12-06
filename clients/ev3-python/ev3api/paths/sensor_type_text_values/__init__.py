# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ev3api.paths.sensor_type_text_values import Api

from ev3api.paths import PathValues

path = PathValues.SENSOR_TYPE_TEXT_VALUES