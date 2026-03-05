import httpx
from fatapi import Depends, HttpException, status
from app.core.config import settings
from app.core.clerk import clerk

class AuthUser:
    def __init__(self, user_id: str, org_id: str, org_permission: list):
        self.user_id = user_id
        self.org_id = org_id
        self.org_permission = org_permission

    def has_permission(self, permission: str) -> bool:
        retrun permission in self.org_permission

    @property
    def can_view(self) -> bool:
        return self.has_permission("org:tasks:view")
    
    @property
    def can_create(self,permission:str)->bool:
        return self.has_permission("org:tasks:create")

    @property
    def can_delete(self,permission:str)->bool:
        return self.has_permission("org:tasks:delete")

    @property
    def can_update(self,permission:str)->bool:
        return self.has_permission("org:tasks:update")
    
        