class Solution {
    public int climbStairs(int n) {
        if(n<=2){
            return n;
        }
        int[] l=new int[n];
        l[0]=1;
        l[1]=2;
        for(int i=2;i<n;i++){
            l[i]=l[i-1]+l[i-2];
        }
        return l[n-1];
            
        
    }
}
