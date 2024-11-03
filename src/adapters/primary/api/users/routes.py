from fastapi import APIRouter, Depends, Response

from src.adapters.primary.api.users.dependencies import (
    check_user_already_authenticated,
    get_user_id,
    get_user_service,
)
from src.adapters.primary.api.users.schemas import UserSchema
from src.adapters.settings import auth_settings
from src.application.user.services import UserService

router = APIRouter()


@router.post(
    "/register",
    response_model=dict[str, str],
    summary="Регистрация пользователя",
    dependencies=[Depends(check_user_already_authenticated)]
)
async def register_user(
    username: str,
    password: str,
    user_service: UserService = Depends(get_user_service)
) -> dict[str, str]:
    user = await user_service.register_user(
        username=username,
        password=password
    )

    if user:
        return {"message": "Пользователь успешно зарегистрирован."}


@router.post(
    "/login",
    response_model=dict[str, str],
    summary="Авторизация пользователя",
    dependencies=[Depends(check_user_already_authenticated)]
)
async def login_user(
    username: str,
    password: str,
    response: Response,
    user_service: UserService = Depends(get_user_service)
) -> dict[str, str]:
    token = await user_service.login_user(
        username=username,
        password=password,
    )

    response.set_cookie(
        key=auth_settings.JWT_COOKIE_NAME,
        value=token,
        httponly=True,
        expires=auth_settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    return {"token": token}


@router.get(
    "/profile",
    response_model=UserSchema,
    summary="Получение профиля пользователя"
)
async def get_user_profile(
    user_service: UserService = Depends(get_user_service),
    user_id: int = Depends(get_user_id)
) -> UserSchema:
    return await user_service.get_user_profile(user_id=user_id)
