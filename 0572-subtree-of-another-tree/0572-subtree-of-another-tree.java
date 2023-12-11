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
    List<TreeNode> list = new ArrayList<>();

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        dfs(root);
        String expectedStr = treeToString(subRoot);
        for (int i=0; i<list.size(); i++) {
            TreeNode current = list.get(i);
            String currentStr = treeToString(current);
            if (currentStr.equals(expectedStr)) return true;
        }
        return false;

    }

    public String treeToString(TreeNode root) {
        if (root == null) return ".";
        return root.val+","+treeToString(root.left)+","+treeToString(root.right);
    }

    public void dfs(TreeNode root) {
        if (root == null) return;
        list.add(root);
        dfs(root.left);
        dfs(root.right);
    }
}