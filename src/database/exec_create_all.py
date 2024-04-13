from src.database.base import Base
from src.database.engine import engine

from src.models.payment_model import PaymentModel

table_objects = [PaymentModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )