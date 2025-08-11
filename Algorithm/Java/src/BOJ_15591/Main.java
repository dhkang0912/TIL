package BOJ_15591;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    // 2차원 컬렉션 선언 => Null 입력됨, 인덱스 = (목적지, usado)
    static ArrayList<ArrayList<int[]>> graph;
    // visited 배열 선언 => Null 입력됨
    static boolean[] visited;

    static void dfs (int usado, int node){
        Stack<Integer> stack = new Stack<>();
        stack.push(node);
        visited[node] = true;

        while (!stack.isEmpty()){
            int v = stack.pop();

            for (int[] next:graph.get(v)){
                int nextNode = next[0];
                int nextUsado = next[1];

                if (!visited[nextNode] && nextUsado >= usado){
                    visited[nextNode] = true;
                    stack.push(nextNode);
                }

            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        // 그래프 초기화
        graph = new ArrayList<>();
        // N+1개 만들어서 0번은 비워둠
        for (int i = 0; i <= N; i++){
            graph.add((new ArrayList<>()));
        }

        // 간선 입력 처리
        // N개 입력 받아서 간선 입력
        // 루트 노트 제외 총 N-1의 간선이 존재
        for (int i = 1; i < N; i++){
            st = new StringTokenizer(br.readLine().trim());
            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            // 양방향 그래프
            // 컬렉션으로 선언하여 get을 사용하여 해당 인덱스의 리스트를 가져오고, [q,r] 형태의 리스트를 추가하는 것
            graph.get(p).add(new int[]{q, r});
            graph.get(q).add(new int[]{p, r});
        }

        // 질문 처리
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i<Q; i++){
            st = new StringTokenizer(br.readLine().trim());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            visited = new boolean[N+1];

            // DFS 탐색
            dfs(k, v);

            // 방문한 노드 개수 - 자기 자신 제외
            int count = -1;
            for (int j = 1; j<=N; j++){
                if(visited[j]) count++;
            }

            // 결과 저장
            sb.append(count).append("\n");
        }
        System.out.print(sb);


    }


}
