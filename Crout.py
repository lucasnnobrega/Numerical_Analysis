##
# Código de Crout
##



#include <iostream>


#int main (void){
if __name__ == "__main__":

    #float Y[3][3] = {{3.0, 2.0, 4.0}, {1.0, 1.0, 2.0}, {4.0, 3.0, 2.0}};
    Y = [[3, 2, 4],\
         [1, 1, 2],\
         [4, 3, 2]]
    #float sum;
    sum = 0

    #float L[3][3] = {0.0}, U[3][3] = {0.0};
    L = [[0 for j in range(3)] for i in range(3)]
    U = [[0 for j in range(3)] for i in range(3)]

    #for(int j = 0; j < 3; j++){
    for j in range (3):
        #for(int i = 0; i < 3; i++){
        for i in range(3):    
            #sum = 0.0;
            sum = 0.0

            #for(int k = 0; k < j ; k++){
            for k in range(j):
                #sum = sum + L[i][k]*U[k][j];
                sum = sum + L[i][k]*U[k][j]
            #}

            #if(i == j)
            if(i == j):
                #U[i][j] = 1; 
                U[i][j] = 1 

            #if(i >= j){
            if(i >= j):
                #L[i][j] = Y[i][j] - sum;
                L[i][j] = Y[i][j] - sum
            #}
            #else
            else:
                #U[i][j] = ((Y[i][j] - sum)/(L[i][i]));
                U[i][j] = ((Y[i][j] - sum)/(L[i][i]))
        #}
    #}

    print("Y")
    #for(int j = 0; j < 3; j++){
    for j in range(3):
        #for(int i = 0; i < 3; i++){
        for i in range(3):
            #std::cout << L[j][i] << " ";
            print("{:3f}".format(Y[j][i]), end=" ")
        #}
        #std::cout << std::endl;
        print()
    #}
    print("L")
    #for(int j = 0; j < 3; j++){
    for j in range(3):
        #for(int i = 0; i < 3; i++){
        for i in range(3):
            #std::cout << L[j][i] << " ";
            print("{:3f}".format(L[j][i]), end=" ")
        #}
        #std::cout << std::endl;
        print()
    #}

    #std::cout << std::endl;
    print("U")
    #for(int j = 0; j < 3; j++){
    for j in range(3):
        #for(int i = 0; i < 3; i++){
        for i in range(3):
            #std::cout << U[j][i] << " ";
            print("{:3f}".format(U[j][i]), end=" ")
        #}
        #std::cout << std::endl;
        print()
    #}

    #return 0;
#}