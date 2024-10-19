from sqlalchemy.orm import Session
from app import models, schemas


def create_invoice(db: Session, invoice: schemas.invoice.InvoiceCreate):
    db_invoice = models.invoice.Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def get_invoices(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.invoice.Invoice).offset(skip).limit(limit).all()
