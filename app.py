from flask import Flask, render_template, request
from db import Tur, session
from sqlmodel import select


app = Flask(__name__)




def add_data(title, price, description):
    tour = Tur(title=title, price=price, description=description)
    session.add(tour)
    session.commit()


@app.get("/")
def index():
    tours = session.scalars(select(Tur)).all()
    print(tours)
    return render_template("index.html", tours=tours)


@app.get("/tour/details")
def tour_details():
    id = int(request.args.get("tour_id"))
    tour = session.get_one(Tur, id)
    tour = tour.model_dump()
    return render_template("tour.html", tour=tour)

if __name__ == "__main__":
    add_data(title="kiev to frncae", price=99, description="tour from kiev to france")
    app.run(debug=True)