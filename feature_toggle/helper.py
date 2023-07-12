import boto3
from boto3.dynamodb.table import TableResource

from feature_toggle.models.dynamodb import Dynamodb


def to_dynamodb(table: TableResource, item: Dynamodb) -> None:
    payload = {
        "Item": item.to_item(),
        "ConditionExpression": f"attribute_not_exists({item.pk}) AND attribute_not_exists({item.sk})",
    }
    # table.put_item(**payload)
    print(payload)
