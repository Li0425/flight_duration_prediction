from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


class FlightDataRequestSchema(Schema):
    Distance = fields.Integer()
    DistanceGroup = fields.Integer()
    Num_Arr_SIBTp10 = fields.Integer()
    Num_Arr_SIBTp15 = fields.Integer()
    Num_Arr_SIBTp20 = fields.Integer()
    Num_Arr_SIBTp25 = fields.Integer()
    Num_Arr_SIBTp5 = fields.Integer()
    Num_Arr_SIBTm0 = fields.Integer()
    Num_Arr_SIBTm10 = fields.Integer()
    Num_Arr_SIBTm15 = fields.Integer()
    Num_Arr_SIBTm20 = fields.Integer()
    Num_Arr_SIBTm25 = fields.Integer()
    Num_Arr_SIBTm30 = fields.Integer()
    Num_Arr_SIBTm5 = fields.Integer()
    Num_Dep_SIBTp10 = fields.Integer()
    Num_Dep_SIBTp15 = fields.Integer()
    Num_Dep_SIBTp20 = fields.Integer()
    Num_Dep_SIBTp25 = fields.Integer()
    Num_Dep_SIBTp5 = fields.Integer()
    Num_Dep_SIBTm0 = fields.Integer()
    Num_Dep_SIBTm10 = fields.Integer()
    Num_Dep_SIBTm15 = fields.Integer()
    Num_Dep_SIBTm20 = fields.Integer()
    Num_Dep_SIBTm25 = fields.Integer()
    Num_Dep_SIBTm30 = fields.Integer()
    Num_Dep_SIBTm5 = fields.Integer()
    OBTDel15 = fields.Integer()
    OBTDelay = fields.Integer()
    OBTDelayGroups = fields.Integer()
    OriginAirportID = fields.Integer()
    OriginCityMarketID = fields.Integer()
    OriginState = fields.Str()
    SIBTDayOfMonth = fields.Integer()
    SIBTDayOfWeek = fields.Integer()
    SIBTHour = fields.Integer()
    SIBTMonth = fields.Integer()
    SIBTQuarter = fields.Integer()
    SOBTtoSIBT = fields.Integer()
    UniqueCarrierCode = fields.Str()


def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = FlightDataRequestSchema(strict=True, many=True)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
