#!/usr/bin/env python3

import sys
from time import sleep
import ctypes
from typing import List

sys.path.append('./catpilot/c-atom/eswb/pytools')

from monitor import *
from eswbmon import *
from ds.datasources import *

from eswb import *

mon_bus_name = 'monitor'
telemetry_dir_name = 'telemetry'

args_parser = ArgParser()
args = args_parser.args

mon = EswbMonitor(monitor_bus_name=mon_bus_name, argv=sys.argv, tabs=True, )

imu_tab = mon.add_tab('IMU')
adc_tab = mon.add_tab('ADC')
io_tab = mon.add_tab('IO')
gen_tab = mon.add_tab('Generators')
sdtl_tab = mon.add_tab('SDTL')

mon.mkdir(telemetry_dir_name)

basic_topics_root = mon_bus_name + '/' + telemetry_dir_name
drone_topics_root = basic_topics_root + '/' + 'drone'

cmd_sdtl_channel = SDTLchannel(name='cmd', ch_id=4, ch_type=SDTLchannelType.unrel)
mon.bridge_sdtl_udp(ip_in='0.0.0.0', port_in='20001',
                    ip_out='192.168.1.21', port_out='20000',
                    bridge_to='telemetry',
                    additional_channels=[cmd_sdtl_channel])


# Data sources
ax = DataSourceEswbTopic('ax', path=f'{basic_topics_root}/nav/ang/a/x')
ay = DataSourceEswbTopic('ay', path=f'{basic_topics_root}/nav/ang/a/y')
az = DataSourceEswbTopic('az', path=f'{basic_topics_root}/nav/ang/a/z')
wx = DataSourceEswbTopic('wx', path=f'{basic_topics_root}/nav/ang/omega/x', mult=57.32)
wy = DataSourceEswbTopic('wy', path=f'{basic_topics_root}/nav/ang/omega/y', mult=57.32)
wz = DataSourceEswbTopic('wz', path=f'{basic_topics_root}/nav/ang/omega/z', mult=57.32)
roll = DataSourceEswbTopic('roll', path=f'{basic_topics_root}/nav/ang/roll', mult=57.32)
pitch = DataSourceEswbTopic('pitch', path=f'{basic_topics_root}/nav/ang/pitch', mult=57.32)
yaw = DataSourceEswbTopic('yaw', path=f'{basic_topics_root}/nav/ang/yaw', mult=57.32)

pstat = DataSourceEswbTopic('pstat', path=f'{basic_topics_root}/nav/pres/pstat')
pdyn = DataSourceEswbTopic('pdyn', path=f'{basic_topics_root}/nav/pres/pdyn')
pdiff = DataSourceEswbTopic('pdiff', path=f'{basic_topics_root}/nav/pres/pdiff')

altitude_bar = DataSourceEswbTopic('altitude_bar', path=f'{basic_topics_root}/nav/air/altitude_bar')
airspeed = DataSourceEswbTopic('airspeed', path=f'{basic_topics_root}/nav/air/airspeed')

tax = DataSourceEswbTopic('tax', path=f'{basic_topics_root}/dev/imu/temp/ta/x')
tay = DataSourceEswbTopic('tay', path=f'{basic_topics_root}/dev/imu/temp/ta/y')
taz = DataSourceEswbTopic('taz', path=f'{basic_topics_root}/dev/imu/temp/ta/z')
twx = DataSourceEswbTopic('twx', path=f'{basic_topics_root}/dev/imu/temp/tw/x')
twy = DataSourceEswbTopic('twy', path=f'{basic_topics_root}/dev/imu/temp/tw/y')
twz = DataSourceEswbTopic('twz', path=f'{basic_topics_root}/dev/imu/temp/tw/z')
tadc = DataSourceEswbTopic('tadc', path=f'{basic_topics_root}/dev/imu/temp/tadc')

