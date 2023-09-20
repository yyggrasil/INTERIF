#include <iostream>

using namespace std;

int main(){
    string MSG = "NEGADO";    
    int Senha[4];
    for(int i =0;i<4;i++){
        cin >> Senha[i];
    }
    if(Senha[0]<Senha[1]&&Senha[1]<Senha[2] && (Senha[3] == (Senha[1]+Senha[0]+Senha[2]))){
            MSG = "LIBERADO";
    }
    cout << MSG << endl;

    return 0;
}