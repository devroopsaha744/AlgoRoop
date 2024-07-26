class Solution {
public:
    bool isPalindrome(int x) {
   long long rev =0;
   long long  num = x;

   if(x<0){
    return false;
   }

        while(x>0){
            int rem = x%10;
            rev = rev*10 + rem;
            x = x/10;
        }

        if(rev == num){
            return true;
        }
        else return false;
        }

    };