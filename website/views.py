from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import MusicCatalog
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_data = request.form.get('note_data')
        composerName = request.form.get('composerName')
        pieceName = request.form.get('pieceName')
        pieceDate = request.form.get('pieceDate')

        new_piece = MusicCatalog(composerName=composerName, pieceName=pieceName,
                                 pieceDate=pieceDate, user_id=current_user.id, note_data=note_data)
        db.session.add(new_piece)
        db.session.commit()
        flash('Piece Cataloged!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = MusicCatalog.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
