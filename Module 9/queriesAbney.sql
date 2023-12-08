-- List the employee number, last name, first name, sex, and salary of each employee 
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from
	employees as e
	join salaries as s on e.emp_no = s.emp_no
order by
	s.salary desc;

-- List the first name, last name, and hire date for the employees who were hired in 1986
select
	e.first_name,
	e.last_name,
	e.hire_date
from employees as e
where e.hire_date between '01-01-1986' and '12-31-1986';
	

--List the manager of each department along with their department number, department name, employee number, last name, and first name.
select 
	dm.dept_no,
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from dept_manager as dm
	join departments as d on dm.dept_no = d.dept_no
	join employees as e on dm.emp_no = e.emp_no;

 -- List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
-- select 
-- 	e.first_name,
-- 	e.last_name,
-- 	d.dept_name,
-- 	de.dept_no,
-- 	e.emp_no
-- from employees as e 
-- 	join dept_emp as de on de.dept_no = e.emp_no;

--List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
select
	 e.first_name,
	 e.last_name,
	 e.sex
from employees as e
where e.first_name = 'Hercules' and e.last_name like 'B%';


-- List each employee in the Sales department, including their employee number, last name, and first name (2 points)
select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on de.dept_no = d.dept_no
where d.dept_name = 'Sales';
	
--List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments d on de.dept_no = d.dept_no
where 
	d.dept_name in ('Sales', 'Development');
	

-- List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).
select
	e.last_name,
	count e.last_name
from employees as e
group by e.last_name;