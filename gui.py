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

main_tab = mon.add_tab('Main')
imu_tab = mon.add_tab('IMU')
adc_tab = mon.add_tab('ADC')
io_tab = mon.add_tab('IO')
cont_tab = mon.add_tab('Control')
gen_tab = mon.add_tab('Generators')
sdtl_tab = mon.add_tab('SDTL')

mon.mkdir(telemetry_dir_name)

basic_topics_root = mon_bus_name + '/' + telemetry_dir_name
drone_topics_root = basic_topics_root + '/' + 'drone'

cmd_sdtl_channel = SDTLchannel(name='cmd', ch_id=4, ch_type=SDTLchannelType.unrel)
mon.bridge_sdtl_udp(ip_in='0.0.0.0', port_in='20001',
                    ip_out=args.ip, port_out='20000',
                    bridge_to='telemetry',
                    additional_channels=[cmd_sdtl_channel])


# Data sources
ax = DataSourceEswbTopic('Acceleration x', path=f'{basic_topics_root}/nav/ang/a/x')
ay = DataSourceEswbTopic('Acceleration y', path=f'{basic_topics_root}/nav/ang/a/y')
az = DataSourceEswbTopic('Acceleration z', path=f'{basic_topics_root}/nav/ang/a/z')
wx = DataSourceEswbTopic('Angular rates x', path=f'{basic_topics_root}/nav/ang/omega/x', mult=57.32)
wy = DataSourceEswbTopic('Angular rates y', path=f'{basic_topics_root}/nav/ang/omega/y', mult=57.32)
wz = DataSourceEswbTopic('Angular rates z', path=f'{basic_topics_root}/nav/ang/omega/z', mult=57.32)
roll = DataSourceEswbTopic('Roll', path=f'{basic_topics_root}/nav/ang/roll', mult=57.32)
pitch = DataSourceEswbTopic('Pitch', path=f'{basic_topics_root}/nav/ang/pitch', mult=57.32)
yaw = DataSourceEswbTopic('Yaw', path=f'{basic_topics_root}/nav/ang/yaw', mult=57.32)

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

