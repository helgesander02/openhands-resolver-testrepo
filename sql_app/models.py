from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table,DateTime,Date
from sqlalchemy.orm import relationship,session,Mapped,mapped_column
import datetime as dt
from .database import Base


class Order(Base):
    __tablename__ = "order"
    od_id=Column(Integer, primary_key=True,autoincrement=True)
    order_number=Column(Integer)
    M_ID=Column(ForeignKey("member.ID"))
    p_ID=Column(ForeignKey("product.prodcut_ID",ondelete='CASCADE'))
    M_ID_=relationship('member', back_populates='orders')
    p_ID_=relationship('product', back_populates='orders')
    Date_=Column(Date, default=dt.datetime.today())
    pick_up=Column(String)
    pick_up_tf=Column(String)
    count=Column(Integer)
    Remark=Column(String)
    pick_up_date=Column(Date)
    money=Column(Integer)
    path=Column(String)
    discount=Column(Integer,default=None)
    total=Column(Integer,default=0)
class member(Base):
    __tablename__ = "member" # table name in the database

    ID = Column(Integer, primary_key=True, index=True,autoincrement=True)
    Name = Column(String)
    Address = Column(String)
    Remark = Column(String, default=True)
    Phone=Column(String)
    orders = relationship('Order', back_populates='M_ID_')

    # items = relationship("Item", back_populates="owner")
class product(Base):
    __tablename__ = "product" # table name in the database

    prodcut_ID = Column(Integer, primary_key=True, index=True,autoincrement=True)
    product_Name = Column(String)
    product_Weight = Column(String)
    product_Price = Column(Integer, default=True)
    orders = relationship('Order', back_populates='p_ID_', cascade="all, delete-orphan")
    content=Column(String)
    # orders = relationship('Order', secondary=association_table, back_populates='p_ID_',overlaps="M_ID")
class receipt(Base):
    __tablename__ = "receipt"

    rc_id=Column(Integer, primary_key=True, index=True,autoincrement=True)
    o_id=Column(Integer)
    m_id=Column(ForeignKey("member.ID"))
    date=Column(Date, default=dt.datetime.today())
    money=Column(Integer)
    remark=Column(String)
    m_way=Column(String)
    discount=Column(Integer)