io_adc1_ch0 = DataSourceEswbTopic('io_adc1_ch0', path=f'{basic_topics_root}/dev/io/voltage/ch0')
io_adc1_ch1 = DataSourceEswbTopic('io_adc1_ch1', path=f'{basic_topics_root}/dev/io/voltage/ch1')
io_adc1_ch2 = DataSourceEswbTopic('io_adc1_ch2', path=f'{basic_topics_root}/dev/io/voltage/ch2')
io_adc1_ch3 = DataSourceEswbTopic('io_adc1_ch3', path=f'{basic_topics_root}/dev/io/voltage/ch3')
io_adc1_ch4 = DataSourceEswbTopic('io_adc1_ch4', path=f'{basic_topics_root}/dev/io/voltage/ch4')
io_adc1_ch5 = DataSourceEswbTopic('io_adc1_ch5', path=f'{basic_topics_root}/dev/io/voltage/ch5')
io_adc1_ch6 = DataSourceEswbTopic('io_adc1_ch6', path=f'{basic_topics_root}/dev/io/voltage/ch6')
io_adc1_ch7 = DataSourceEswbTopic('io_adc1_ch7', path=f'{basic_topics_root}/dev/io/voltage/ch7')
io_adc2_ch0 = DataSourceEswbTopic('io_adc2_ch0', path=f'{basic_topics_root}/dev/io/voltage/ch8')
io_adc2_ch1 = DataSourceEswbTopic('io_adc2_ch1', path=f'{basic_topics_root}/dev/io/voltage/ch9')
io_adc2_ch2 = DataSourceEswbTopic('io_adc2_ch2', path=f'{basic_topics_root}/dev/io/voltage/ch10')
io_adc2_ch3 = DataSourceEswbTopic('io_adc2_ch3', path=f'{basic_topics_root}/dev/io/voltage/ch11')
io_adc2_ch4 = DataSourceEswbTopic('io_adc2_ch4', path=f'{basic_topics_root}/dev/io/voltage/ch12')
io_adc2_ch5 = DataSourceEswbTopic('io_adc2_ch5', path=f'{basic_topics_root}/dev/io/voltage/ch13')
io_adc2_ch6 = DataSourceEswbTopic('io_adc2_ch6', path=f'{basic_topics_root}/dev/io/voltage/ch14')
io_adc2_ch7 = DataSourceEswbTopic('io_adc2_ch7', path=f'{basic_topics_root}/dev/io/voltage/ch15')

io_button1 = DataSourceEswbTopic('io_button1', path=f'{basic_topics_root}/dev/io/digital/button1')
io_button2 = DataSourceEswbTopic('io_button2', path=f'{basic_topics_root}/dev/io/digital/button2')
io_button3 = DataSourceEswbTopic('io_button3', path=f'{basic_topics_root}/dev/io/digital/button3')
io_button4 = DataSourceEswbTopic('io_button4', path=f'{basic_topics_root}/dev/io/digital/button4')
io_hall1_period = DataSourceEswbTopic('io_hall1_period', path=f'{basic_topics_root}/dev/io/digital/hall1_period')
io_hall2_period = DataSourceEswbTopic('io_hall2_period', path=f'{basic_topics_root}/dev/io/digital/hall2_period')
io_hall3_period = DataSourceEswbTopic('io_hall3_period', path=f'{basic_topics_root}/dev/io/digital/hall3_period')
io_hall4_period = DataSourceEswbTopic('io_hall4_period', path=f'{basic_topics_root}/dev/io/digital/hall4_period')
io_in1 = DataSourceEswbTopic('io_in1', path=f'{basic_topics_root}/dev/io/digital/in1')

sin1 = DataSourceEswbTopic('sin1', path=f'{basic_topics_root}/hk/gen/sin1')
sin2 = DataSourceEswbTopic('sin2', path=f'{basic_topics_root}/hk/gen/sin2')
mean1 = DataSourceEswbTopic('mean1', path=f'{basic_topics_root}/hk/gen/mean1')
mean2 = DataSourceEswbTopic('mean2', path=f'{basic_topics_root}/hk/gen/mean2')


# Charts
sin1 = EwChart([sin1], title="Sin1")
sin2 = EwChart([sin2], title="Sin2")
mean1 = EwChart([mean1], title="Mean1")
mean2 = EwChart([mean2], title="Mean2")

accel = EwChart([ax, ay, az], 
                title="Accelerations",
                labels={'left': 'm/s²', 'bottom': 'time, ms'})
gyro = EwChart([wx, wy, wz], 
               title="Angular rates",
               labels={'left': '1/s', 'bottom': 'time, ms'})
roll_pitch = EwChart([roll, pitch], 
                     title="Angles",
                     labels={'left': 'grad', 'bottom': 'time, ms'})
yaw = EwChart([yaw], 
              title="Angles",
              labels={'left': 'grad', 'bottom': 'time, ms'})

accel_gyro_temp = EwChart([tax, tay, taz, twx, twy, twz], 
                          title="Sensor temperatures",
                          labels={'left': '°C', 'bottom': 'time, ms'})
adc_temp = EwChart([tadc], 
                   title="ADC temperature",
                   labels={'left': '°C', 'bottom': 'time, ms'})

pstat_pdyn = EwChart([pstat, pdyn], 
                     title="Static and dynamic pressure",
                     labels={'left': 'Pa', 'bottom': 'time, ms'})
pdiff = EwChart([pdiff], 
                title="Differential pressure",
                labels={'left': 'Pa', 'bottom': 'time, ms'})

altitude_bar = EwChart([altitude_bar], 
                       title="Barometric altitude",
                       labels={'left': 'm', 'bottom': 'time, ms'})
