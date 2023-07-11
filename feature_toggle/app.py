from feature_toggle.models.dynamodb import Dynamodb, EntityType


def main() -> None:
    x = Dynamodb()
    print(x.model_dump_json(indent=2))
