from . import app, db
from .models import Owner, Car, Cover
from .forms import CarForm, OwnerForm, CoverForm
from flask import redirect, url_for, request, render_template

@app.route("/main")
def home():
    tasks = Car.query.all()
    covs = Cover.query.all()

    return render_template("home.html", tasks=tasks, covs=covs)

@app.route("/create", methods=["GET", "POST"])
def create():
    form = CarForm()

    if request.method == "POST":
        new_task = Car(
            description=form.description.data,
            owner_id=form.owner.data
            )
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        owners = Owner.query.all()
        form.owner.choices = [(owner.id, owner.name) for owner in owners]

        return render_template("create_car.html", form=form)

@app.route("/create_owner", methods=["GET", "POST"])
def create_owner():
    form = OwnerForm()

    if request.method == "POST":
        new_owner = Owner(name=form.name.data)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        return render_template("create_owner.html", form=form)

@app.route("/update/<int:id>/", methods=["GET", "POST"])
def update(id):
    task = Car.query.get(id)
    form = CarForm()

    if request.method == "POST":
        task.description = form.description.data
        task.owner_id = form.owner.data
        db.session.add(task)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        owners = Owner.query.all()
        form.owner.choices = [(owner.id, owner.name) for owner in owners]

        form.description.data = task.description

        return render_template("create_car.html", form=form)

@app.route("/delete/<int:id>")
def delete(id):
    task = Car.query.get(id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/complete/<int:id>")
def complete(id):
    task = Car.query.get(id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Car.query.get(id)
    task.completed = False
    db.session.add(task)
    db.session.commit()

    return redirect(url_for("home"))


# @app.route('/', methods=['GET', 'POST'])
# @app.route('/home', methods=['GET', 'POST'])
# def register():
#     error = ""
#     form = BasicForm()

#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data

#         if len(first_name) == 0 or len(last_name) == 0:
#             error = "Please supply both first and last name"
#         else:
#             return 'thank_you'

#     return render_template('extra.html', form=form, message=error)

@app.route("/create_cover", methods=["GET", "POST"])
def create_cover():
    form = CoverForm()

    if request.method == "POST":
        new_task = Cover(
            first_name=form.first_name.data,
            last_name=form.last_name.data
            )
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        owners = Owner.query.all()
        form.owner.choices = [(owner.id, owner.name) for owner in owners]

        return render_template("create_cover.html", form=form)