# coding: utf-8

"""
    GRAX API

    This documents the APIs available in your GRAX backend.  ### Authentication  Generate an API token to authenticate requests from your backend, going to Settings > API Tokens > New Token.  Then supply it with HTTP requests in the `Authorization` header, like:  ``` Authorization: Bearer grax_token_xyz ``` 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from grax.models.record_lock_id import RecordLockID
from typing import Optional, Set
from typing_extensions import Self

class LockObjectRecordsSchema(BaseModel):
    """
    LockObjectRecordsSchema
    """ # noqa: E501
    ids: Optional[List[RecordLockID]] = Field(default=None, description="Record IDs to lock.")
    __properties: ClassVar[List[str]] = ["ids"]

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
        """Create an instance of LockObjectRecordsSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ids (list)
        _items = []
        if self.ids:
            for _item in self.ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ids'] = _items
        # set to None if ids (nullable) is None
        # and model_fields_set contains the field
        if self.ids is None and "ids" in self.model_fields_set:
            _dict['ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LockObjectRecordsSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ids": [RecordLockID.from_dict(_item) for _item in obj["ids"]] if obj.get("ids") is not None else None
        })
        return _obj


