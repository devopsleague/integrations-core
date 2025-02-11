# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from typing_extensions import Literal

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class Filters(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    id: Optional[tuple[int, ...]] = None
    source: Optional[tuple[str, ...]] = None
    type: Optional[
        tuple[Literal['success', 'error', 'warning', 'information', 'success audit', 'failure audit'], ...]
    ] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    auth_type: Optional[Literal['default', 'negotiate', 'kerberos', 'ntlm']] = None
    bookmark_frequency: Optional[int] = None
    disable_generic_tags: Optional[bool] = None
    domain: Optional[str] = None
    empty_default_hostname: Optional[bool] = None
    event_format: Optional[tuple[str, ...]] = None
    event_id: Optional[tuple[str, ...]] = None
    event_priority: Optional[Literal['normal', 'low']] = None
    excluded_messages: Optional[tuple[str, ...]] = None
    filters: Optional[Filters] = None
    host: Optional[str] = None
    included_messages: Optional[tuple[str, ...]] = None
    interpret_messages: Optional[bool] = None
    legacy_mode: Optional[bool] = None
    log_file: Optional[tuple[str, ...]] = None
    message_filters: Optional[tuple[str, ...]] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    password: Optional[str] = None
    path: Optional[str] = None
    payload_size: Optional[int] = None
    query: Optional[str] = None
    server: Optional[str] = None
    service: Optional[str] = None
    source_name: Optional[tuple[str, ...]] = None
    start: Optional[Literal['now', 'oldest']] = None
    tag_event_id: Optional[bool] = None
    tag_sid: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    timeout: Optional[float] = None
    type: Optional[tuple[str, ...]] = None
    user: Optional[str] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
