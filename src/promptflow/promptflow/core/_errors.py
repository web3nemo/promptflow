# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from promptflow.exceptions import ErrorTarget, SystemErrorException, UserErrorException


class CoreError(UserErrorException):
    """Core base class, target default is CORE."""

    def __init__(
        self,
        message="",
        message_format="",
        target: ErrorTarget = ErrorTarget.CORE,
        module=None,
        **kwargs,
    ):
        super().__init__(message=message, message_format=message_format, target=target, module=module, **kwargs)


class CoreInternalError(SystemErrorException):
    """Core internal error."""

    def __init__(
        self,
        message="",
        message_format="",
        target: ErrorTarget = ErrorTarget.CORE,
        module=None,
        **kwargs,
    ):
        super().__init__(message=message, message_format=message_format, target=target, module=module, **kwargs)


class GenerateFlowMetaJsonError(CoreError):
    """Exception raised if flow json generation failed."""

    pass


class RequiredEnvironmentVariablesNotSetError(CoreError):
    """Exception raised if connection from_env required env vars not found."""

    def __init__(self, env_vars: list, cls_name: str):
        super().__init__(f"Required environment variables {env_vars} to build {cls_name} not set.")


class OpenURLFailed(SystemErrorException):
    def __init__(self, **kwargs):
        super().__init__(target=ErrorTarget.CORE, **kwargs)


class BuildConnectionError(SystemErrorException):
    def __init__(self, **kwargs):
        super().__init__(target=ErrorTarget.CORE, **kwargs)


class MissingRequiredPackage(UserErrorException):
    def __init__(self, **kwargs):
        super().__init__(target=ErrorTarget.CORE, **kwargs)


class UserAuthenticationError(UserErrorException):
    """Exception raised when user authentication failed"""

    pass


class OpenURLUserAuthenticationError(UserAuthenticationError):
    def __init__(self, **kwargs):
        super().__init__(target=ErrorTarget.CORE, **kwargs)


class OpenURLFailedUserError(UserErrorException):
    def __init__(self, **kwargs):
        super().__init__(target=ErrorTarget.CORE, **kwargs)


class UnknownConnectionType(UserErrorException):
    def __init__(self, **kwargs):
        super().__init__(target=ErrorTarget.CORE, **kwargs)


class UnsupportedConnectionAuthType(UserErrorException):
    def __init__(self, **kwargs):
        super().__init__(target=ErrorTarget.CORE, **kwargs)


class AccessDeniedError(UserErrorException):
    """Exception raised when run info can not be found in storage"""

    def __init__(self, operation: str, target: ErrorTarget):
        super().__init__(message=f"Access is denied to perform operation {operation!r}", target=target)
