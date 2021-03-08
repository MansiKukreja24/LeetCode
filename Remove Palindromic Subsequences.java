class Solution {
    public int removePalindromeSub(String s) {
        if(s.equals(""))
            return 0;
        if(isPalindrome(s))
            return 1;
        
        return 2;
    }    
    public boolean isPalindrome(String s){
        int a=0;
        int b=s.length()-1;
        while(b>a){
            if(s.charAt(a++)!=s.charAt(b--))
                return false;
            
            
        }
    return true;
    }
       
}
