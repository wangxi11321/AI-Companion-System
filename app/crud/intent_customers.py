from sqlalchemy.orm import Session
from app.models.intent_customers import IntentCustomer
from app.schemas.section_intent_customers import IntentCustomerCreate
from typing import Optional

def create_intent_customer(db: Session, customer: IntentCustomerCreate) -> IntentCustomer:
    db_customer = IntentCustomer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_intent_customer(db: Session, customer_id: int) -> Optional[IntentCustomer]:
    return db.query(IntentCustomer).filter(IntentCustomer.id == customer_id).first()