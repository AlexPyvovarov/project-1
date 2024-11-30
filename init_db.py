from config import restart_db, session
from db import Tur, SQLModel
from app import app


with app.app_context():
    restart_db()
    tur1 = Tur(title="kiev to odesa", 
               price=9.5, 
               description="a ride from kiev to odesa", 
               is_booked=True)
    tur2 = Tur(title="kiev to lviv", 
               price=13.5, 
               description="a ride from kiev to lviv", 
               is_booked=False)
    tur3 = Tur(title="kiev to moldova", 
               price=15.5, 
               description="a ride from kiev to molodova", 
               is_booked=True)
    session.add_all([tur1, tur2, tur3])
    session.commit()