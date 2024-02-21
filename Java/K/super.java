package K;


class student  {
String name;
int age ;

student(String name , int age ){
    this.name = name;
    this.age = age;
}


public static void main(String[] args){
    Stage s1 = new Stage("1" , "aboud" , 12);

    System.out.print(s1.stage);
}
}






class Stage extends student{
    String stage;
 Stage(String stage , String name , int age ){
        super( name ,  age );
        this.stage = stage; 
         
    }
}