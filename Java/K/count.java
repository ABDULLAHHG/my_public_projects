package K;


class count {
static int count = 0;
count(){
    count++;
}
public static void main(String[] args){
    student s1 = new student("a" , 1 , "1");
    System.out.print(s1.count);
}
}


class student extends count {
String name;
int age ;
String stage ;

student(String name , int age , String stage){
    super();
    this.name = name;
    this.age = age;
    this.stage = stage;
}

}
