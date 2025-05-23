function findFirst(nums: number[], target: number): number {
    let res = -1;
    let first = 0;
    let last = nums.length - 1;

    while (first <= last) {
        let mid = Math.floor(first + (last - first) / 2);

        if (nums[mid] >= target) {
            if (nums[mid] == target) {
                res = mid;
            }

            last = mid - 1;
        } else {
            first = mid + 1;
        }
    }

    return res;
}

function findLast(nums: number[], target: number): number {
    let res = -1;
    let first = 0;
    let last = nums.length - 1;

    while (first <= last) {
        let mid = Math.floor(first + (last - first) / 2);

        if (nums[mid] <= target) {
            if (nums[mid] == target) {
                res = mid;
            }

            first = mid + 1;
        } else {
            last = mid - 1;
        }
    }
    return res;
}

function searchRange(nums: number[], target: number): number[] {
    let first = findFirst(nums, target);
    let last = findLast(nums, target);

    console.log(first, last);

    if (first == -1) {
        return [last, last];
    } else if (last == -1) {
        return [first, first];
    }

    return [first, last];
}

searchRange([5, 7, 7, 8, 8, 10], 8);
