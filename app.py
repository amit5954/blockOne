from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    classofStudent = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)

    def __repr__(self, firstName, lastName, classofStudent, nationality):
        return f"Student(firstName = {firstName}, lastName = {lastName}, classofStudent = {classofStudent}, nationality = {nationality})"


# db.create_all()
student_put_args = reqparse.RequestParser()
student_put_args.add_argument("firstName", type=str, help="First Name of the student is required", required=True)
student_put_args.add_argument("lastName", type=str, help="Last Name of the Student is required", required=True)
student_put_args.add_argument("classofStudent", type=str, help="class of the Student is required", required=True)
student_put_args.add_argument("nationality", type=str, help="Nationality of the Student", required=True)

student_update_args = reqparse.RequestParser()
student_update_args.add_argument("firstName", type=str, help="First Name of the student is required")
student_update_args.add_argument("lastName", type=str, help="Last Name of the student")
student_update_args.add_argument("classofStudent", type=str, help="Class of the student")
student_update_args.add_argument("nationality", type=str, help="Nationality on the student")

resource_fields = {
    'id': fields.Integer,
    'firstName': fields.String,
    'lastName': fields.String,
    'classofStudent': fields.String,
    'nationality': fields.String,
}


class Student(Resource):
    @marshal_with(resource_fields)
    def get(self, student_id):
        result = StudentModel.query.filter_by(id=student_id).first()
        if not result:
            abort(404, message="Could not find student with that id")
        return result

    @marshal_with(resource_fields)
    def post(self, student_id):
        args = student_put_args.parse_args()
        result = StudentModel.query.filter_by(id=student_id).first()
        if result:
            abort(409, message="Student id taken...")

        student = StudentModel(id=student_id,
                               firstName=args['firstName'],
                               lastName=args['lastName'],
                               classofStudent=args['classofStudent'],
                               nationality=args['nationality']
                               )
        db.session.add(student)
        db.session.commit()
        return student, 201

    @marshal_with(resource_fields)
    def put(self, student_id):
        args = student_update_args.parse_args()
        result = StudentModel.query.filter_by(id=student_id).first()
        if not result:
            abort(404, message="Student doesn't exist, cannot update")

        if args['firstName']:

            result.firstName = args['firstName']
        if args['lastName']:
            result.lastName = args['lastName']
        if args['classofStudent']:
            result.classofStudent = args['classofStudent']
        if args['nationality']:
            result.nationality = args['nationality']

        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, student_id):
        result = StudentModel.query.filter_by(id=student_id).first()
        if not result:
            abort(404, message="Could not find student with that id")
        db.session.delete(result)
        db.session.commit()
        return '', 204


api.add_resource(Student, "/student/<int:student_id>")


class AllStudents(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = StudentModel.query.all()
        if not result:
            abort(404, message="Could not find student with that id")
        return result


api.add_resource(AllStudents, "/allstudents")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
