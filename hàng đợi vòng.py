class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity      # kích thước cố định
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("⚠️ Hàng đợi đầy, không thể thêm!")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"✅ Đã thêm {item} vào hàng đợi.")

    def dequeue(self):
        if self.is_empty():
            print("⚠️ Hàng đợi rỗng, không thể lấy!")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:  # chỉ còn 1 phần tử
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"🛠️ Lấy ra: {data}")
        return data

    def display(self):
        if self.is_empty():
            print("📭 Hàng đợi rỗng.")
            return
        print("👥 Hàng đợi: ", end="")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()
        
cq = CircularQueue(5)  # tạo hàng đợi vòng dung lượng 5

while True:
    print("\n===== MENU HÀNG ĐỢI VÒNG =====")
    print("1. Thêm phần tử")
    print("2. Lấy phần tử")
    print("3. Hiển thị hàng đợi")
    print("4. Thoát")
    choice = input("Chọn thao tác: ")

    if choice == "1":
        val = input("Nhập giá trị: ")
        cq.enqueue(val)
    elif choice == "2":
        cq.dequeue()
    elif choice == "3":
        cq.display()
    elif choice == "4":
        print("👋 Thoát chương trình.")
        break
    else:
        print("❌ Vui lòng nhập số từ 1-4.")
