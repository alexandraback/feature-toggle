from enum import Enum

from pydantic import BaseModel


class EntityType(str, Enum):
    feat = "feat"


class Dynamodb(BaseModel):
    entity_type: EntityType = EntityType.feat
