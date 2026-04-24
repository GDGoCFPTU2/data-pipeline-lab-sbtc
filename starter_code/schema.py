from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    document_id: str = Field(..., description="Unique id of the input document")
    source_type: str = Field(..., description="Input source type, e.g. PDF or Video")
    author: str = Field(..., description="Author or creator of the source")
    category: str = Field(..., description="Business/content category")
    content: str = Field(..., description="Normalized textual content")
    timestamp: str = Field(..., description="Creation or publication timestamp")
