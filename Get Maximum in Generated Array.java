class Solution {
    public int getMaximumGenerated(int n) {
        if(n<2)
            return n;
        int[] arr=new int[n+1];
        arr[0]=0;
        arr[1]=1;
        int i=1;
        int maximum=Integer.MIN_VALUE;
        while(2*i<=n || ((2*i)+1)<=n){
            arr[2*i]=arr[i];
            maximum=Math.max(maximum,arr[2*i]);
            if((2*i)+1 <= n){
                arr[(2*i)+1]=arr[i]+arr[i+1];
                maximum=Math.max(maximum,arr[(2*i)+1]);
        }
            i++;
        }
                
            
        return maximum;
    }
}
