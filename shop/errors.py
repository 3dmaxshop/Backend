from telnetlib import STATUS


class AppError (Exception):
    def __init__(self, reason:str, status: int) -> None:
        super().__init__(f'[{status}] {reason}')
        self.reason = reason
        self.status = status

class Conflict(AppError):

    status = 409

    def __init__(self, entity: str, info:str) -> None:
        super().__init__(reason=f'[{entity}] conflict {info}', status = self.status)
        self.entity = entity
        self.info = info

class NotFoundError(AppError):

    status = 404
    
    def __init__(self, entity: str, info:str) -> None:
        super().__init__(reason=f'[{entity}] conflict {info}', status = self.status)
        self.entity = entity
        self.info = info

class IndexNotFoundError(AppError):

    status = 404
    
    def __init__(self, info:str) -> None:
        super().__init__(reason=f'{info}', status = self.status)
        self.info = info

