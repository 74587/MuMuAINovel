"""角色相关的Pydantic模型"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime


class CharacterBase(BaseModel):
    """角色基础模型"""
    name: str = Field(..., description="角色/组织姓名")
    age: Optional[str] = Field(None, description="年龄")
    gender: Optional[str] = Field(None, description="性别")
    is_organization: bool = Field(False, description="是否为组织")
    role_type: Optional[str] = Field(None, description="角色类型：protagonist/supporting/antagonist")
    personality: Optional[str] = Field(None, description="性格特点/组织特性")
    background: Optional[str] = Field(None, description="背景故事")
    appearance: Optional[str] = Field(None, description="外貌特征")
    relationships: Optional[str] = Field(None, description="人际关系(JSON)")
    organization_type: Optional[str] = Field(None, description="组织类型")
    organization_purpose: Optional[str] = Field(None, description="组织目的")
    organization_members: Optional[str] = Field(None, description="组织成员(JSON)")
    traits: Optional[str] = Field(None, description="特征标签(JSON)")


class CharacterUpdate(BaseModel):
    """更新角色的请求模型"""
    name: Optional[str] = None
    age: Optional[str] = None
    gender: Optional[str] = None
    is_organization: Optional[bool] = None
    role_type: Optional[str] = None
    personality: Optional[str] = None
    background: Optional[str] = None
    appearance: Optional[str] = None
    relationships: Optional[str] = None
    organization_type: Optional[str] = None
    organization_purpose: Optional[str] = None
    organization_members: Optional[str] = None
    traits: Optional[str] = None


class CharacterResponse(CharacterBase):
    """角色响应模型"""
    id: str
    project_id: str
    avatar_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class CharacterGenerateRequest(BaseModel):
    """AI生成角色的请求模型"""
    project_id: str = Field(..., description="项目ID")
    name: Optional[str] = Field(None, description="角色名称")
    role_type: Optional[str] = Field(None, description="角色类型")
    background: Optional[str] = Field(None, description="角色背景")
    requirements: Optional[str] = Field(None, description="特殊要求")
    provider: Optional[str] = Field(None, description="AI提供商")
    model: Optional[str] = Field(None, description="AI模型")


class CharacterListResponse(BaseModel):
    """角色列表响应模型"""
    total: int
    items: List[CharacterResponse]