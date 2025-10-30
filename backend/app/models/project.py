"""项目数据模型"""
from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.sql import func
from app.database import Base
import uuid


class Project(Base):
    """项目表"""
    __tablename__ = "projects"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(200), nullable=False, comment="项目标题")
    description = Column(Text, comment="项目简介")
    theme = Column(Text, comment="主题")
    genre = Column(String(50), comment="小说类型")
    target_words = Column(Integer, default=0, comment="目标字数")
    current_words = Column(Integer, default=0, comment="当前字数")
    status = Column(String(20), default="planning", comment="创作状态")
    wizard_status = Column(String(20), default="incomplete", comment="向导完成状态: incomplete/completed")
    wizard_step = Column(Integer, default=0, comment="向导当前步骤: 0-4")
    
    # 世界构建字段
    world_time_period = Column(Text, comment="时间背景")
    world_location = Column(Text, comment="地理位置")
    world_atmosphere = Column(Text, comment="氛围基调")
    world_rules = Column(Text, comment="世界规则")
    
    # 项目配置
    chapter_count = Column(Integer, comment="章节数量")
    narrative_perspective = Column(String(50), comment="叙事视角：first_person/third_person/omniscient")
    character_count = Column(Integer, default=5, comment="角色数量")
    
    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    
    def __repr__(self):
        return f"<Project(id={self.id}, title={self.title})>"