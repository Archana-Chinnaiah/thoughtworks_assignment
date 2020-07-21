it_subjects={"DS","DBMS","OS","C"}
cse_subjects={"PYTHON","DBMS","COMPILER DESIGN","C"}
mech_subjects={"Thermodynamics","maths","Fluid mechanics","C"}
civil_subjects={"coastal engineering","SAD","material science","C"}
it_students=[[1,'Arch',['c','c++','ds','python']],[2,'Abi',['c','dbms']],[3,'Anu',['os','c']],[4,'Agilan',['c','dbms']]]
cse_students=[[1,'Lavan',["DBMS","COMPILER DESIGN",'python','DS']],[2,'Keerthi',["PYTHON","DBMS"]],[3,'Kalai',["C","PYTHON"]],[4,'Arasan',["PYTHON","COMPILER DESIGN"]]]            
mech_students=[[1,'Pavi',["Thermodynamics","maths"]],[2,'Kabi',["Thermodynamics","C"]],[3,'Kavi',["maths","Fluid mechanics"]],[4,'Ajee',["Thermodynamics","Fluid mechanics"]]]
civil_students=[[1,'Ammu',["coastal engineering","SAD","material science"]],[2,'Karthi',["SAD","material science"]],[3,'Sri',["coastal engineering",'c']],[4,'Agil',["coastal engineering","material science"]]]


class Department:
    def __init__(self,student_list,dept_name,subject_list):
        self.student=student_list
        self.dept=dept_name
        self.subject=subject_list
        
def overlap(it,cse,mech,civil):
   it=it.subject
   cse=cse.subject
   mech=mech.subject
   civil=civil.subject    
   return list(it.intersection(cse,mech,civil))

    
def student_names(department,*dept_names):
    for each in dept_names:
        if(department.lower()==each.dept.lower()):
               for names in each.student:
                   print("*",names[1])
        
def course(*dept_names):
    for each in dept_names:
       for names in each.student:
           if(len(names[2])>3):
               print("#",each.dept)
                   
                  
  
    
    
it=Department(it_students,'IT',it_subjects)
cse=Department(cse_students,'CSE',cse_subjects)
mech=Department(mech_students,'MECH',mech_subjects)
civil=Department(civil_students,'CIVIL',civil_subjects)

print("\t\t****WELCOME TO PROGRAMMING****")
dept=input("\nEnter the department for student name List: ")
print("\nList of Student Names Belongs to the Department \n",)
student_names(dept,it,cse,mech,civil)
print("\nThe subjects that are overlap between different Departments are: ",overlap(it,cse,mech,civil))
print("\nDepartment Names WHERE the students take more than 3 COURSES: ")
course(it,cse,mech,civil)


      
        
    

