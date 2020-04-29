# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
    merged_nums = (nums1+nums2).sort!
    median_index = (merged_nums.length-1)/2.to_f
    if median_index.floor == median_index
        merged_nums[median_index.to_i].to_f
    else
        (merged_nums[(median_index-0.5).to_i] + merged_nums[(median_index+0.5).to_i])/2.to_f
    end
end