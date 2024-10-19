from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.post("/", response_model=schemas.invoice.Invoice)
def create_invoice(
    invoice: schemas.invoice.InvoiceCreate, db: Session = Depends(get_db)
):
    return crud.invoice.create_invoice(db=db, invoice=invoice)


@router.get("/", response_model=list[schemas.invoice.Invoice])
def read_invoices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    invoices = crud.invoice.get_invoices(db, skip=skip, limit=limit)
    return invoices
