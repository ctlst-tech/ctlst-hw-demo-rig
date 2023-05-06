# ctlst-hw-demo-rig
CatPilot Settings and pyQt visitation script for Catalyst's hardware public demo rig

---

## Build, Upload, Run

### Clone repo
```bash
git clone git@github.com:ctlst-tech/ctlst-hw-demo-rig.git
git submodule --init --recursive
```

### Build
```bash
make atomics
make ctlst
```

### Upload
```bash
make upload ip=192.168.1.20
```

### Run
On Autopilot
```bash
catpilot
```
On GCU:
```bash
./gui.py --ip 192.168.1.20
```

---

## Architecture
file `config/swsys.xml` is divided into 5 parts:
- Buses declaration
- Boards
- Nav processing
- Bridges
- Connection

There are 4 internal buses (gen_bus, nav_bus, imu_bus, io_bus) and 1 bus (gcu_bus) for transmittion to the GCU.
Also there are 3 main flows for following subsystems: imu, adc, io. You can change priorities and timings if needed.

---

## Primary validation

### 1. Check connection with GCU
- open `configs/swsys.xml`
- check ip and ports
```xml
    <!-- Connection -->
    <service type="sdtl" name="gcu_link">
        <type value="udp"/>

        <ip value="192.168.1.2"/>
        <port value="20001"/>
        <server_ip value="0.0.0.0"/>
        <server_port value="20000"/>

        <channel id="1" name="downlink" type="rel"/>
        <channel id="2" name="downlink_sk" type="unrel"/>
        <channel id="4" name="cmd" type="unrel"/>
    </service>

    <service type="eqrb_sdtl" name="debug_sdtl">
        <event_queue_source value="gcu_bus"/>
        <sdtl_service value="gcu_link"/>
        <channel_1_name value="downlink"/>
        <channel_2_name value="downlink_sk"/>
    </service>
```
- correct if necessary
- upload firmware
- start the GUI app

**you may face with problems when strating the GUI app (not all topics were registered). Just try to restart it*

### 2. Check LEDs and relay
- by default it uses a meander with 1 sec period to control all LEDs
- file `configs/flow_io_gpio.xml` contains the control logic
```xml
        <f name="out1" by_spec="ctlst.io.gpio_out">
            <in alias="input_float">inputs/out1</in>
            <param alias="channel">2</param>
        </f>
        <f name="out2" by_spec="ctlst.io.gpio_out">
            <in alias="input_float">inputs/out2</in>
            <param alias="channel">3</param>
        </f>
        <f name="relay" by_spec="ctlst.io.gpio_out">
            <in alias="input_float">inputs/relay</in>
            <param alias="channel">4</param>
        </f>
        <f name="phase" by_spec="ctlst.io.gpio_out">
            <in alias="input_float">inputs/phase</in>
            <param alias="channel">5</param>
        </f>
        <f name="overheat" by_spec="ctlst.io.gpio_out">
            <in alias="input_float">inputs/overheat</in>
            <param alias="channel">6</param>
        </f>
        <f name="status" by_spec="ctlst.io.gpio_out">
            <in alias="input_float">inputs/status</in>
            <param alias="channel">7</param>
        </f>
```

### 3. Check servo and motor
- by default it uses a standard pwm for a servo and random parameters for an engine
- file `configs/flow_io_gpio.xml` contains the control logic
```xml
        <f name="servo" by_spec="ctlst.io.pwm_out">
            <in alias="input">inputs/servo</in>
            <param alias="channel">0</param>
            <param alias="period">20000</param>
            <param alias="min">500</param>
            <param alias="max">2500</param>
            <param alias="bipolar">true</param>
        </f>
        <f name="engine" by_spec="ctlst.io.pwm_out">
            <in alias="input">inputs/engine</in>
            <param alias="channel">1</param>
            <param alias="period">2000</param>
            <param alias="min">250</param>
            <param alias="max">750</param>
            <param alias="bipolar">false</param>
        </f>
```

### 4. Check thermosensors, potentiometer
- open ADC tab in the GCU app and check the values when heating

### 5. Check buttons
- open IO tab in the GCU app and check the values when pressing

### 5. Check OUT1/OUT2 and IN1
- connect OUT1/OUT2 with IN1 and check IO tab in the GCU

