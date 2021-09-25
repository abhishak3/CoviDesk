from app.models import AvailableBeds, NGOs
from flask import request, render_template, url_for, session, redirect
from flask_login import login_required

from . import main
from .forms import BedRegistrationForm
from .. import db

@main.route('/')
def index():
    if not session.get('name'):
        name = "Normal User"
    else:
        name = session.get('name')
    return render_template('index.html', name=name, beds=AvailableBeds.query.all()[::-1]), 200

@main.route('/bedreg', methods=['GET','POST'])
@login_required
def bedregister():
    form = BedRegistrationForm()
    if form.validate_on_submit():
        number = form.number.data
        hospital = form.hospital.data
        room_no = form.room_no.data
        with_oxygen = form.with_oxygen.data
        is_icu = form.is_icu.data
        with_ventilators = form.with_ventilators.data
        ngo = NGOs.query.filter_by(name=session.get('name')).first()

        bed = AvailableBeds(number=number, hospital=hospital,
                    room_no=room_no, with_oxygen=with_oxygen, is_icu=is_icu,
                    with_ventilators=with_ventilators, ngo=ngo)
        db.session.add(bed)
        db.session.commit()
        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('main.index')
        return redirect(next)
    if not session.get('name'):
        name = "Normal User"
    else:
        name = session.get('name')

    return render_template('bedreg.html', form=form, name=name)
 