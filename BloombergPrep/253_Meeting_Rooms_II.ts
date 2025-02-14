/**
 * 253. Meeting Rooms II
 * Solved
 * Medium
 * Topics
 * Companies
 * Hint
 * Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
 * 
 *  
 * 
 * Example 1:
 * 
 * Input: intervals = [[0,30],[5,10],[15,20]]
 * Output: 2
 * Example 2:
 * 
 * Input: intervals = [[7,10],[2,4]]
 * Output: 1
 *  
 * 
 * Constraints:
 * 
 * - 1 <= intervals.length <= 10^4
 * - 0 <= starti < endi <= 10^6
 */
import { MinPriorityQueue } from '@datastructures-js/priority-queue'

function minMeetingRooms(intervals: number[][]): number {
    if (!intervals.length) {
        return 0;
    }

    intervals.sort((a, b) => a[0] - b[0]);

    const pq = new MinPriorityQueue();

    pq.enqueue(intervals[0][1]);

    for (let i = 1; i < intervals.length; i++) {
        if (pq.front().element <= intervals[i][0]) {
            pq.dequeue();
        }

        pq.enqueue(intervals[i][1]);
    }

    return pq.size()
};
