class Main{

static class employee{
    String name;
    int age ;
    double salary;

    employee(String name , int age , double salary){
        this.name = name;
        this.age = age ;
        this.salary = salary;
    }

}


static class teacher extends employee{
    double bouns = 0.5;
    teacher(String name ,  int age , double salary){
        super( name ,  age ,  salary);
        salary = (bouns * salary) + salary;
    } 

    void display(){
        System.out.print(this.name + this.age + "  " + this.salary);
    }

}








public static void main(String[] args){
teacher aboud = new teacher("Aboud" , 100 , 100000);
aboud.display();
}

}