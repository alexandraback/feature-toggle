from datetime import datetime

import boto3

from feature_toggle.helper import to_dynamodb
from feature_toggle.models.dynamodb import Dynamodb


def main() -> None:
    data = {
        "app_name": "polaris",
        "feat_name": "new-issue",
        "enabled": True,
        # "dummy": "Alex",
        "insert_time": datetime(2020, 5, 1, 12, 0, 0),
    }

    x = Dynamodb.model_validate(data)
    print(x)
    print(x.model_dump())
    print(x.model_dump_json(indent=2))

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("feature-toggle")

    y = to_dynamodb(table=table, item=x)
