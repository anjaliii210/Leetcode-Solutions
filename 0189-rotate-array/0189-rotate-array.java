class Solution {
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        rev(nums,0,n-k-1);
        rev(nums,n-k,n-1);
        rev(nums,0,n-1);
    }
    public static int[] rev(int [] arr,int start,int end){
        int temp=0;
        while(start<end){
            temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
        return arr;
    }
}