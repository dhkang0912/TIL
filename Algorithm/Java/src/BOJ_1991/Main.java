package BOJ_1991;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    Map<String, Node> tree = new HashMap<>(); // 트리 저장

    class Node {
        String left, right;
        Node(String left, String right) {
            this.left = left;
            this.right = right;
        }
    }

    void preorder(String node){
        if(node.equals(".")) return; // equals 통해 값 비교
        System.out.print(node);
        preorder(tree.get(node).left);
        preorder(tree.get(node).right);
    }

    void inorder(String node){
        if (node.equals(".")) return;
        inorder(tree.get(node).left);
        System.out.print(node);
        inorder(tree.get(node).right);
    }

    void postorder(String node){
        if (node.equals(".")) return;
        postorder(tree.get(node).left);
        postorder(tree.get(node).right);
        System.out.print(node);
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.run();
    }

    public void run() throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N ; i++) {
            String[] input = br.readLine().split(" "); // split을 사용하면 바로 배열에 넣을 수 있음
            tree.put(input[0], new Node(input[1], input[2]));
        }

        preorder("A");
        System.out.println();
        inorder("A");
        System.out.println();
        postorder("A");
        System.out.println();

    }


}
