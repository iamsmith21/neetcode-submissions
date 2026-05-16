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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // if (root == null && subRoot != null ) return false;
        if (root == null ) return false;
        if (sameTree(root,subRoot)) return true;

        Boolean v1 = false;
        Boolean v2 = false;
        if (!sameTree(root,subRoot)) {
            v1 =  isSubtree(root.left, subRoot);
            v2 = isSubtree(root.right, subRoot);

        }
           return (v1 || v2);
    }

    public boolean sameTree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true;
        }
        if (root != null && subRoot != null && root.val == subRoot.val) {
            return sameTree(root.left, subRoot.left) &&
                   sameTree(root.right, subRoot.right);
        }
        return false;
    }
}
