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

#update-
@app.route('/employee/<string:name>', methods=['POST'])
def update_employee(name):
    data = request.get()
    for employee in employees:

        if employee['name'] == name:
            employees.update('name', 'employee_id','skills')

            return jsonify({'message' : 'updated employee {}'.format(employee)})






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


#for Delete
@app.route('/employee/<int:employee_id>', methods=['DELETE'])
def del_emp(employee_id):
    global employees
    i=0
    delete= False

    for employee in employees:
        if employee['employee_id']==employee_id:
            employee.pop(i)
            delete=True
        i+=1

        if delete:
            return Response("", status=204, mimetype='application/json')
        else:
            return Response("", status=400, mimetype='application/json')








app.run(debug=True, port=6061)