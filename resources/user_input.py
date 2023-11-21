from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models.user_input import DocumentModel
from schemas import DocumentSchema

blp = Blueprint("Documents", "Documents", description="Operations on Documents")


@blp.route('/document', methods=['POST'])
class DocumentCreate(MethodView):

    @blp.arguments(DocumentSchema)
    def post(self, document_data):
        if 'file' not in request.files:
            abort(422, message='Missing file field in the request.')

        file = request.files['file']

        if 'name' not in document_data:
            abort(422, message='Missing name field in the request.')

        name = document_data['name']

        if DocumentModel.query.filter_by(name=name).first():
            abort(409, message='A document with that name already exists.')

        document = DocumentModel(name=name, content=file.read())
        db.session.add(document)
        db.session.commit()

        return document, 201


@blp.route('/document/<int:document_id>', methods=['GET'])
class DocumentRetrieve(MethodView):

    @blp.response(200, DocumentSchema)
    @blp.response(404, 'Document not found')
    def get(self, document_id):
        document = DocumentModel.query.get(document_id)
        if not document:
            abort(404, message='Document not found')

        return document
