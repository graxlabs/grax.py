# coding: utf-8

"""
    GRAX API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from grax.models.search_filters import SearchFilters
from grax.models.search_limits import SearchLimits
from typing import Optional, Set
from typing_extensions import Self

class SearchCreate(BaseModel):
    """
    SearchCreate
    """ # noqa: E501
    filters: Optional[SearchFilters] = None
    limits: Optional[SearchLimits] = None
    notify: Optional[StrictBool] = Field(default=None, description="Whether to notify when the search is complete.")
    object: Optional[StrictStr] = Field(default=None, description="Object to search.")
    reverse: Optional[StrictBool] = Field(default=None, description="Whether to search in reverse order.")
    status: Optional[StrictStr] = Field(default=None, description="Status of the records to search. Can be 'deleted', 'archived', 'archivedDeleted' or 'live'. Defaults to 'all'.")
    status_at: Optional[StrictStr] = Field(default=None, description="Consider Status at record modified if 'modified' or latest within range if 'range'. Defaults to consider at latest.", alias="statusAt")
    status_at_modified: Optional[StrictBool] = Field(default=None, description="Unused.", alias="statusAtModified")
    time_field: Optional[StrictStr] = Field(default=None, description="Time field to search. Can be 'createdAt', 'modifiedAt', 'latestModifiedAt', 'rangeLatestModifiedAt', 'allModifiedAt', 'deletedAt' or 'purgedAt'. Defaults to 'createdAt'.", alias="timeField")
    time_field_max: Optional[datetime] = Field(default=None, description="Maximum time for the search.", alias="timeFieldMax")
    time_field_min: Optional[datetime] = Field(default=None, description="Minimum time for the search.", alias="timeFieldMin")
    __properties: ClassVar[List[str]] = ["filters", "limits", "notify", "object", "reverse", "status", "statusAt", "statusAtModified", "timeField", "timeFieldMax", "timeFieldMin"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SearchCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filters": SearchFilters.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "limits": SearchLimits.from_dict(obj["limits"]) if obj.get("limits") is not None else None,
            "notify": obj.get("notify"),
            "object": obj.get("object"),
            "reverse": obj.get("reverse"),
            "status": obj.get("status"),
            "statusAt": obj.get("statusAt"),
            "statusAtModified": obj.get("statusAtModified"),
            "timeField": obj.get("timeField"),
            "timeFieldMax": obj.get("timeFieldMax"),
            "timeFieldMin": obj.get("timeFieldMin")
        })
        return _obj


