'''
Docker Monitor component

For more details about this component, please refer to the documentation at
https://github.com/Sanderhuisman/home-assistant-custom-components
'''
import logging

from homeassistant.components.switch import (
    ENTITY_ID_FORMAT,
    PLATFORM_SCHEMA,
    SwitchDevice
)
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.core import ServiceCall

from custom_components.docker_monitor import (
    CONF_ATTRIBUTION,
    DATA_DOCKER_API,
    DOCKER_HANDLE
)

DEPENDENCIES = ['docker_monitor']

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """Set up the Docker Monitor Switch."""

    api = hass.data[DOCKER_HANDLE][DATA_DOCKER_API]

    switches = []
    for name in [x.get_name() for x in api.get_containers()]:
        switches.append(ContainerSwitch(api, name))

    if switches:
        add_devices_callback(switches, True)
    else:
        _LOGGER.info("No containers setup")
        return False


class ContainerSwitch(SwitchDevice):
    def __init__(self, api, name):
        self._api = api
        self._name = name
        self._state = False

        self._container = api.get_container(name)

        def update_callback(stats):
            _LOGGER.debug("Received callback with message: {}".format(stats))

            if stats['info']['status'] == 'running':
                state = True
            else:
                state = False

            if self._state is not state:
                self._state = state

                self.schedule_update_ha_state()

        self._container.stats(update_callback)

    @property
    def should_poll(self):
        return True

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return 'mdi:docker'

    @property
    def device_state_attributes(self):
        return {
            ATTR_ATTRIBUTION: CONF_ATTRIBUTION
        }

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self._container.start()

    def turn_off(self, **kwargs):
        self._container.stop()