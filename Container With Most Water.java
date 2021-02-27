class Solution {
    public int maxArea(int[] height) {
        int n=height.length;
        int maximum=0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int current = (Math.min(height[i],height[j]) * (j-i));
                maximum=Math.max(maximum,current);
            }
        }
        return maximum;
        
    }
}
