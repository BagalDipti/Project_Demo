from flask import Flask,jsonify,request, Response
app = Flask(__name__)
employees = [
    {
    'name': 'Dipti',
    'employee_id': 'GSC-30702',
    'skills': [
        {'name':'Ansible', 'proficiency_level': 'beginner' },
         {'name':'Linux', 'proficiency_level': 'Intermediate' },
          {'name':'Jenkins', 'proficiency_level': 'Professional' },
    ]
},

 {
    'name': 'Harshada',
    'employee_id': 'GSC-30700',
    'skills': [
        {'name':'Docker', 'proficiency_level': 'beginner' },
         {'name':'Kubernetes', 'proficiency_level': 'Intermediate' },
          {'name':'VMware', 'proficiency_level': 'Professional' },
    ]
}

]


@app.route('/')
def main():
    return 'Employee Information'




# To display all the employees
@app.route('/employees')
def get_employees():
    return  jsonify({'employees' : employees})



#To check Employee is present or not
@app.route('/employee/<string:name>')
def check_employee(name):
    for employee in employees:
        if employee['name'] == name :
            return jsonify(employee)
    return jsonify({'Alert' : 'Sorry, No employee found'})




#To Delete
@app.route('/employee/<string:name>', methods=['DELETE'])
def delete_employee(name):
    for employee in employees:
        if employee['name'] == name:
            employees.remove(employee)
            return jsonify({'message' : 'deleted employee {}'.format(name)})
    return jsonify({'Alert' : 'Sorry, No employee found'})




#  TO add new employee
@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = {
        'name': data['name'],
        'employee_id': data['employee_id'],
        'skills': data['skills']
    }
    employees.append(new_employee)
    return jsonify({'Messgae' : 'New Employee Successfully Added..!!'})









app.run(debug=True, port=6061)
