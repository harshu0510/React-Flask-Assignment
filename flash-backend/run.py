from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.route("/api/employees", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.as_dict() for employee in employees])

@app.route("/api/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    employee = Employee(name=data["name"], position=data["position"], salary=data["salary"])
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee.as_dict()), 201

@app.route("/api/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.get_json()
    employee = Employee.query.get(employee_id)
    employee.name = data["name"]
    employee.position = data["position"]
    employee.salary = data["salary"]
    db.session.commit()
    return jsonify(employee.as_dict())

@app.route("/api/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Check if database is empty before pre-filling with sample data
        if Employee.query.count() == 0:
            sample_data = [
                {"name": "Atif Hussain", "position": "Data Analyst", "salary": 75000},
                {"name": "Somitav Mishra", "position": "Business Analyst", "salary": 65000},
                {"name": "Bob Johnson", "position": "Project Manager", "salary": 85000},
                {"name": "John Doe", "position": "Software Engineer", "salary": 70000},
                {"name": "Michael Brown", "position": "Quality Assurance Engineer", "salary": 72000},
                {"name": "Jane Smith", "position": "UI/UX Designer", "salary": 78000},
                {"name": "Chris Miller", "position": "Systems Administrator", "salary": 68000},
                {"name": "Megan Wilson", "position": "Marketing Specialist", "salary": 60000},
                {"name": "Kevin Lee", "position": "Network Engineer", "salary": 82000},
                {"name": "Sara Martinez", "position": "Financial Analyst", "salary": 75000},
                {"name": "Daniel Taylor", "position": "Product Manager", "salary": 88000},
                {"name": "Laura Hall", "position": "Human Resources Specialist", "salary": 65000},
                {"name": "Alex Turner", "position": "IT Support Technician", "salary": 62000},
                {"name": "Grace Adams", "position": "Customer Support Representative", "salary": 58000},
                {"name": "Jordan White", "position": "Sales Executive", "salary": 70000},
                {"name": "Olivia Thomas", "position": "Legal Counsel", "salary": 90000},
                {"name": "Ethan Carter", "position": "Database Administrator", "salary": 82000},
                {"name": "Sophia Lewis", "position": "Graphic Designer", "salary": 63000},
                {"name": "Nathan Scott", "position": "Operations Manager", "salary": 80000},
                {"name": "Ava Allen", "position": "Health and Safety Officer", "salary": 70000},
            ]
            for data in sample_data:
                employee = Employee(name=data["name"], position=data["position"], salary=data["salary"])
                db.session.add(employee)
            db.session.commit()
    app.run(debug=True)
