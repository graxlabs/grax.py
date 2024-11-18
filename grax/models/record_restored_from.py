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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from grax.models.audit_user import AuditUser
from typing import Optional, Set
from typing_extensions import Self

class RecordRestoredFrom(BaseModel):
    """
    RecordRestoredFrom
    """ # noqa: E501
    activity_id: Optional[StrictStr] = Field(default=None, description="Activity ID that restored the record.", alias="activityID")
    added: Optional[datetime] = Field(default=None, description="Added time of the new record.")
    id: Optional[StrictStr] = Field(default=None, description="Original record ID.")
    modified: Optional[datetime] = Field(default=None, description="Modified time of the original record.")
    user: Optional[AuditUser] = None
    __properties: ClassVar[List[str]] = ["activityID", "added", "id", "modified", "user"]

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
        """Create an instance of RecordRestoredFrom from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecordRestoredFrom from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activityID": obj.get("activityID"),
            "added": obj.get("added"),
            "id": obj.get("id"),
            "modified": obj.get("modified"),
            "user": AuditUser.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


