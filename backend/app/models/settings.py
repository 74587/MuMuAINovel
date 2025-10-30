"""设置数据模型"""
from sqlalchemy import Column, String, Text, Float, Integer, DateTime, Index
from sqlalchemy.sql import func
from app.database import Base
import uuid


class Settings(Base):
    """设置表"""
    __tablename__ = "settings"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(50), nullable=False, unique=True, index=True, comment="用户ID")
    api_provider = Column(String(50), default="openai", comment="API提供商")
    api_key = Column(String(500), comment="API密钥")
    api_base_url = Column(String(500), comment="自定义API地址")
    model_name = Column(String(100), default="gpt-4", comment="模型名称")
    temperature = Column(Float, default=0.7, comment="温度参数")
    max_tokens = Column(Integer, default=2000, comment="最大token数")
    preferences = Column(Text, comment="其他偏好设置(JSON)")
    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    
    __table_args__ = (
        Index('idx_user_id', 'user_id'),
    )
    
    def __repr__(self):
        return f"<Settings(id={self.id}, user_id={self.user_id}, api_provider={self.api_provider})>"