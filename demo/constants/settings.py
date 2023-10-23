from pydantic import SecretStr
from pydantic_settings import BaseSettings

from demo.constants.paths import ROOT_FOLDER


class Settings(BaseSettings):
    """Settings for the demo app.

    Reads from demo/.env file or environment variables.
    You can create the .env file from the .env_example file.

    !!! SecretStr is a pydantic type that hides the value in logs.
    If you want to use the real value, you should do:
    SETTINGS.<variable>.get_secret_value()
    """

    class Config:
        env_file = ROOT_FOLDER / "demo" / ".env"

    openai_model: str = "gpt-3.5-turbo" # if you have access to GPT4, you can use "gpt-4"
    openai_api_key: SecretStr
    aws_region: str = "us-east-1"
    bedrock_model_id: str = "anthropic.claude-v2" # change to any of the models here: https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids-arns.html
    temperature: float = 0

SETTINGS = Settings()  # type: ignore
