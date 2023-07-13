from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, ConfigDict, field_serializer, field_validator, validator


class EntityType(str, Enum):
    FEAT = "feat"


class Feature(BaseModel):
    entity_type: EntityType = EntityType.FEAT
    insert_time: datetime | None = None
    modified_time: datetime | None = None
    app_name: str
    feat_name: str
    enabled: bool
    model_config: ConfigDict(
        use_enum_values=True,
    )

    @field_serializer("insert_time", "modified_time")
    def serialize_dt(self, dt: datetime):
        if dt is None:
            return
        return dt.isoformat()

    # @field_validator("insert_time", mode="after", check_fields=False)
    @validator("insert_time", always=True)
    def add_default_timestamp(cls, v):
        if v is not None:
            return v

        return datetime.now(tz=timezone.utc)

    @property
    def pk(self):
        return f"APP#{self.app_name}"

    @property
    def sk(self):
        return f"FEAT#{self.feat_name}"

    @property
    def keys(self):
        return {"PK": self.pk, "SK": self.sk}

    def to_item(self):
        payload = {
            **self.keys,
            **self.model_dump(),
        }
        return payload
