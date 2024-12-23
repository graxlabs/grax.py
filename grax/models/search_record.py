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
from grax.models.record_deleted import RecordDeleted
from grax.models.record_field import RecordField
from grax.models.record_purged import RecordPurged
from grax.models.record_restored_from import RecordRestoredFrom
from typing import Optional, Set
from typing_extensions import Self

class SearchRecord(BaseModel):
    """
    SearchRecord
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="Time the record was created.")
    deleted: Optional[RecordDeleted] = None
    fields: Optional[List[RecordField]] = Field(default=None, description="Record fields.")
    id: Optional[StrictStr] = Field(default=None, description="Record ID.")
    modified: Optional[datetime] = Field(default=None, description="Time the record was modified.")
    name: Optional[StrictStr] = Field(default=None, description="Record name.")
    purged: Optional[RecordPurged] = None
    restored_from: Optional[RecordRestoredFrom] = Field(default=None, alias="restoredFrom")
    salesforce_url: Optional[StrictStr] = Field(default=None, description="Salesforce URL for the record.", alias="salesforceURL")
    __properties: ClassVar[List[str]] = ["created", "deleted", "fields", "id", "modified", "name", "purged", "restoredFrom", "salesforceURL"]

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
        """Create an instance of SearchRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of purged
        if self.purged:
            _dict['purged'] = self.purged.to_dict()
        # override the default output from pydantic by calling `to_dict()` of restored_from
        if self.restored_from:
            _dict['restoredFrom'] = self.restored_from.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "deleted": RecordDeleted.from_dict(obj["deleted"]) if obj.get("deleted") is not None else None,
            "fields": [RecordField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "id": obj.get("id"),
            "modified": obj.get("modified"),
            "name": obj.get("name"),
            "purged": RecordPurged.from_dict(obj["purged"]) if obj.get("purged") is not None else None,
            "restoredFrom": RecordRestoredFrom.from_dict(obj["restoredFrom"]) if obj.get("restoredFrom") is not None else None,
            "salesforceURL": obj.get("salesforceURL")
        })
        return _obj


