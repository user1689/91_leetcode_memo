## Midterm_for_Info5100

\1. **Deep copy shallow copy**: Write a class for “Something” have multiple constructors for the class, Write a Copy Constructor for the class. 

```java
class Department {
  	private int departmentId;
  	private String departmentName;
  	public Department(int id, String name) {
      	this.departmentId = id;
      	this.departmentName = name;
    }
  	public int getDepartmentId() {
      	return this.departmentId;
    }
  	public String getDepartmentName() {
      	return this.departmentName;
    }
  	
  	public void setDepartmentId(int id) {
      	this.departmentId = id;
    }
  	public void setDepartmentName(String name) {
      	this.departmentName = name;
    }
}

class Employee {
    private int id;
    private String name;
    private Department dept;
    
    public Employee() {
        this.name = "default";
        this.id = 0;
        this.dept = null;
  }
    
    public Employee(Employee ee) {
        this.name = ee.getName();
        this.id = ee.getId();
        this.dept = new Department(1, "sample department");
  }
    
    public int getId() {
        return this.id;
  }

    public void setName(String name) {
        this.name = name;
    }
    
    public String getName() {
        return this.name;
  }

    public void setId(int id) {
        this.id = id;
    }

    public void printEmployeeInfo() {
        System.out.println("name: " + this.name);
        System.out.println("id: " + this.id);
    }
}

public class testDeepCopy {
    public static void main(String[] args) {
        Department software = new Department(1, "software");

        Employee sample = new Employee();
        Employee Jack = new Employee(sample);
        Jack.setName("Jack");
        Jack.setId(007);

        Employee Mark = new Employee(sample);
        Mark.setName("Mark");
        Mark.setId(006);

        Jack.printEmployeeInfo();
        Mark.printEmployeeInfo();
    }
}

/*---------------*/
public class Department{
  	
  	private int id;
  	private String name;
  
  	public Department(int id, String name) {
				this.id = id;
      	this.name = name;
    }  
  	
  	public void setId(int id) {
      	this.id = id;
    }
  
  	public void setName(String name) {
				this.name = name;
    }
  
  	public int getId() {
				return this.id;
    }
  
  	public String getName() {
      	return this.name;
    }
  
}

public class Professor {
  	private int uid;
  	private String name;
  	private Department dept;
  
  	public Professor(Professor p) {
      	this.uid = p.getUid();
      	this.name = p.getName();
      	this.dept = new Department(1, "sample department");
    }
  
  
  	public Professor() {
      	this.uid = 0;
      	this.name = "default";
      	this.dept = null;
    }
  	
  	public int getUid() {
      	return this.uid;
    }
  	
  	public String getName() {
      	return this.name;
    }
  	
  	public void setUid(int uid) {
      	this.uid = uid;
    }
  
  	public void setName(String name) {
				this.name = name;
    }
  
  	public void printInfo() {
				System.out.println("name: " + this.getName());
      	System.out.println("uid: " + this.getUid());
    }
     
}

public class main {
  	
  	public static void main (String args[]) {
				Professor sample = new Professor();
      	Professor jack = new Professor(sample);
      	jack.setName("jack");
 				jack.setUid(888);
      	jack.printInfo();
      	
    }
  
}
```

**2. Difference between abstract class and interface**: https://www.guru99.com/interface-vs-abstract-class-java.html#:~:text=An%20abstract%20class%20permits%20you,class%20can%20implement%20multiple%20interfaces. 

```java
```

\3. **Create a parent class and child class** : 

```java
class Demo() {
  	int id;
  	String name;
  	public Demo() {}
  	public Demo(int id, String name) {
      	this.id = id;
      	this.name = name;
    }
}

class Table() extends Demo{
  	int id;
  	String name;
  	int price;
  	public Table(int id, String name, int price) {
      	super(id, name);
      	this.price = price;
    }
}
```

\4. **Singleton/Pubsub**: [https://github.com/HappyCoder29/Spring2022-Info5100/blob/main/DesignPatterns/SingletonDesignpattern/src/edu/northeastern/ashish/Camera.java](https://github.com/HappyCoder29/Spring2022-Info5100/blob/main/DesignPatterns/SingletonDesignpattern/src/edu/northeastern/ashish/Camera.java)

```java
// singleton
public class Camera {
    
    private static Camera _instance;
    private static Object obj = new Object();
    private String CameraName = "";

    private Camera() {}

    public static Camera getInstance() {
        if (_instance == null) {
            synchronized(obj) {
                if (_instance == null) {
                    _instance = new Camera();
                }
            }
        }
        return _instance;
    }

    public String getCameraName() {
        return this.CameraName;
    }

}


// pubsub
import java.util.ArrayList;
import java.util.List;
class Professor {
  	
    String name;
    int id;
    List<Student> students;
    String quiz;

    public Professor() {}

    public Professor(String name, int id) {
        this.name = name;
        this.id = id;
        this.students = new ArrayList<>();
  }

    public void notifyStudents(String quiz) {
        this.quiz = quiz;
        for (int i = 0; i < students.size(); i++) {
            Student s = students.get(i);
            s.getNotify(this);
      }
            
  }
    
}

class Student {
  	
    String name;
    int id;

    public Student() {}

    public Student(String name, int id) {
        this.name = name;
        this.id = id;
  }

    public void subscribe(Professor professor) {
        if (!professor.students.contains(this)) {
          professor.students.add(this);
    }
  }

    public void unsubscribe(Professor professor) { 
        professor.students.remove(this);
  }
    
    public void getNotify(Professor professor) {
        System.out.println("---------");
        System.out.println("student name:" + this.name);
      System.out.println("professor name:" + professor.name);
        System.out.println("quiz content:" + professor.quiz);
      System.out.println("---------");
  }
}

public class testPubSub {
 
    public static void main(String[] args) {
        Student st1 = new Student("Student 1", 1);
        Student st2 = new Student("Student 2", 2);
        Student st3 = new Student("Student 3", 3);
        Student st4 = new Student("Student 4", 4);
        Student st5 = new Student("Student 5", 5);
        Professor prof1 = new Professor("Professor 1", 1);
        Professor prof2 = new Professor("Professor 2", 2);
        st1.subscribe(prof1);
        st2.subscribe(prof1);
        st3.subscribe(prof2);
        st4.subscribe(prof2);
        st5.subscribe(prof2);
        
        prof1.notifyStudents("Quiz1");
        try{
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        prof2.notifyStudents("Quiz2");
    }
}

```

\5. Some string question.

```java
```

