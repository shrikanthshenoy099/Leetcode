class Solution {
    public int[] runningSum(int[] nums) {
        int su=0;
        int n=nums.length;
        int[] res=new int[n];
        for(int i=0;i<n;i++){
            res[i]=su + nums[i];
            su=res[i];
        }
        return res;
        
    }
}