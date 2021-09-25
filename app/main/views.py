from app.models import AvailableBeds, NGOs
from flask import render_template, url_for, session, redirect

from . import main
from .forms import BedRegistrationForm
from .. import db

@main.route('/', methods=['GET','POST'])
def index():
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
        return redirect(url_for('main.index'))

    return render_template('index.html', form=form, name=session.get('name'), beds=AvailableBeds.query.all()[::-1]), 200