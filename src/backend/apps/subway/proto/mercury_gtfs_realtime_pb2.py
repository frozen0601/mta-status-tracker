# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mercury-gtfs-realtime.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from subway.proto import gtfs_realtime_pb2 as gtfs__realtime__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="mercury-gtfs-realtime.proto",
    package="transit_realtime",
    syntax="proto2",
    serialized_options=b"\n\033com.google.transit.realtime",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1bmercury-gtfs-realtime.proto\x12\x10transit_realtime\x1a\x13gtfs-realtime.proto",\n\x11MercuryFeedHeader\x12\x17\n\x0fmercury_version\x18\x01 \x02(\t"\x89\x01\n\x19MercuryStationAlternative\x12\x39\n\x0f\x61\x66\x66\x65\x63ted_entity\x18\x01 \x02(\x0b\x32 .transit_realtime.EntitySelector\x12\x31\n\x05notes\x18\x02 \x02(\x0b\x32".transit_realtime.TranslatedString"\xfa\x03\n\x0cMercuryAlert\x12\x12\n\ncreated_at\x18\x01 \x02(\x04\x12\x12\n\nupdated_at\x18\x02 \x02(\x04\x12\x12\n\nalert_type\x18\x03 \x02(\t\x12H\n\x13station_alternative\x18\x04 \x03(\x0b\x32+.transit_realtime.MercuryStationAlternative\x12\x1b\n\x13service_plan_number\x18\x05 \x03(\t\x12\x1c\n\x14general_order_number\x18\x06 \x03(\t\x12\x1d\n\x15\x64isplay_before_active\x18\x07 \x01(\x04\x12H\n\x1chuman_readable_active_period\x18\x08 \x01(\x0b\x32".transit_realtime.TranslatedString\x12\x16\n\x0e\x64irectionality\x18\t \x01(\x04\x12;\n\x11\x61\x66\x66\x65\x63ted_stations\x18\n \x03(\x0b\x32 .transit_realtime.EntitySelector\x12;\n\x0fscreens_summary\x18\x0b \x01(\x0b\x32".transit_realtime.TranslatedString\x12\x1c\n\x14no_affected_stations\x18\x0c \x01(\x08\x12\x10\n\x08\x63lone_id\x18\r \x01(\t"\xdc\x08\n\x15MercuryEntitySelector\x12\x12\n\nsort_order\x18\x01 \x02(\t"\xae\x08\n\x08Priority\x12!\n\x1dPRIORITY_NO_SCHEDULED_SERVICE\x10\x01\x12\x1f\n\x1bPRIORITY_INFORMATION_OUTAGE\x10\x02\x12\x1b\n\x17PRIORITY_STATION_NOTICE\x10\x03\x12\x1b\n\x17PRIORITY_SPECIAL_NOTICE\x10\x04\x12\x1d\n\x19PRIORITY_WEEKDAY_SCHEDULE\x10\x05\x12\x1d\n\x19PRIORITY_WEEKEND_SCHEDULE\x10\x06\x12\x1e\n\x1aPRIORITY_SATURDAY_SCHEDULE\x10\x07\x12\x1c\n\x18PRIORITY_SUNDAY_SCHEDULE\x10\x08\x12\x1a\n\x16PRIORITY_EXTRA_SERVICE\x10\t\x12\x1c\n\x18PRIORITY_BOARDING_CHANGE\x10\n\x12\x1d\n\x19PRIORITY_SPECIAL_SCHEDULE\x10\x0b\x12\x1a\n\x16PRIORITY_EXPECT_DELAYS\x10\x0c\x12\x1c\n\x18PRIORITY_REDUCED_SERVICE\x10\r\x12%\n!PRIORITY_PLANNED_EXPRESS_TO_LOCAL\x10\x0e\x12#\n\x1fPRIORITY_PLANNED_EXTRA_TRANSFER\x10\x0f\x12"\n\x1ePRIORITY_PLANNED_STOPS_SKIPPED\x10\x10\x12\x1b\n\x17PRIORITY_PLANNED_DETOUR\x10\x11\x12\x1c\n\x18PRIORITY_PLANNED_REROUTE\x10\x12\x12%\n!PRIORITY_PLANNED_SUBSTITUTE_BUSES\x10\x13\x12#\n\x1fPRIORITY_PLANNED_PART_SUSPENDED\x10\x14\x12\x1e\n\x1aPRIORITY_PLANNED_SUSPENDED\x10\x15\x12\x1b\n\x17PRIORITY_SERVICE_CHANGE\x10\x16\x12\x19\n\x15PRIORITY_PLANNED_WORK\x10\x17\x12\x18\n\x14PRIORITY_SOME_DELAYS\x10\x18\x12\x1d\n\x19PRIORITY_EXPRESS_TO_LOCAL\x10\x19\x12\x13\n\x0fPRIORITY_DELAYS\x10\x1a\x12\x1a\n\x16PRIORITY_CANCELLATIONS\x10\x1b\x12%\n!PRIORITY_DELAYS_AND_CANCELLATIONS\x10\x1c\x12\x1a\n\x16PRIORITY_STOPS_SKIPPED\x10\x1d\x12\x1a\n\x16PRIORITY_SEVERE_DELAYS\x10\x1e\x12\x13\n\x0fPRIORITY_DETOUR\x10\x1f\x12\x14\n\x10PRIORITY_REROUTE\x10 \x12\x1d\n\x19PRIORITY_SUBSTITUTE_BUSES\x10!\x12\x1b\n\x17PRIORITY_PART_SUSPENDED\x10"\x12\x16\n\x12PRIORITY_SUSPENDED\x10#:_\n\x13mercury_feed_header\x12\x1c.transit_realtime.FeedHeader\x18\xe9\x07 \x01(\x0b\x32#.transit_realtime.MercuryFeedHeader:O\n\rmercury_alert\x12\x17.transit_realtime.Alert\x18\xe9\x07 \x01(\x0b\x32\x1e.transit_realtime.MercuryAlert:k\n\x17mercury_entity_selector\x12 .transit_realtime.EntitySelector\x18\xe9\x07 \x01(\x0b\x32\'.transit_realtime.MercuryEntitySelectorB\x1d\n\x1b\x63om.google.transit.realtime',
    dependencies=[
        gtfs__realtime__pb2.DESCRIPTOR,
    ],
)


MERCURY_FEED_HEADER_FIELD_NUMBER = 1001
mercury_feed_header = _descriptor.FieldDescriptor(
    name="mercury_feed_header",
    full_name="transit_realtime.mercury_feed_header",
    index=0,
    number=1001,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
MERCURY_ALERT_FIELD_NUMBER = 1001
mercury_alert = _descriptor.FieldDescriptor(
    name="mercury_alert",
    full_name="transit_realtime.mercury_alert",
    index=1,
    number=1001,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
MERCURY_ENTITY_SELECTOR_FIELD_NUMBER = 1001
mercury_entity_selector = _descriptor.FieldDescriptor(
    name="mercury_entity_selector",
    full_name="transit_realtime.mercury_entity_selector",
    index=2,
    number=1001,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)

_MERCURYENTITYSELECTOR_PRIORITY = _descriptor.EnumDescriptor(
    name="Priority",
    full_name="transit_realtime.MercuryEntitySelector.Priority",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_NO_SCHEDULED_SERVICE",
            index=0,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_INFORMATION_OUTAGE",
            index=1,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_STATION_NOTICE",
            index=2,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SPECIAL_NOTICE",
            index=3,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_WEEKDAY_SCHEDULE",
            index=4,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_WEEKEND_SCHEDULE",
            index=5,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SATURDAY_SCHEDULE",
            index=6,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SUNDAY_SCHEDULE",
            index=7,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_EXTRA_SERVICE",
            index=8,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_BOARDING_CHANGE",
            index=9,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SPECIAL_SCHEDULE",
            index=10,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_EXPECT_DELAYS",
            index=11,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_REDUCED_SERVICE",
            index=12,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_EXPRESS_TO_LOCAL",
            index=13,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_EXTRA_TRANSFER",
            index=14,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_STOPS_SKIPPED",
            index=15,
            number=16,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_DETOUR",
            index=16,
            number=17,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_REROUTE",
            index=17,
            number=18,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_SUBSTITUTE_BUSES",
            index=18,
            number=19,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_PART_SUSPENDED",
            index=19,
            number=20,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_SUSPENDED",
            index=20,
            number=21,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SERVICE_CHANGE",
            index=21,
            number=22,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_WORK",
            index=22,
            number=23,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SOME_DELAYS",
            index=23,
            number=24,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_EXPRESS_TO_LOCAL",
            index=24,
            number=25,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_DELAYS",
            index=25,
            number=26,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_CANCELLATIONS",
            index=26,
            number=27,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_DELAYS_AND_CANCELLATIONS",
            index=27,
            number=28,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_STOPS_SKIPPED",
            index=28,
            number=29,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SEVERE_DELAYS",
            index=29,
            number=30,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_DETOUR",
            index=30,
            number=31,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_REROUTE",
            index=31,
            number=32,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SUBSTITUTE_BUSES",
            index=32,
            number=33,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PART_SUSPENDED",
            index=33,
            number=34,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SUSPENDED",
            index=34,
            number=35,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=812,
    serialized_end=1882,
)
_sym_db.RegisterEnumDescriptor(_MERCURYENTITYSELECTOR_PRIORITY)


_MERCURYFEEDHEADER = _descriptor.Descriptor(
    name="MercuryFeedHeader",
    full_name="transit_realtime.MercuryFeedHeader",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="mercury_version",
            full_name="transit_realtime.MercuryFeedHeader.mercury_version",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=70,
    serialized_end=114,
)


_MERCURYSTATIONALTERNATIVE = _descriptor.Descriptor(
    name="MercuryStationAlternative",
    full_name="transit_realtime.MercuryStationAlternative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="affected_entity",
            full_name="transit_realtime.MercuryStationAlternative.affected_entity",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=2,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="notes",
            full_name="transit_realtime.MercuryStationAlternative.notes",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=2,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=117,
    serialized_end=254,
)


_MERCURYALERT = _descriptor.Descriptor(
    name="MercuryAlert",
    full_name="transit_realtime.MercuryAlert",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="created_at",
            full_name="transit_realtime.MercuryAlert.created_at",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="updated_at",
            full_name="transit_realtime.MercuryAlert.updated_at",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="alert_type",
            full_name="transit_realtime.MercuryAlert.alert_type",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="station_alternative",
            full_name="transit_realtime.MercuryAlert.station_alternative",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="service_plan_number",
            full_name="transit_realtime.MercuryAlert.service_plan_number",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="general_order_number",
            full_name="transit_realtime.MercuryAlert.general_order_number",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="display_before_active",
            full_name="transit_realtime.MercuryAlert.display_before_active",
            index=6,
            number=7,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="human_readable_active_period",
            full_name="transit_realtime.MercuryAlert.human_readable_active_period",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="directionality",
            full_name="transit_realtime.MercuryAlert.directionality",
            index=8,
            number=9,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="affected_stations",
            full_name="transit_realtime.MercuryAlert.affected_stations",
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="screens_summary",
            full_name="transit_realtime.MercuryAlert.screens_summary",
            index=10,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="no_affected_stations",
            full_name="transit_realtime.MercuryAlert.no_affected_stations",
            index=11,
            number=12,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="clone_id",
            full_name="transit_realtime.MercuryAlert.clone_id",
            index=12,
            number=13,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=257,
    serialized_end=763,
)


_MERCURYENTITYSELECTOR = _descriptor.Descriptor(
    name="MercuryEntitySelector",
    full_name="transit_realtime.MercuryEntitySelector",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="sort_order",
            full_name="transit_realtime.MercuryEntitySelector.sort_order",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _MERCURYENTITYSELECTOR_PRIORITY,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=766,
    serialized_end=1882,
)

_MERCURYSTATIONALTERNATIVE.fields_by_name["affected_entity"].message_type = gtfs__realtime__pb2._ENTITYSELECTOR
_MERCURYSTATIONALTERNATIVE.fields_by_name["notes"].message_type = gtfs__realtime__pb2._TRANSLATEDSTRING
_MERCURYALERT.fields_by_name["station_alternative"].message_type = _MERCURYSTATIONALTERNATIVE
_MERCURYALERT.fields_by_name["human_readable_active_period"].message_type = gtfs__realtime__pb2._TRANSLATEDSTRING
_MERCURYALERT.fields_by_name["affected_stations"].message_type = gtfs__realtime__pb2._ENTITYSELECTOR
_MERCURYALERT.fields_by_name["screens_summary"].message_type = gtfs__realtime__pb2._TRANSLATEDSTRING
_MERCURYENTITYSELECTOR_PRIORITY.containing_type = _MERCURYENTITYSELECTOR
DESCRIPTOR.message_types_by_name["MercuryFeedHeader"] = _MERCURYFEEDHEADER
DESCRIPTOR.message_types_by_name["MercuryStationAlternative"] = _MERCURYSTATIONALTERNATIVE
DESCRIPTOR.message_types_by_name["MercuryAlert"] = _MERCURYALERT
DESCRIPTOR.message_types_by_name["MercuryEntitySelector"] = _MERCURYENTITYSELECTOR
DESCRIPTOR.extensions_by_name["mercury_feed_header"] = mercury_feed_header
DESCRIPTOR.extensions_by_name["mercury_alert"] = mercury_alert
DESCRIPTOR.extensions_by_name["mercury_entity_selector"] = mercury_entity_selector
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MercuryFeedHeader = _reflection.GeneratedProtocolMessageType(
    "MercuryFeedHeader",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERCURYFEEDHEADER,
        "__module__": "mercury_gtfs_realtime_pb2",
        # @@protoc_insertion_point(class_scope:transit_realtime.MercuryFeedHeader)
    },
)
_sym_db.RegisterMessage(MercuryFeedHeader)

MercuryStationAlternative = _reflection.GeneratedProtocolMessageType(
    "MercuryStationAlternative",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERCURYSTATIONALTERNATIVE,
        "__module__": "mercury_gtfs_realtime_pb2",
        # @@protoc_insertion_point(class_scope:transit_realtime.MercuryStationAlternative)
    },
)
_sym_db.RegisterMessage(MercuryStationAlternative)

MercuryAlert = _reflection.GeneratedProtocolMessageType(
    "MercuryAlert",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERCURYALERT,
        "__module__": "mercury_gtfs_realtime_pb2",
        # @@protoc_insertion_point(class_scope:transit_realtime.MercuryAlert)
    },
)
_sym_db.RegisterMessage(MercuryAlert)

MercuryEntitySelector = _reflection.GeneratedProtocolMessageType(
    "MercuryEntitySelector",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERCURYENTITYSELECTOR,
        "__module__": "mercury_gtfs_realtime_pb2",
        # @@protoc_insertion_point(class_scope:transit_realtime.MercuryEntitySelector)
    },
)
_sym_db.RegisterMessage(MercuryEntitySelector)

mercury_feed_header.message_type = _MERCURYFEEDHEADER
gtfs__realtime__pb2.FeedHeader.RegisterExtension(mercury_feed_header)
mercury_alert.message_type = _MERCURYALERT
gtfs__realtime__pb2.Alert.RegisterExtension(mercury_alert)
mercury_entity_selector.message_type = _MERCURYENTITYSELECTOR
gtfs__realtime__pb2.EntitySelector.RegisterExtension(mercury_entity_selector)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
