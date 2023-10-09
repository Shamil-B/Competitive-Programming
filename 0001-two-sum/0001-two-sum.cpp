class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
//         int p1 = 0;
        int size = nums.size(); // Use nums.size() to get the size of the vector
//         int p2 = size-1;
//         sort(nums.begin(), nums.end());
        
        

//         while(p2 > p1){
//             int sum = nums[p2] + nums[p1];
//             if(sum == target){
//                 vector<int> ans = {p1, p2};
//                 return ans;
//             }
            
//             else if(sum < target){
//                 p1 = p1 + 1;
//             }
//             else{
//                 p2 = p2 - 1;
//             }
//         }

//         // Handle the case when no valid pair is found
//         return {}; // Return an empty vector to indicate no solution
        
        for(int i = 0; i < size; i++){
            for(int j = size-1; j > 0; j--){
                if((nums[i] + nums[j] == target) & (i != j)){
                    return {i, j};
                }
            }
        }
        return {};
    }
};
