#include <stdio.h> 
int main(){
    int n;
    printf("\nEnter size of buffer: "); 
    scanf("%d",&n);
    int buffer[n],produce,consume,choice=0,bufsize = n; 
    int in = 0; 
    int out = 0; 
    while(choice !=3){
        printf("\n1. Produce \t 2. Consume \t3. Exit");
        printf("\nEnter your choice: "); 
        scanf("%d",&choice);
        switch(choice){
            case 1: 
                if((in+1)%bufsize==out){
                printf("\nBuffer is Full");
                break;
                }
                else{
                    printf("\nEnter the value: "); 
                    scanf("%d", &produce); 
                    buffer[in] = produce; 
                    in = (in+1)%bufsize;
                    break;
                }
            case 2: 
                if(in == out){ 
                    printf("\nBuffer is Empty");
                    break;
                }
                else{ 
                    consume = buffer[out]; 
                    printf("\nThe consumed value is %d", consume); 
                    out = (out+1)%bufsize; 
                    break;
                }
        }
    } 
    
} 
