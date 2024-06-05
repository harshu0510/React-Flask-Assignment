import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './style.css';

const EmployeeList = () => {
  const [employees, setEmployees] = useState([]);
  const [filter, setFilter] = useState({
    name: '',
    salary: 0,
  });

  // useEffect to fetch data only once when component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/employees');
        setEmployees(response.data);
      } catch (error) {
        console.error('Error fetching employees:', error);
      }
    };
    fetchData();
  }, []); // empty dependency array ensures this runs only once

  const handleFilterChange = (event) => {
    const { name, value } = event.target;
    setFilter((prevFilter) => ({...prevFilter, [name]: value }));
  };

  const filteredEmployees = employees.filter((employee) => {
    const nameMatch = employee.name.toLowerCase().includes(filter.name.toLowerCase());
    const salaryMatch = employee.salary >= parseInt(filter.salary);
    return nameMatch && salaryMatch;
  });

  return (
    <div className="employee-list">
      <h1>Employee List</h1>
      <form className="filter-form">
        <label>
          Filter by Name:
          <input type="text" name="name" value={filter.name} onChange={handleFilterChange} />
        </label>
        <br />
        <label>
          Filter by Salary (min):
          <input type="number" name="salary" value={filter.salary} onChange={handleFilterChange} />
        </label>
      </form>
      <ul className="employee-list-ul">
        {filteredEmployees.map((employee) => (
          <li key={employee.id} className="employee-list-item">
            {employee.name} - {employee.position} - {employee.salary}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmployeeList;
