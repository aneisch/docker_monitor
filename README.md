### Docker Monitor <a name="docker_monitor"></a>

The Docker monitor allows you to  turn on/off containers. The monitor can connected to a daemon through the url parameter. When home assistant is used within a Docker container, the daemon can be mounted as follows `-v /var/run/docker.sock:/var/run/docker.sock`. The monitor is based on [Glances](https://github.com/nicolargo/glances) and [ha-dockermon](https://github.com/philhawthorne/ha-dockermon) and
is a fork of @Sanderhuisman [docker_monitor](https://github.com/Sanderhuisman/home-assistant-custom-components)


#### Configuration

To use the `docker_monitor` in your installation, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
docker_monitor:
  containers:
    - homeassistant_homeassistant_1
    - homeassistant_mariadb_1
    - homeassistant_mosquitto_1
```

##### Configuration variables

| Parameter            | Type                     | Description                                                           |
| -------------------- | ------------------------ | --------------------------------------------------------------------- |
| name                 | string       (Optional)  | Client name of Docker daemon. Defaults to `Docker`.                   |
| url                  | string       (Optional)  | Host URL of Docker daemon. Defaults to `unix://var/run/docker.sock`.  |
| scan_interval        | time_period  (Optional)  | Update interval. Defaults to 10 seconds.                              |
| containers           | list         (Optional)  | Array of containers to monitor. Defaults to all 

## Credits

* [frenck](https://github.com/frenck/home-assistant-config)
* [robmarkcole](https://github.com/robmarkcole/Hue-sensors-HASS)
* [Sanderhuisman](https://github.com/Sanderhuisman/home-assistant-custom-components)