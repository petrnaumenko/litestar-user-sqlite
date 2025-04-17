from typing import Annotated

from advanced_alchemy.extensions.litestar import (
    filters,
    providers,
    service,
)
from litestar import Controller, delete, get, patch, post
from litestar.params import Dependency, Parameter

from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user import UserService


class UserController(Controller):
    dependencies = providers.create_service_dependencies(
        UserService,
        "users_service",
        filters={"pagination_type": "limit_offset", "id_filter": int, "search": "name", "search_ignore_case": True},
    )

    @get(path="/users")
    async def list_users(
        self,
        users_service: UserService,
        filters: Annotated[list[filters.FilterTypes], Dependency(skip_validation=True)],
    ) -> service.OffsetPagination[User]:
        results, total = await users_service.list_and_count(*filters)
        return users_service.to_schema(results, total, filters=filters, schema_type=User)

    @post(path="/users")
    async def create_user(self, users_service: UserService, data: UserCreate) -> User:
        obj = await users_service.create(data)
        return users_service.to_schema(obj, schema_type=User)

    @get(path="/users/{user_id:int}")
    async def get_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(title="User ID"),
    ) -> User:
        obj = await users_service.get(user_id)
        return users_service.to_schema(obj, schema_type=User)

    @patch(path="/users/{user_id:int}")
    async def update_user(
        self,
        users_service: UserService,
        data: UserUpdate,
        user_id: int = Parameter(title="User ID"),
    ) -> User:
        obj = await users_service.update(data, item_id=user_id)
        return users_service.to_schema(obj, schema_type=User)

    @delete(path="/users/{user_id:int}")
    async def delete_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(title="User ID"),
    ) -> None:
       await users_service.delete(user_id)
