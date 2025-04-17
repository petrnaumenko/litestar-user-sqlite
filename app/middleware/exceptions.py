from advanced_alchemy.exceptions import NotFoundError
from litestar import Request, Response
from litestar.exceptions import ValidationException
from litestar.status_codes import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR


def validation_exception_handler(request: Request, exc: ValidationException) -> Response:
    return Response(
        content={
            "error": "validation error",
            "path": request.url.path,
            "detail": exc.detail,
            "status_code": HTTP_400_BAD_REQUEST,
        },
        status_code=HTTP_400_BAD_REQUEST,
    )


def internal_server_error_handler(request: Request, exc: Exception) -> Response:
    return Response(
        content={
            "error": "internal server error",
            "path": request.url.path,
            "detail": str(exc),
            "status_code": HTTP_500_INTERNAL_SERVER_ERROR,
        },
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )


def value_error_handler(request: Request, exc: ValueError) -> Response:
    return Response(
        content={
            "error": "value error",
            "path": request.url.path,
            "detail": str(exc),
            "status_code": HTTP_400_BAD_REQUEST,
        },
        status_code=HTTP_400_BAD_REQUEST,
    )


def not_found_error_handler(request: Request, exc: NotFoundError) -> Response:
    return Response(
        content={
            "error": "not found error",
            "path": request.url.path,
            "detail": str(exc),
            "status_code": HTTP_404_NOT_FOUND,
        },
        status_code=HTTP_404_NOT_FOUND,
    )


exception_handlers = {
        ValidationException: validation_exception_handler,
        HTTP_500_INTERNAL_SERVER_ERROR: internal_server_error_handler,
        ValueError: value_error_handler,
    }
