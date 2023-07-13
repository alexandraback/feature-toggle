from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, field_serializer


class EntityType(str, Enum):
    FEAT = "feat"


class Feature(BaseModel):
    entity_type: EntityType = EntityType.FEAT
    insert_time: datetime | None = datetime.now(tz=timezone.utc)
    modified_time: datetime | None = None
    app_name: str
    feat_name: str
    enabled: bool

    @field_serializer("entity_type")
    def serialize_enum(self, enum: Enum):
        if enum is not None:
            return enum.value

    @field_serializer("insert_time", "modified_time")
    def serialize_dt(self, dt: datetime):
        if dt is None:
            return
        return dt.isoformat()

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
