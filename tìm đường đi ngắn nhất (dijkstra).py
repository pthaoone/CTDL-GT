import networkx as nx #thư viện xử lý đồ thị
import matplotlib.pyplot as plt #thư viện vẽ đồ thị
import random
from heapq import heappush, heappop #thư viện hàng đợi ưu tiên

def random_pos(nodes):
    return {n: (random.uniform(0, 1), random.uniform(0, 1)) for n in nodes} # Tạo vị trí ngẫu nhiên cho các node trong đồ thị

def draw_graph(G, pos, path=None, title="Đồ thị Dijkstra"): # Vẽ đồ thị
    plt.figure(title) 
    nx.draw(G, pos, with_labels=True, node_color="lightblue", arrows=True, node_size=700) 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"))
    if path and len(path) > 1:
        nx.draw_networkx_edges(G, pos, edgelist=list(zip(path, path[1:])),
                               edge_color="r", width=2.5, arrows=True)
    plt.title(title)
    plt.show()

def dijkstra(G, start, end):
    dist = {n: float('inf') for n in G.nodes} 
    prev = {n: None for n in G.nodes} 
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heappop(pq)
        if u == end:
            break
        for v, data in G[u].items():
            w = data['weight']
            if d + w < dist[v]:
                dist[v] = d + w
                prev[v] = u
                heappush(pq, (dist[v], v))

    path = []
    node = end
    while node:
        path.append(node)
        node = prev[node]
    return list(reversed(path)), dist[end]

def input_graph():
    G = nx.DiGraph()
    while True:
        try:
            n = int(input("Nhập số node: "))
            if 1 <= n:
                break
            else:
                print(f"Số node phải nằm trong khoảng 1 đến {n}.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

    while True:
        nodes = input(f"Nhập {n} tên node (vd: A B C D ...): ").split()
        if len(nodes) != n:
            print(f"Bạn phải nhập đúng {n} node.")
            continue
        if len(nodes) != len(set(nodes)):
            print("Có tên node bị trùng! Vui lòng nhập lại.")
            continue
        break

    for node in nodes:
        G.add_node(node)

    print("\nNhập cạnh dạng: u v w (vd: A B 5). Gõ 'done' để dừng. Gõ 'delete' để xóa cạnh vừa nhập.")
    
    while True:
        line = input("Cạnh: ").strip()
        if line.lower() == "done":
            break

        if line.lower() == "delete":
            if G.number_of_edges() == 0:
                print("Không có cạnh nào để xóa!")
                continue
            u = input("Nhập node nguồn của cạnh cần xóa: ").strip()
            v = input("Nhập node đích của cạnh cần xóa: ").strip()
            if G.has_edge(u, v):
                G.remove_edge(u, v)
                print(f"Cạnh {u} → {v} đã được xóa.")
            else:
                print(f"Cạnh {u} → {v} không tồn tại!")
            continue

        try:
            u, v, w = line.split()
            w = float(w)

            # Kiểm tra node tồn tại
            missing = [x for x in [u, v] if x not in G.nodes]
            if missing:
                print(f"Node {', '.join(missing)} không tồn tại trong đồ thị")
                continue

            # Kiểm tra trùng cạnh cùng chiều
            if G.has_edge(u, v):
                print(f"Cạnh {u} → {v} đã tồn tại! Không được nhập lại.")
            # Kiểm tra cạnh ngược chiều
            elif G.has_edge(v, u):
                print(f"Cạnh {v} → {u} đã tồn tại! Không được thêm ngược lại.")
            # kiểm tra node tự nối với chính nó
            elif u == v:
                print("Không được phép nối một node với chính nó!")
            # Kiểm tra trọng số âm
            elif w < 0:
                print("Trọng số cạnh không được âm!")
            else:
                G.add_edge(u, v, weight=w)

        except ValueError:
            print("Sai định dạng! Hãy nhập theo dạng: u v w (ví dụ: A B 5.2)")

    print("\nDanh sách cạnh hiện tại:")
    for u, v, w in G.edges(data="weight"):
        print(f"{u} → {v} (w={w})")
    return G

def run_dijkstra(G):
    pos = random_pos(G.nodes)
    print("\nCác node:", " ".join(G.nodes))

    # Nhập node bắt đầu
    while True:
        s = input("Nhập node bắt đầu: ").strip()
        if s not in G.nodes:
            print(f"Node '{s}' không tồn tại! Vui lòng nhập lại.")
        else:
            break

    # Nhập node kết thúc
    while True:
        t = input("Nhập node kết thúc: ").strip()
        if t not in G.nodes:
            print(f"Node '{t}' không tồn tại! Vui lòng nhập lại.")
        elif t == s:
            print("Node bắt đầu và kết thúc phải khác nhau! Nhập lại.")
        else:
            break

    path, total = dijkstra(G, s, t)
    total = round(total, 2)
    print("\nKết quả (Dijkstra tự cài):", path, "→ Tổng trọng số:", total)
    draw_graph(G, pos, path, title=f"Đường đi ngắn nhất: {s} → {t}")

def main():
    G = None
    while True:
        print("\n=== MENU ĐỒ THỊ DIJKSTRA (CÓ HƯỚNG) ===")
        print("1. Nhập đồ thị mới")
        print("0. Thoát")
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            G = input_graph()
            run_dijkstra(G)
        elif choice == "0":
            print("Kết thúc chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

if __name__ == "__main__":
    main()