use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_map: HashMap<i32, i32> = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            let fres = target - num;
            if let Some(&index) = num_map.get(&fres) {
                return vec![index, i as i32];
            } else {
                num_map.insert(*num, i as i32);
            };
        };
        return vec![]
    }
}