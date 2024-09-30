import java.util.*;
public class prime {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int count=0;
        for(int i=0;i<n;i++){
            if(n%2==0){
                count++;
            }
        }
        if(count>2){
            System.out.println("Not a Prime");
        }else{
            System.out.println("Prime Number");
        }
    }
}
