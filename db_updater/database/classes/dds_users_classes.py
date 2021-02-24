# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Integer, Numeric, SmallInteger, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PUBACCAN(Base):
    __tablename__ = 'PUBACC_AN'
    __table_args__ = {'schema': 'dds_users'}

    record_type = Column(CHAR(2))
    unique_system_identifier = Column(Numeric(9, 0), primary_key=True, nullable=False)
    uls_file_number = Column(CHAR(14))
    ebf_number = Column(String(30))
    call_sign = Column(CHAR(10))
    antenna_action_performed = Column(CHAR(1))
    antenna_number = Column(Integer, primary_key=True, nullable=False)
    location_number = Column(Integer, primary_key=True, nullable=False)
    receive_zone_code = Column(CHAR(6))
    antenna_type_code = Column(CHAR(1))
    height_to_tip = Column(Numeric(5, 1))
    height_to_center_raat = Column(Numeric(5, 1))
    antenna_make = Column(String(25))
    antenna_model = Column(String(25))
    tilt = Column(Numeric(3, 1))
    polarization_code = Column(CHAR(5))
    beamwidth = Column(Numeric(4, 1))
    gain = Column(Numeric(4, 1))
    azimuth = Column(Numeric(4, 1))
    height_above_avg_terrain = Column(Numeric(5, 1))
    diversity_height = Column(Numeric(5, 1))
    diversity_gain = Column(Numeric(4, 1))
    diversity_beam = Column(Numeric(4, 1))
    reflector_height = Column(Numeric(5, 1))
    reflector_width = Column(Numeric(4, 1))
    reflector_separation = Column(Numeric(5, 1))
    repeater_seq_num = Column(Integer)
    back_to_back_tx_dish_gain = Column(Numeric(4, 1))
    back_to_back_rx_dish_gain = Column(Numeric(4, 1))
    location_name = Column(String(20))
    passive_repeater_id = Column(Integer)
    alternative_cgsa_method = Column(CHAR(1))
    path_number = Column(Integer)
    line_loss = Column(Numeric(3, 1))
    status_code = Column(CHAR(1))
    status_date = Column(DateTime(True))
    psd_nonpsd_methodology = Column(String(10))
    maximum_erp = Column(Numeric(15, 3))


class PUBACCEN(Base):
    __tablename__ = 'PUBACC_EN'
    __table_args__ = {'schema': 'dds_users'}

    record_type = Column(CHAR(2), nullable=False)
    unique_system_identifier = Column(Numeric(9, 0), primary_key=True, nullable=False)
    uls_file_number = Column(CHAR(14))
    ebf_number = Column(String(30))
    call_sign = Column(CHAR(10))
    entity_type = Column(CHAR(2), primary_key=True, nullable=False)
    licensee_id = Column(CHAR(9))
    entity_name = Column(String(200))
    first_name = Column(String(20))
    mi = Column(CHAR(1))
    last_name = Column(String(20))
    suffix = Column(CHAR(3))
    phone = Column(CHAR(10))
    fax = Column(CHAR(10))
    email = Column(String(50))
    street_address = Column(String(60))
    city = Column(String(20))
    state = Column(CHAR(2))
    zip_code = Column(CHAR(9))
    po_box = Column(String(20))
    attention_line = Column(String(35))
    sgin = Column(CHAR(3))
    frn = Column(CHAR(10))
    applicant_type_code = Column(CHAR(1))
    applicant_type_other = Column(CHAR(40))
    status_code = Column(CHAR(1))
    status_date = Column(DateTime(True))


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


