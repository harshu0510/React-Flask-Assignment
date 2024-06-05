import React, { useState } from 'react';
import axios from 'axios';
import './style.css';

const WelcomePage = () => {
  const [employee, setEmployee] = useState({
    name: '',
    position: '',
    salary: 0,
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://127.0.0.1:5000/api/employees', employee)
     .then(response => {
        console.log(response.data);
      })
     .catch(error => {
        console.error(error);
      });
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setEmployee((prevEmployee) => ({...prevEmployee, [name]: value }));
  };

  return (
    <div className="welcome-page">
      <h1>Welcome to Employee Management System</h1>
      <form onSubmit={handleSubmit} className="form">
        <label>
          Name:
          <input type="text" name="name" value={employee.name} onChange={handleChange} />
        </label>
        <br />
        <label>
          Position:
          <input type="text" name="position" value={employee.position} onChange={handleChange} />
        </label>
        <br />
        <label>
          Salary:
          <input type="number" name="salary" value={employee.salary} onChange={handleChange} />
        </label>
        <br />
        <button type="submit" className="btn">Add Employee</button>
      </form>
    </div>
  );
};

export default WelcomePage;
