CREATE DATABASE EMPLOYEE_INFO;
USE EMPLOYEE_INFO;

CREATE TABLE IF NOT EXISTS employees (
    employee_id VARCHAR(10) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    department VARCHAR(50) NOT NULL
);


INSERT INTO employees (employee_id, full_name, position, email, phone_number, department) VALUES
('EMP001', 'Arjun Sharma', 'Senior HR Manager', 'arjun.sharma@company.com', '+91-98765-43210', 'Human Resources'),
('EMP002', 'Priya Patel', 'Talent Acquisition Specialist', 'priya.patel@company.com', '+91-98765-43211', 'Human Resources'),
('EMP003', 'Rohan Das', 'IT Helpdesk Administrator', 'rohan.das@company.com', '+91-87654-32109', 'Information Technology'),
('EMP004', 'Ananya Iyer', 'Compensation & Benefits Lead', 'ananya.iyer@company.com', '+91-98765-43212', 'Human Resources'),
('EMP005', 'Vikram Malhotra', 'Director of Engineering', 'vikram.m@company.com', '+91-76543-21098', 'Engineering'),
('EMP006', 'Sneha Kapoor', 'Senior Frontend Engineer', 'sneha.kapoor@company.com', '+91-76543-21099', 'Engineering'),
('EMP007', 'Amit Verma', 'DevOps Infrastructure Lead', 'amit.verma@company.com', '+91-65432-10987', 'Engineering'),
('EMP008', 'Meera Nair', 'Finance & Payroll Specialist', 'meera.nair@company.com', '+91-54321-09876', 'Finance'),
('EMP009', 'Kabir Mehta', 'Legal Compliance Counsel', 'kabir.mehta@company.com', '+91-43210-98765', 'Legal'),
('EMP010', 'Neha Joshi', 'Chief People Officer', 'neha.joshi@company.com', '+91-98765-43213', 'Executive Branch');
