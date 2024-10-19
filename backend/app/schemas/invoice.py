from pydantic import BaseModel


class InvoiceBase(BaseModel):
    amount: float
    description: str


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
