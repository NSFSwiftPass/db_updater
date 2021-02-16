# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Integer, MetaData, Numeric, SmallInteger, String, Table

metadata = MetaData()


t_PUBACC_AN = Table(
    'PUBACC_AN', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('antenna_action_performed', CHAR(1)),
    Column('antenna_number', Integer, nullable=False),
    Column('location_number', Integer),
    Column('receive_zone_code', CHAR(6)),
    Column('antenna_type_code', CHAR(1)),
    Column('height_to_tip', Numeric(5, 1)),
    Column('height_to_center_raat', Numeric(5, 1)),
    Column('antenna_make', String(25)),
    Column('antenna_model', String(25)),
    Column('tilt', Numeric(3, 1)),
    Column('polarization_code', CHAR(5)),
    Column('beamwidth', Numeric(4, 1)),
    Column('gain', Numeric(4, 1)),
    Column('azimuth', Numeric(4, 1)),
    Column('height_above_avg_terrain', Numeric(5, 1)),
    Column('diversity_height', Numeric(5, 1)),
    Column('diversity_gain', Numeric(4, 1)),
    Column('diversity_beam', Numeric(4, 1)),
    Column('reflector_height', Numeric(5, 1)),
    Column('reflector_width', Numeric(4, 1)),
    Column('reflector_separation', Numeric(5, 1)),
    Column('repeater_seq_num', Integer),
    Column('back_to_back_tx_dish_gain', Numeric(4, 1)),
    Column('back_to_back_rx_dish_gain', Numeric(4, 1)),
    Column('location_name', String(20)),
    Column('passive_repeater_id', Integer),
    Column('alternative_cgsa_method', CHAR(1)),
    Column('path_number', Integer),
    Column('line_loss', Numeric(3, 1)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    Column('psd_nonpsd_methodology', String(10)),
    Column('maximum_erp', Numeric(15, 3)),
    schema='dds_users'
)


t_PUBACC_EN = Table(
    'PUBACC_EN', metadata,
    Column('record_type', CHAR(2), nullable=False),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('entity_type', CHAR(2)),
    Column('licensee_id', CHAR(9)),
    Column('entity_name', String(200)),
    Column('first_name', String(20)),
    Column('mi', CHAR(1)),
    Column('last_name', String(20)),
    Column('suffix', CHAR(3)),
    Column('phone', CHAR(10)),
    Column('fax', CHAR(10)),
    Column('email', String(50)),
    Column('street_address', String(60)),
    Column('city', String(20)),
    Column('state', CHAR(2)),
    Column('zip_code', CHAR(9)),
    Column('po_box', String(20)),
    Column('attention_line', String(35)),
    Column('sgin', CHAR(3)),
    Column('frn', CHAR(10)),
    Column('applicant_type_code', CHAR(1)),
    Column('applicant_type_other', CHAR(40)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_FC = Table(
    'PUBACC_FC', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('coordination_number', CHAR(25)),
    Column('coordinator_name', String(40)),
    Column('coordinator_phone', CHAR(10)),
    Column('freq_coordination_date', CHAR(10)),
    Column('action_performed', CHAR(1)),
    schema='dds_users'
)


t_PUBACC_FF = Table(
    'PUBACC_FF', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0)),
    Column('call_sign', CHAR(10)),
    Column('location_number', Integer),
    Column('antenna_number', Integer),
    Column('frequency', Numeric(16, 8)),
    Column('frequency_number', Integer),
    Column('freq_freeform_cond_type', CHAR(1)),
    Column('unique_freq_freeform_id', Numeric(9, 0)),
    Column('sequence_number', Integer),
    Column('freq_freeform_condition', String(255)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_FR = Table(
    'PUBACC_FR', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('frequency_action_performed', CHAR(1)),
    Column('location_number', Integer),
    Column('antenna_number', Integer),
    Column('class_station_code', CHAR(4)),
    Column('op_altitude_code', CHAR(2)),
    Column('frequency_assigned', Numeric(16, 8)),
    Column('frequency_upper_band', Numeric(16, 8)),
    Column('frequency_carrier', Numeric(16, 8)),
    Column('time_begin_operations', Integer),
    Column('time_end_operations', Integer),
    Column('power_output', Numeric(15, 3)),
    Column('power_erp', Numeric(15, 3)),
    Column('tolerance', Numeric(6, 5)),
    Column('frequency_ind', CHAR(1)),
    Column('status', CHAR(1)),
    Column('eirp', Numeric(7, 1)),
    Column('transmitter_make', String(25)),
    Column('transmitter_model', String(25)),
    Column('auto_transmitter_power_control', CHAR(1)),
    Column('cnt_mobile_units', Integer),
    Column('cnt_mob_pagers', Integer),
    Column('freq_seq_id', Integer),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    Column('date_first_used', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_FS = Table(
    'PUBACC_FS', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('call_sign', CHAR(10)),
    Column('location_number', Integer),
    Column('antenna_number', Integer),
    Column('frequency', Numeric(16, 8)),
    Column('frequency_number', Integer),
    Column('special_condition_type', CHAR(1)),
    Column('special_condition_code', Integer),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_FT = Table(
    'PUBACC_FT', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('call_sign', CHAR(10)),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('freq_type_action_performed', CHAR(1)),
    Column('location_number', Integer),
    Column('antenna_number', Integer),
    Column('frequency_assigned', Numeric(16, 8)),
    Column('frequency_type_number', Integer),
    Column('frequency_type_code', CHAR(2)),
    schema='dds_users'
)


t_PUBACC_IR = Table(
    'PUBACC_IR', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('call_sign', CHAR(10)),
    Column('uls_file_number', CHAR(14)),
    Column('location_number', Integer),
    Column('antenna_number', Integer),
    Column('frequency_assigned', Numeric(16, 8)),
    Column('irac_result', CHAR(2)),
    Column('fas_docket_num', CHAR(8)),
    Column('fccm_num', CHAR(10)),
    Column('faa_ng_num', CHAR(11)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    Column('a_irac_status_code', SmallInteger),
    schema='dds_users'
)


t_PUBACC_L3 = Table(
    'PUBACC_L3', metadata,
    Column('record_type', CHAR(2), nullable=False),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('lease_id', CHAR(10)),
    Column('ls_site_link_id', Numeric(9, 0)),
    Column('location_action_performed', CHAR(1)),
    Column('location_type_code', CHAR(1)),
    Column('location_class_code', CHAR(1)),
    Column('location_number', Integer),
    Column('site_status', CHAR(1)),
    Column('corresponding_fixed_location', Integer),
    Column('location_address', String(80)),
    Column('location_city', CHAR(20)),
    Column('location_county', String(60)),
    Column('location_state', CHAR(2)),
    Column('radius_of_operation', Numeric(5, 1)),
    Column('area_of_operation_code', CHAR(1)),
    Column('clearance_indicator', CHAR(1)),
    Column('ground_elevation', Numeric(7, 1)),
    Column('lat_degrees', Integer),
    Column('lat_minutes', Integer),
    Column('lat_seconds', Numeric(3, 1)),
    Column('lat_direction', CHAR(1)),
    Column('long_degrees', Integer),
    Column('long_minutes', Integer),
    Column('long_seconds', Numeric(3, 1)),
    Column('long_direction', CHAR(1)),
    Column('max_lat_degrees', Integer),
    Column('max_lat_minutes', Integer),
    Column('max_lat_seconds', Numeric(3, 1)),
    Column('max_lat_direction', CHAR(1)),
    Column('max_long_degrees', Integer),
    Column('max_long_minutes', Integer),
    Column('max_long_seconds', Numeric(3, 1)),
    Column('max_long_direction', CHAR(1)),
    Column('nepa', CHAR(1)),
    Column('quiet_zone_notification_date', CHAR(10)),
    Column('tower_registration_number', CHAR(10)),
    Column('height_of_support_structure', Numeric(7, 1)),
    Column('overall_height_of_structure', Numeric(7, 1)),
    Column('structure_type', CHAR(7)),
    Column('airport_id', CHAR(4)),
    Column('location_name', CHAR(20)),
    Column('units_hand_held', Integer),
    Column('units_mobile', Integer),
    Column('units_temp_fixed', Integer),
    Column('units_aircraft', Integer),
    Column('units_itinerant', Integer),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_L4 = Table(
    'PUBACC_L4', metadata,
    Column('record_type', CHAR(2), nullable=False),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('lease_id', CHAR(10)),
    Column('ls_site_link_id', Numeric(9, 0)),
    Column('location_action_performed', CHAR(1)),
    Column('location_number', Integer),
    Column('registration_required', CHAR(1)),
    Column('protection_date', DateTime(True)),
    Column('link_reg_num', String(30)),
    Column('link_reg_action_performed', CHAR(1)),
    Column('mexico_clearance_indicator', CHAR(1)),
    Column('quiet_zone_consent', CHAR(1)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_L5 = Table(
    'PUBACC_L5', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('call_sign', CHAR(10)),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('lease_id', CHAR(10)),
    Column('ls_site_link_id', Numeric(9, 0)),
    Column('location_number', Integer),
    Column('special_condition_type', CHAR(1)),
    Column('special_condition_code', Integer),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_L6 = Table(
    'PUBACC_L6', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('callsign', CHAR(10)),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('lease_id', CHAR(10)),
    Column('ls_site_link_id', Numeric(9, 0)),
    Column('location_number', Integer),
    Column('loc_freeform_cond_type', CHAR(1)),
    Column('unique_loc_freeform_id', Numeric(9, 0)),
    Column('sequence_number', Integer),
    Column('loc_freeform_condition', String(255)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_LA = Table(
    'PUBACC_LA', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0)),
    Column('callsign', CHAR(10)),
    Column('attachment_code', CHAR(1)),
    Column('attachment_desc', String(60)),
    Column('attachment_date', CHAR(10)),
    Column('attachment_filename', String(60)),
    Column('action_performed', CHAR(1)),
    schema='dds_users'
)


t_PUBACC_LC = Table(
    'PUBACC_LC', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('a_ls_class_code', CHAR(2)),
    Column('a_ls_allocation_type', CHAR(1)),
    Column('a_ls_term', CHAR(1)),
    schema='dds_users'
)


t_PUBACC_LD = Table(
    'PUBACC_LD', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('lease_id', CHAR(10)),
    Column('issue_date', DateTime(True)),
    Column('expired_date', DateTime(True)),
    Column('cancellation_date', DateTime(True)),
    Column('lease_never_comm_ind', CHAR(1)),
    schema='dds_users'
)


t_PUBACC_LF = Table(
    'PUBACC_LF', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0)),
    Column('callsign', CHAR(10)),
    Column('location_number', Integer),
    Column('loc_freeform_cond_type', CHAR(1)),
    Column('unique_loc_freeform_id', Numeric(9, 0)),
    Column('sequence_number', Integer),
    Column('loc_freeform_condition', String(255)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_LO = Table(
    'PUBACC_LO', metadata,
    Column('record_type', CHAR(2), nullable=False),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('call_sign', CHAR(10)),
    Column('ebf_number', String(30)),
    Column('location_action_performed', CHAR(1)),
    Column('location_type_code', CHAR(1)),
    Column('location_class_code', CHAR(1)),
    Column('location_number', Integer),
    Column('site_status', CHAR(1)),
    Column('corresponding_fixed_location', Integer),
    Column('location_address', String(80)),
    Column('location_city', CHAR(20)),
    Column('location_county', String(60)),
    Column('location_state', CHAR(2)),
    Column('radius_of_operation', Numeric(5, 1)),
    Column('area_of_operation_code', CHAR(1)),
    Column('clearance_indicator', CHAR(1)),
    Column('ground_elevation', Numeric(7, 1)),
    Column('lat_degrees', Integer),
    Column('lat_minutes', Integer),
    Column('lat_seconds', Numeric(3, 1)),
    Column('lat_direction', CHAR(1)),
    Column('long_degrees', Integer),
    Column('long_minutes', Integer),
    Column('long_seconds', Numeric(3, 1)),
    Column('long_direction', CHAR(1)),
    Column('max_lat_degrees', Integer),
    Column('max_lat_minutes', Integer),
    Column('max_lat_seconds', Numeric(3, 1)),
    Column('max_lat_direction', CHAR(1)),
    Column('max_long_degrees', Integer),
    Column('max_long_minutes', Integer),
    Column('max_long_seconds', Numeric(3, 1)),
    Column('max_long_direction', CHAR(1)),
    Column('nepa', CHAR(1)),
    Column('quiet_zone_notification_date', CHAR(10)),
    Column('tower_registration_number', CHAR(10)),
    Column('height_of_support_structure', Numeric(7, 1)),
    Column('overall_height_of_structure', Numeric(7, 1)),
    Column('structure_type', CHAR(7)),
    Column('airport_id', CHAR(4)),
    Column('location_name', CHAR(20)),
    Column('units_hand_held', Integer),
    Column('units_mobile', Integer),
    Column('units_temp_fixed', Integer),
    Column('units_aircraft', Integer),
    Column('units_itinerant', Integer),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    Column('earth_agree', CHAR(1)),
    schema='dds_users'
)


t_PUBACC_LS = Table(
    'PUBACC_LS', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('call_sign', CHAR(10)),
    Column('location_number', Integer),
    Column('special_condition_type', CHAR(1)),
    Column('special_condition_code', Integer),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_MW = Table(
    'PUBACC_MW', metadata,
    Column('record_type', CHAR(2), nullable=False),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('pack_indicator', CHAR(1)),
    Column('pack_registration_num', Integer),
    Column('pack_name', String(50)),
    Column('type_of_operation', String(45)),
    Column('smsa_code', CHAR(6)),
    Column('station_class', CHAR(4)),
    Column('cum_effect_is_major', CHAR(1)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)


t_PUBACC_RC = Table(
    'PUBACC_RC', metadata,
    Column('record_type', CHAR(2)),
    Column('unique_system_identifier', Numeric(9, 0), nullable=False),
    Column('uls_file_number', CHAR(14)),
    Column('ebf_number', String(30)),
    Column('call_sign', CHAR(10)),
    Column('radial_action_performed', CHAR(1)),
    Column('location_number', Integer),
    Column('antenna_number', Integer),
    Column('receiver_make', String(25)),
    Column('receiver_model', String(25)),
    Column('receiver_stability', Numeric(6, 5)),
    Column('receiver_noise_figure', Numeric(5, 2)),
    Column('status_code', CHAR(1)),
    Column('status_date', DateTime(True)),
    schema='dds_users'
)
