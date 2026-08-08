bool isPalindrome(int x) {
    double n,i=0;
    int check=x;
    if(x<0)
    return false;
    else{
    while(x!=0){
        n=x%10;
        x=x/10;
        i=i*10+n;
    }
    if (i==check){
        return true;
    }
    else
    return false;}}