airspeed = EwChart([airspeed], 
                   title="Airspeed",
                   labels={'left': 'm/s', 'bottom': 'time, ms'})

io_adc1_ch0 = EwChart([io_adc1_ch0], title="IO ADC1 ch0", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc1_ch1 = EwChart([io_adc1_ch1], title="IO ADC1 ch1", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc1_ch2 = EwChart([io_adc1_ch2], title="IO ADC1 ch2", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc1_ch3 = EwChart([io_adc1_ch3], title="IO ADC1 ch3", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc1_ch4 = EwChart([io_adc1_ch4], title="IO ADC1 ch4", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc1_ch5 = EwChart([io_adc1_ch5], title="IO ADC1 ch5", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc1_ch6 = EwChart([io_adc1_ch6], title="IO ADC1 ch6", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc1_ch7 = EwChart([io_adc1_ch7], title="IO ADC1 ch7", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch0 = EwChart([io_adc2_ch0], title="IO ADC2 ch0", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch1 = EwChart([io_adc2_ch1], title="IO ADC2 ch1", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch2 = EwChart([io_adc2_ch2], title="IO ADC2 ch2", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch3 = EwChart([io_adc2_ch3], title="IO ADC2 ch3", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch4 = EwChart([io_adc2_ch4], title="IO ADC2 ch4", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch5 = EwChart([io_adc2_ch5], title="IO ADC2 ch5", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch6 = EwChart([io_adc2_ch6], title="IO ADC2 ch6", labels={'left': 'V', 'bottom': 'time, ms'})
io_adc2_ch7 = EwChart([io_adc2_ch7], title="IO ADC2 ch7", labels={'left': 'V', 'bottom': 'time, ms'})

io_button1 = EwChart([io_button1], title="Button 1", labels={'left': '0/1', 'bottom': 'time, ms'})
io_button2 = EwChart([io_button2], title="Button 2", labels={'left': '0/1', 'bottom': 'time, ms'})
io_button3 = EwChart([io_button3], title="Button 3", labels={'left': '0/1', 'bottom': 'time, ms'})
io_button4 = EwChart([io_button4], title="Button 4", labels={'left': '0/1', 'bottom': 'time, ms'})
io_hall1 = EwChart([io_hall1_period], title="Hall 1 period", labels={'left': 'us', 'bottom': 'time, ms'})
io_hall2 = EwChart([io_hall2_period], title="Hall 2 period", labels={'left': 'us', 'bottom': 'time, ms'})
io_hall3 = EwChart([io_hall3_period], title="Hall 3 period", labels={'left': 'us', 'bottom': 'time, ms'})
io_hall4 = EwChart([io_hall4_period], title="Hall 4 period", labels={'left': 'us', 'bottom': 'time, ms'})
io_in1 = EwChart([io_in1], title="IN 1", labels={'left': '0/1', 'bottom': 'time, ms'})


# Add widgets
# imu_tab.add_widget(EwGroup([accel, gyro, roll_pitch, accel_gyro_temp]))
imu_tab.add_widget(accel)
imu_tab.add_widget(gyro)
imu_tab.add_widget(roll_pitch)
imu_tab.add_widget(EwGroup([pstat_pdyn, pdiff, altitude_bar, airspeed]))
imu_tab.add_widget(EwGroup([adc_temp, accel_gyro_temp]))
# imu_tab.add_widget(pstat_pdyn)
# imu_tab.add_widget(pdiff)
# imu_tab.add_widget(altitude_bar)
# imu_tab.add_widget(airspeed)
# imu_tab.add_widget(accel_gyro_temp)
# imu_tab.add_widget(adc_temp)

adc_tab.add_widget(EwGroup([io_adc1_ch0, io_adc1_ch1, io_adc1_ch2, io_adc1_ch3]))
adc_tab.add_widget(EwGroup([io_adc1_ch4, io_adc1_ch5, io_adc1_ch6, io_adc1_ch7]))
adc_tab.add_widget(EwGroup([io_adc2_ch0, io_adc2_ch1, io_adc2_ch2, io_adc2_ch3]))
adc_tab.add_widget(EwGroup([io_adc2_ch4, io_adc2_ch5, io_adc2_ch6, io_adc2_ch7]))

io_tab.add_widget(EwGroup([io_button1, io_button2, io_button3, io_button4]))
io_tab.add_widget(EwGroup([io_hall1, io_hall2, io_hall3, io_hall4]))
io_tab.add_widget(EwGroup([io_in1]))

gen_tab.add_widget(sin1)
gen_tab.add_widget(sin2)
gen_tab.add_widget(mean1)
gen_tab.add_widget(mean2)

sdtl_tab.add_widget(EwGroup([mon.get_stat_widget()]))

mon.app_window.print_bus_tree()
mon.run()