io_thermistor_1 = DataSourceEswbTopic('io_thermistor_1', path=f'{basic_topics_root}/dev/io/voltage/thermistor_1')
io_thermistor_2 = DataSourceEswbTopic('io_thermistor_2', path=f'{basic_topics_root}/dev/io/voltage/thermistor_2')
io_thermistor_3 = DataSourceEswbTopic('io_thermistor_3', path=f'{basic_topics_root}/dev/io/voltage/thermistor_3')
io_thermistor_4 = DataSourceEswbTopic('io_thermistor_4', path=f'{basic_topics_root}/dev/io/voltage/thermistor_4')
io_thermistor_5 = DataSourceEswbTopic('io_thermistor_5', path=f'{basic_topics_root}/dev/io/voltage/thermistor_5')
io_thermistor_6 = DataSourceEswbTopic('io_thermistor_6', path=f'{basic_topics_root}/dev/io/voltage/thermistor_6')
io_thermistor_7 = DataSourceEswbTopic('io_thermistor_7', path=f'{basic_topics_root}/dev/io/voltage/thermistor_7')
io_thermistor_8 = DataSourceEswbTopic('io_thermistor_8', path=f'{basic_topics_root}/dev/io/voltage/thermistor_8')
io_thermocouple_1 = DataSourceEswbTopic('io_thermocouple_1', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_1')
io_thermocouple_2 = DataSourceEswbTopic('io_thermocouple_2', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_2')
io_thermocouple_3 = DataSourceEswbTopic('io_thermocouple_3', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_3')
io_thermocouple_4 = DataSourceEswbTopic('io_thermocouple_4', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_4')
io_thermocouple_5 = DataSourceEswbTopic('io_thermocouple_5', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_5')
io_thermocouple_6 = DataSourceEswbTopic('io_thermocouple_6', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_6')
io_thermocouple_7 = DataSourceEswbTopic('io_thermocouple_7', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_7')
io_thermocouple_8 = DataSourceEswbTopic('io_thermocouple_8', path=f'{basic_topics_root}/dev/io/voltage/thermocouple_8')
io_r_left = DataSourceEswbTopic('io_r_left', path=f'{basic_topics_root}/dev/io/voltage/r_left')
io_r_right = DataSourceEswbTopic('io_r_right', path=f'{basic_topics_root}/dev/io/voltage/r_right')

io_button1 = DataSourceEswbTopic('io_button1', path=f'{basic_topics_root}/dev/io/digital/button1')
io_button2 = DataSourceEswbTopic('io_button2', path=f'{basic_topics_root}/dev/io/digital/button2')
io_button3 = DataSourceEswbTopic('io_button3', path=f'{basic_topics_root}/dev/io/digital/button3')
io_button4 = DataSourceEswbTopic('io_button4', path=f'{basic_topics_root}/dev/io/digital/button4')
io_cps1_period = DataSourceEswbTopic('io_cps1_period', path=f'{basic_topics_root}/dev/io/digital/cps1_period')
io_cps1_step = DataSourceEswbTopic('io_cps1_step', path=f'{basic_topics_root}/dev/io/digital/cps1_step')
io_cps1_tooth = DataSourceEswbTopic('io_cps1_tooth', path=f'{basic_topics_root}/dev/io/digital/cps1_tooth')
io_cps2_period = DataSourceEswbTopic('io_cps2_period', path=f'{basic_topics_root}/dev/io/digital/cps2_period')
io_cps2_step = DataSourceEswbTopic('io_cps2_step', path=f'{basic_topics_root}/dev/io/digital/cps2_step')
io_cps2_tooth = DataSourceEswbTopic('io_cps2_tooth', path=f'{basic_topics_root}/dev/io/digital/cps2_tooth')
io_in1 = DataSourceEswbTopic('io_in1', path=f'{basic_topics_root}/dev/io/digital/in1')

cont_output_motor = DataSourceEswbTopic('cont_output_motor', path=f'{basic_topics_root}/cont/output/motor')
cont_output_servo = DataSourceEswbTopic('cont_output_servo', path=f'{basic_topics_root}/cont/output/servo')
cont_output_relay = DataSourceEswbTopic('cont_output_relay', path=f'{basic_topics_root}/cont/output/relay')
cont_output_out1 = DataSourceEswbTopic('cont_output_out1', path=f'{basic_topics_root}/cont/output/out1')
cont_output_out2 = DataSourceEswbTopic('cont_output_out2', path=f'{basic_topics_root}/cont/output/out2')
cont_output_l1 = DataSourceEswbTopic('cont_output_l1', path=f'{basic_topics_root}/cont/output/l1')
cont_output_l2 = DataSourceEswbTopic('cont_output_l2', path=f'{basic_topics_root}/cont/output/l2')
cont_output_l3 = DataSourceEswbTopic('cont_output_l3', path=f'{basic_topics_root}/cont/output/l3')
cont_output_l4 = DataSourceEswbTopic('cont_output_l4', path=f'{basic_topics_root}/cont/output/l4')
cont_output_phase = DataSourceEswbTopic('cont_output_phase', path=f'{basic_topics_root}/cont/output/phase')
cont_output_overheat_tc = DataSourceEswbTopic('cont_output_overheat_tc', path=f'{basic_topics_root}/cont/output/overheat_tc')
cont_output_overheat_th = DataSourceEswbTopic('cont_output_overheat_th', path=f'{basic_topics_root}/cont/output/overheat_th')
cont_output_status = DataSourceEswbTopic('cont_output_status', path=f'{basic_topics_root}/cont/output/status')
cont_rpm1 = DataSourceEswbTopic('cont_rpm1', path=f'{basic_topics_root}/cont/output/rpm1', mult=60.0)
cont_rpm2 = DataSourceEswbTopic('cont_rpm2', path=f'{basic_topics_root}/cont/output/rpm2', mult=60.0)

cont_error = DataSourceEswbTopic('cont_state', path=f'{basic_topics_root}/cont/internal/error')
cont_mode = DataSourceEswbTopic('cont_state', path=f'{basic_topics_root}/cont/internal/mode')
cont_oh_tc = DataSourceEswbTopic('cont_oh_tc', path=f'{basic_topics_root}/cont/internal/overheat_tc_status')
cont_oh_th = DataSourceEswbTopic('cont_oh_th', path=f'{basic_topics_root}/cont/internal/overheat_th_status')

cont_state_status_enum = DataSourceEnum(name='Status', sources=[cont_error],
                                        enum_table={
    0: 'CONNECTED',
    1: 'DISCONNECTED'})
cont_state_mode_enum = DataSourceEnum(name='Mode', sources=[cont_mode],
                                      enum_table={
    1: 'DISARM',
    2: 'MANUAL',
    3: 'ANGRATES',
    4: 'SPECIAL'})
cont_state_overheat_tc_enum = DataSourceEnum(name='Temperature status 1', sources=[cont_oh_tc],
                                      enum_table={
    0: 'NORMAL',
    1: 'OVERHEAT'})
cont_state_overheat_th_enum = DataSourceEnum(name='Temperature status 2', sources=[cont_oh_th],
                                      enum_table={
    0: 'NORMAL',
    1: 'OVERHEAT'})

sin1 = DataSourceEswbTopic('sin1', path=f'{basic_topics_root}/hk/gen/sin1')
sin2 = DataSourceEswbTopic('sin2', path=f'{basic_topics_root}/hk/gen/sin2')
mean1 = DataSourceEswbTopic('mean1', path=f'{basic_topics_root}/hk/gen/mean1')
mean2 = DataSourceEswbTopic('mean2', path=f'{basic_topics_root}/hk/gen/mean2')

# Charts
sin1 = EwChart([sin1], title="Sin1")
sin2 = EwChart([sin2], title="Sin2")
mean1 = EwChart([mean1], title="Mean1")
mean2 = EwChart([mean2], title="Mean2")

# title='<span style="color: #000">Accelerations</span>',


accel_chart = EwChart([ax, ay, az], 
                title='Accelerations',
                labels={'left': 'm/s²', 'bottom': 'time'})
gyro_chart = EwChart([wx, wy, wz], 
               title="Angular rates",
               labels={'left': 'deg/s', 'bottom': 'time'})
roll_pitch_chart = EwChart([roll, pitch], 
                     title="Angles",
                     labels={'left': 'deg', 'bottom': 'time'})
yaw_chart = EwChart([yaw], 
              title="Angles",
              labels={'left': 'deg', 'bottom': 'time'})

accel_gyro_temp_chart = EwChart([tax, tay, taz, twx, twy, twz], 
                          title="Sensor temperatures",
                          labels={'left': '°C', 'bottom': 'time'})
adc_temp_chart = EwChart([tadc], 
                   title="ADC temperature",
                   labels={'left': '°C', 'bottom': 'time'})

pstat_pdyn_chart = EwChart([pstat, pdyn], 
                     title="Static and dynamic pressure",
                     labels={'left': 'Pa', 'bottom': 'time'})
pdiff_chart = EwChart([pdiff], 
                title="Differential pressure",
                labels={'left': 'Pa', 'bottom': 'time'})

altitude_bar_chart = EwChart([altitude_bar], 
                       title="Barometric altitude",
                       labels={'left': 'm', 'bottom': 'time'})
airspeed_chart = EwChart([airspeed], 
                   title="Airspeed",
                   labels={'left': 'm/s', 'bottom': 'time'})

io_thermistor_1_chart = EwChart([io_thermistor_1], title="Thermistor 1", labels={'left': 'V', 'bottom': 'time'})
io_thermistor_2_chart = EwChart([io_thermistor_2], title="Thermistor 2", labels={'left': 'V', 'bottom': 'time'})
io_thermistor_3_chart = EwChart([io_thermistor_3], title="Thermistor 3", labels={'left': 'V', 'bottom': 'time'})
io_thermistor_4_chart = EwChart([io_thermistor_4], title="Thermistor 4", labels={'left': 'V', 'bottom': 'time'})
io_thermistor_5_chart = EwChart([io_thermistor_5], title="Thermistor", labels={'left': 'V', 'bottom': 'time'})
io_thermistor_6_chart = EwChart([io_thermistor_6], title="Thermistor 6", labels={'left': 'V', 'bottom': 'time'})
io_thermistor_7_chart = EwChart([io_thermistor_7], title="Thermistor 7", labels={'left': 'V', 'bottom': 'time'})
io_thermistor_8_chart = EwChart([io_thermistor_8], title="Thermistor 8", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_1_chart = EwChart([io_thermocouple_1], title="Thermocouple 1", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_2_chart = EwChart([io_thermocouple_2], title="Thermocouple 2", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_3_chart = EwChart([io_thermocouple_3], title="Thermocouple 3", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_4_chart = EwChart([io_thermocouple_4], title="Thermocouple 4", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_5_chart = EwChart([io_thermocouple_5], title="Thermocouple", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_6_chart = EwChart([io_thermocouple_6], title="Thermocouple 6", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_7_chart = EwChart([io_thermocouple_7], title="Thermocouple 7", labels={'left': 'V', 'bottom': 'time'})
io_thermocouple_8_chart = EwChart([io_thermocouple_8], title="Thermocouple 8", labels={'left': 'V', 'bottom': 'time'})
io_r_left_chart = EwChart([io_r_left], title="R left", labels={'left': 'V', 'bottom': 'time'})
io_r_right_chart = EwChart([io_r_right], title="R right", labels={'left': 'V', 'bottom': 'time'})

io_button1_chart = EwChart([io_button1], title="Button 1", labels={'left': '0/1', 'bottom': 'time'})
io_button2_chart = EwChart([io_button2], title="Button 2", labels={'left': '0/1', 'bottom': 'time'})
io_button3_chart = EwChart([io_button3], title="Button 3", labels={'left': '0/1', 'bottom': 'time'})
io_button4_chart = EwChart([io_button4], title="Button 4", labels={'left': '0/1', 'bottom': 'time'})
cont_rpm1_chart = EwChart([cont_rpm1], title="Motor 1 RPM", labels={'left': 'RPM', 'bottom': 'time'})
cont_rpm2_chart = EwChart([cont_rpm2], title="Motor 2 RPM", labels={'left': 'RPM', 'bottom': 'time'})
io_in1_chart = EwChart([io_in1], title="IN 1", labels={'left': '0/1', 'bottom': 'time'})

io_cps1_period_chart = EwChart([io_cps1_period], title="cps 1 period", labels={'left': 'us', 'bottom': 'time'})
io_cps1_tooth_chart = EwChart([io_cps1_tooth], title="cps 1 tooth", labels={'left': 'us', 'bottom': 'time'})
io_cps1_step_chart = EwChart([io_cps1_step], title="cps 1 step", labels={'left': 'us', 'bottom': 'time'})
io_cps2_period_chart = EwChart([io_cps2_period], title="cps 2 period", labels={'left': 'us', 'bottom': 'time'})
io_cps2_tooth_chart = EwChart([io_cps2_tooth], title="cps 2 tooth", labels={'left': 'us', 'bottom': 'time'})
io_cps2_step_chart = EwChart([io_cps2_step], title="cps 2 step", labels={'left': 'us', 'bottom': 'time'})

cont_output_motor_chart = EwChart([cont_output_motor], title="Motor control signal", labels={'left': '[0, 1]', 'bottom': 'time'})
cont_output_servo_chart = EwChart([cont_output_servo], title="Servo control signal", labels={'left': '[-1, 1]', 'bottom': 'time'})
cont_output_relay_chart = EwChart([cont_output_relay], title="Relay", labels={'left': '', 'bottom': 'time'})
cont_output_out1_chart = EwChart([cont_output_out1], title="Out 1", labels={'left': '', 'bottom': 'time'})
cont_output_out2_chart = EwChart([cont_output_out2], title="Out 2", labels={'left': '', 'bottom': 'time'})
cont_output_l1_chart = EwChart([cont_output_l1], title="L1", labels={'left': '', 'bottom': 'time'})
cont_output_l2_chart = EwChart([cont_output_l2], title="L2", labels={'left': '', 'bottom': 'time'})
cont_output_l3_chart = EwChart([cont_output_l3], title="L3", labels={'left': '', 'bottom': 'time'})
cont_output_l4_chart = EwChart([cont_output_l4], title="L4", labels={'left': '', 'bottom': 'time'})
cont_output_phase_chart = EwChart([cont_output_phase], title="Phase", labels={'left': '', 'bottom': 'time'})
cont_output_overheat_tc_chart = EwChart([cont_output_overheat_tc], title="Overheat TC", labels={'left': '', 'bottom': 'time'})
cont_output_overheat_th_chart = EwChart([cont_output_overheat_th], title="Overheat TH", labels={'left': '', 'bottom': 'time'})
cont_output_status_chart = EwChart([cont_output_status], title="Status", labels={'left': '', 'bottom': 'time'})

# Main
ai = EwAttitudeIndicator([pitch, roll])
hi = EwHeadingIndicator([yaw])

state_table = EwTable(caption='Information', data_sources=[
    cont_state_status_enum,
    cont_state_mode_enum,
    cont_state_overheat_tc_enum,
    cont_state_overheat_th_enum,
    roll,
    pitch,
])

# Add widgets
imu_tab.add_widget(accel_chart)
imu_tab.add_widget(gyro_chart)
imu_tab.add_widget(roll_pitch_chart)
imu_tab.add_widget(EwGroup([pstat_pdyn_chart, pdiff_chart, altitude_bar_chart, airspeed_chart]))
imu_tab.add_widget(EwGroup([adc_temp_chart, accel_gyro_temp_chart]))

adc_tab.add_widget(EwGroup([io_thermistor_1_chart, io_thermistor_2_chart, io_thermistor_3_chart, io_thermistor_4_chart]))
adc_tab.add_widget(EwGroup([io_thermistor_5_chart, io_thermistor_6_chart, io_thermistor_7_chart, io_thermistor_8_chart]))
adc_tab.add_widget(EwGroup([io_thermocouple_1_chart, io_thermocouple_2_chart, io_thermocouple_3_chart, io_thermocouple_4_chart]))
adc_tab.add_widget(EwGroup([io_thermocouple_5_chart, io_thermocouple_6_chart, io_thermocouple_7_chart, io_thermocouple_8_chart]))
adc_tab.add_widget(EwGroup([io_r_left_chart, io_r_right_chart]))

io_tab.add_widget(EwGroup([io_button1_chart, io_button2_chart, io_button3_chart, io_button4_chart]))
io_tab.add_widget(EwGroup([io_cps1_period_chart, io_cps1_step_chart, io_cps1_tooth_chart]))
io_tab.add_widget(EwGroup([io_cps2_period_chart, io_cps2_step_chart, io_cps2_tooth_chart]))
io_tab.add_widget(EwGroup([io_in1_chart]))

cont_tab.add_widget(EwGroup([cont_output_motor_chart, cont_output_servo_chart, cont_output_relay_chart]))
cont_tab.add_widget(EwGroup([cont_output_out1_chart, cont_output_out2_chart]))
cont_tab.add_widget(EwGroup([cont_output_l1_chart, cont_output_l2_chart, cont_output_l3_chart, cont_output_l4_chart]))
cont_tab.add_widget(EwGroup([cont_output_phase_chart, cont_output_overheat_tc_chart, cont_output_overheat_th_chart]))
cont_tab.add_widget(EwGroup([cont_output_status_chart]))

gen_tab.add_widget(sin1)
gen_tab.add_widget(mean1)
gen_tab.add_widget(sin2)
gen_tab.add_widget(mean2)

main_tab.add_widget(state_table)
main_tab.add_widget(EwGroup([state_table, ai, hi]))
main_tab.add_widget(EwGroup([roll_pitch_chart, accel_chart, gyro_chart, altitude_bar_chart]))
main_tab.add_widget(EwGroup([io_thermistor_5_chart, io_thermocouple_5_chart]))
main_tab.add_widget(EwGroup([cont_output_motor_chart, cont_output_servo_chart]))
main_tab.add_widget(EwGroup([cont_rpm1_chart, cont_rpm2_chart]))

sdtl_tab.add_widget(EwGroup([mon.get_stat_widget()]))

mon.app_window.print_bus_tree()
mon.run()
