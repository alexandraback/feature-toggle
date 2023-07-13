import boto3
from boto3.dynamodb.table import TableResource

from feature_toggle.models.feature import Feature


def to_dynamodb(table: TableResource, item: Feature) -> dict:
    payload = {
        "Item": item.to_item(),
        "ConditionExpression": f"attribute_not_exists(PK) AND attribute_not_exists(SK)",
    }

    resp = table.put_item(**payload)
    return resp
