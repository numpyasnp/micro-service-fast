# base model kullaniliyor modeller için.


"""
Klasik SQLAlchemy Kullanın Eğer:

    Çok tablolu karmaşık JOIN'ler yapıyorsanız

    Window fonksiyonları veya analitik sorgular gerekiyorsa

    Veritabanı-spesifik özellikler (JSONB, GIS, full-text search) kullanacaksanız

    İleri seviye transaction yönetimi gerekiyorsa

    Bulk operasyonlarda yüksek performans gerekiyorsa

SQLModel Kullanın Eğer:

    CRUD operasyonları ağırlıklı çalışıyorsanız

    Hızlı prototipleme yapıyorsanız

    API ile DB modeli senkronizasyonu önemliyse

    Basit ilişkiler yeterliyse

    Tip güvenliği ve kod tamamlama öncelikliyse
"""
from typing import Optional

from sqlmodel import SQLModel, Field


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: Optional[int] = Field(default=None, index=True)
    secret_name: str
    user_id: int = Field(index=True)