class PUBACCFR(Base):
    __tablename__ = 'PUBACC_FR'
    __table_args__ = {'schema': 'dds_users'}

    record_type = Column(CHAR(2))
    unique_system_identifier = Column(Numeric(9, 0), primary_key=True, nullable=False)
    uls_file_number = Column(CHAR(14))
    ebf_number = Column(String(30))
    call_sign = Column(CHAR(10))
    frequency_action_performed = Column(CHAR(1))
    location_number = Column(Integer, primary_key=True, nullable=False)
    antenna_number = Column(Integer, primary_key=True, nullable=False)
    class_station_code = Column(CHAR(4))
    op_altitude_code = Column(CHAR(2))
    frequency_assigned = Column(Numeric(16, 8))
    frequency_upper_band = Column(Numeric(16, 8))
    frequency_carrier = Column(Numeric(16, 8))
    time_begin_operations = Column(Integer)
    time_end_operations = Column(Integer)
    power_output = Column(Numeric(15, 3))
    power_erp = Column(Numeric(15, 3))
    tolerance = Column(Numeric(6, 5))
    frequency_ind = Column(CHAR(1))
    status = Column(CHAR(1))
    eirp = Column(Numeric(7, 1))
    transmitter_make = Column(String(25))
    transmitter_model = Column(String(25))
    auto_transmitter_power_control = Column(CHAR(1))
    cnt_mobile_units = Column(Integer)
    cnt_mob_pagers = Column(Integer)
    freq_seq_id = Column(Integer, primary_key=True, nullable=False)
    status_code = Column(CHAR(1))
    status_date = Column(DateTime(True))
    date_first_used = Column(DateTime(True))


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


class PUBACCLO(Base):
    __tablename__ = 'PUBACC_LO'
    __table_args__ = {'schema': 'dds_users'}

    record_type = Column(CHAR(2), nullable=False)
    unique_system_identifier = Column(Numeric(9, 0), primary_key=True, nullable=False)
    uls_file_number = Column(CHAR(14))
    ebf_number = Column(String(30))
    call_sign = Column(CHAR(10))
    location_action_performed = Column(CHAR(1))
    location_type_code = Column(CHAR(1))
    location_class_code = Column(CHAR(1))
    location_number = Column(Integer, primary_key=True, nullable=False)
    site_status = Column(CHAR(1))
    corresponding_fixed_location = Column(Integer)
    location_address = Column(String(80))
    location_city = Column(CHAR(20))
    location_county = Column(String(60))
    location_state = Column(CHAR(2))
    radius_of_operation = Column(Numeric(5, 1))
    area_of_operation_code = Column(CHAR(1))
    clearance_indicator = Column(CHAR(1))
    ground_elevation = Column(Numeric(7, 1))
    lat_degrees = Column(Integer)
    lat_minutes = Column(Integer)
    lat_seconds = Column(Numeric(3, 1))
    lat_direction = Column(CHAR(1))
    long_degrees = Column(Integer)
    long_minutes = Column(Integer)
    long_seconds = Column(Numeric(3, 1))
    long_direction = Column(CHAR(1))
    max_lat_degrees = Column(Integer)
    max_lat_minutes = Column(Integer)
    max_lat_seconds = Column(Numeric(3, 1))
    max_lat_direction = Column(CHAR(1))
    max_long_degrees = Column(Integer)
    max_long_minutes = Column(Integer)
    max_long_seconds = Column(Numeric(3, 1))
    max_long_direction = Column(CHAR(1))
    nepa = Column(CHAR(1))
    quiet_zone_notification_date = Column(CHAR(10))
    tower_registration_number = Column(CHAR(10))
    height_of_support_structure = Column(Numeric(7, 1))
    overall_height_of_structure = Column(Numeric(7, 1))
    structure_type = Column(CHAR(7))
    airport_id = Column(CHAR(4))
    location_name = Column(CHAR(20))
    units_hand_held = Column(Integer)
    units_mobile = Column(Integer)
    units_temp_fixed = Column(Integer)
    units_aircraft = Column(Integer)
    units_itinerant = Column(Integer)
    status_code = Column(CHAR(1))
    status_date = Column(DateTime(True))
    earth_agree = Column(CHAR(1))


class PUBACCL(Base):
    __tablename__ = 'PUBACC_LS'
    __table_args__ = {'schema': 'dds_users'}

    record_type = Column(CHAR(2))
    unique_system_identifier = Column(Numeric(9, 0), primary_key=True, nullable=False)
    call_sign = Column(CHAR(10))
    location_number = Column(Integer, primary_key=True, nullable=False)
    special_condition_type = Column(CHAR(1))
    special_condition_code = Column(Integer)
    status_code = Column(CHAR(1))
    status_date = Column(DateTime(True))


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
