/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    int count = 0;
    int result = 0;


    public int kthSmallest(TreeNode root, int k) {
        // if (root == null) return result;

        // kthSmallest(root.left, k);
        // count++;
        // if (count == k) {
        //     result = root.val;
        //     return result; 
        // }
        // kthSmallest(root.right, k);

        // return result;

        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        int count = 0;

        while (current != null || !stack.isEmpty()){
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            count++;

            if (count == k) return current.val;

            current = current.right;
        }

        return -1;
    }

}
