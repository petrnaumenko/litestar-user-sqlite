import hashlib
import re

import msgspec
from advanced_alchemy.extensions.litestar import repository, service
from litestar import status_codes
from litestar.exceptions import HTTPException

from app.models.user import UserModel
from app.schemas.user import UserCreate


class UserService(service.SQLAlchemyAsyncRepositoryService[UserModel]):
    class Repo(repository.SQLAlchemyAsyncRepository[UserModel]):
        model_type = UserModel

    repository_type = Repo

    @staticmethod
    def validate_password(password: str) -> None:
        if (
            len(password) < 8
            or not re.search(r"[A-Z]", password)
            or not re.search(r"[a-z]", password)
            or not re.search(r"\d", password)
        ):
            raise HTTPException(status_code=status_codes.HTTP_400_BAD_REQUEST, detail="Password must be at least 8 characters long and include upper case letters, lower case letters, and digits.")

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    async def create(self, data: UserCreate) -> UserModel:
        self.validate_password(data.password)
        data_dict = msgspec.to_builtins(data)
        data_dict["password"] = self.hash_password(data.password)
        return await super().create(UserModel(**data_dict))
