# ASSIGNMENT_1_AI

Mã nguồn cho Assignment 1 - Nhập môn AI - HK251 - BKHCM

## Cấu trúc thư mục

```
📦 ASSIGNMENT_1_AI
├── 📁 Backend
│ ├── 📁 pycache
│ ├── 📁 BlindSearch
│ ├── 📁 Heuristic
│ ├── 📁 venv
│ ├── init.py
│ ├── chartEt.py
│ ├── chartMt.py
│ ├── index.py
│ ├── README.md
│ └── utils.py
│
├── 📁 Frontend
│ ├── 📁 Images
│ ├── 📁 screens
│ │ ├── Map.js
│ │ └── Menu.js
│ ├── game.js
│ └── style.css
│
├── 📁 SokobanMap
│
├── index.html
├── memory_comparison.png
├── README.md
└── runtime_comparison_ms.png
```

---

## 💻 Frontend

Mở **Live Server** với file `index.html` để xem lời giải đã lưu (dựa trên kết quả thuật toán).

```
📦 ASSIGNMENT_1_AI
├── 📁 Backend
├── 📁 Frontend
├── 📁 SokobanMap
├── index.html ← File này cần mở
├── memory_comparison.png
├── README.md
└── runtime_comparison_ms.png

```

### ⚠️ Lưu ý:

Đường dẫn có thể khác nhau giữa các thiết bị hoặc trình duyệt, gây lỗi **không đọc được file**.  
Trong trường hợp đó, cần sửa lại **3 vị trí** sau:

1. **`Frontend/game.js`** dòng **8** → sửa đường dẫn của `res`.
2. **`Frontend/screens/Map.js`**:
   - Dòng **17**: sửa `imagePaths`.
   - Dòng **129**: sửa `path`.

👉 Hoặc xem trực tiếp bản deploy tại:  
🔗 [https://mangtre503.github.io/ASSIGNMENT_1_AI/](https://mangtre503.github.io/ASSIGNMENT_1_AI/)

---

## Backend:

    Xem ASSIGNMENT_1_AI\Backend\index.py <br>
    Xem ASSIGNMENT_1_AI\Backend\Evaluate\index.py cho các hàm đánh giá về time, memory <br>
    Xen ASSIGNMENT_1_AI\Backend\Heuristic\index.py cho hàm heuristic <br>
