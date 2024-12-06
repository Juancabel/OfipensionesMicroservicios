import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://monitoring_user:isis2503@10.128.0.70:27017"
)
db = client.get_database("monitoring_db")
informe_collection = db.get_collection("informes")


async def set_informes_db():
    # Creates a unique index on the code field
    await informe_collection.create_index("code", unique=True)


# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]