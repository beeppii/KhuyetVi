# Khuyết Vị

Game nấu ăn hợp tác với 3 nhân vật **Mù, Điếc, Câm**, mỗi người chỉ có một phần giác quan nên phải phối hợp để hoàn thành món ăn. Game ghi lại dữ liệu chơi (CSV) và phân tích bằng pandas, numpy, matplotlib.

> Đồ án môn Lập trình Trí tuệ nhân tạo, nhóm 4 người, trình bày ngày 08/01/2027.

(Sửa lại 1–2 câu mô tả cho đúng với bản game design cuối cùng.)

## Thành viên

| Vai | Phụ trách | Thành viên | GitHub |
|---|---|---|---|
| A | Core Engine | (điền tên) | (điền username) |
| B | Kitchen Logic | (điền tên) | (điền username) |
| C | UI/UX & Assets | (điền tên) | (điền username) |
| D | Data & Analytics | (điền tên) | (điền username) |

## Công nghệ

- Python **3.13** (không dùng 3.14)
- pygame-ce 2.5.8
- numpy, pandas, matplotlib
- pytest

## Cài đặt và chạy

Cần cài sẵn Python 3.13, PyCharm (bản Community) và Git.

1. Clone repo về máy (trong PyCharm: Get from VCS, dán link repo).
2. Tạo môi trường ảo bằng đúng Python 3.13. Trong Terminal ở thư mục project:
   ```
   py -3.13 -m venv .venv
   ```
   Rồi trong PyCharm chọn interpreter là `.venv\Scripts\python.exe` vừa tạo.
3. Cài thư viện (đầu dòng Terminal phải có `(.venv)`):
   ```
   python -m pip install -r requirements.txt
   ```
4. Kiểm tra pygame:
   ```
   python -c "import pygame"
   ```
5. Chạy game:
   ```
   python main.py
   ```

Chạy test (khi đã có): `python -m pytest`

## Cấu trúc thư mục

```
main.py            # điểm vào của game
hello_pygame.py    # bài làm quen pygame (WASD, va chạm, chữ, âm thanh)
requirements.txt   # danh sách thư viện
```

Cập nhật mục này khi thêm thư mục mới.

## Quy tắc làm việc nhóm

- Nhánh `main` luôn chạy được. **Không code thẳng vào `main`.**
- Mỗi việc làm trên một nhánh riêng, đặt tên dạng `ten-vai/ten-viec`, ví dụ `A/di-chuyen-mu`.
- Tạo Pull Request nhỏ, có ít nhất 1 người review rồi mới merge.
- Viết commit message rõ ràng, ví dụ `Them hitbox tu lanh`, không viết `update` hay `fix`.
- Không đẩy `.venv/`, `.idea/`, `.vscode/`, `__pycache__/` lên Git (đã có trong `.gitignore`).
- Họp ngắn 15 phút vào thứ Hai và thứ Năm.

## Cách commit và push bằng PyCharm

Làm theo thứ tự này mỗi khi bắt đầu một việc mới:

1. **Cập nhật code mới nhất.** Chuyển về nhánh `main`, nhấn **Ctrl+T** (Update Project) để kéo code của cả nhóm về máy.
2. **Tạo nhánh mới cho việc của bạn.** Bấm vào tên nhánh ở thanh trên cùng (đang ghi `main`), chọn **New Branch...**, đặt tên theo quy tắc ở trên (ví dụ `A/di-chuyen-mu`), bấm **Create**. Nếu không thấy, mở menu ☰, chọn **Git**, rồi **New Branch...**
3. **Code xong một phần nhỏ thì commit.** Nhấn **Ctrl+K** để mở khung Commit. Kiểm tra danh sách file: chỉ tick những file bạn muốn commit và **không được có** `.venv` hay `.idea`. Viết message rõ ràng (ví dụ `Them hitbox tu lanh`), rồi bấm **Commit**.
4. **Push lên GitHub.** Nhấn **Ctrl+Shift+K** rồi bấm **Push**. Hoặc ở bước 3 bấm **Commit and Push** để làm cả hai việc cùng lúc. Lần đầu push một nhánh mới, PyCharm tự tạo nhánh đó trên GitHub.
5. **Tạo Pull Request.** Mở trang repo trên github.com, bấm nút **Compare & pull request**, viết vài dòng mô tả bạn đã làm gì, chọn một bạn làm **Reviewer**, bấm **Create pull request**.
6. **Review và merge.** Người review đọc code, nếu ổn thì bấm **Merge pull request**. Sau đó mọi người quay về `main` và nhấn **Ctrl+T** để cập nhật.

Lưu ý:

- Commit nhỏ và thường xuyên, mỗi khi xong một việc nhỏ. Đừng dồn cả ngày mới commit.
- Commit chỉ lưu trong máy của bạn. **Phải push** thì code mới lên GitHub.
- Nếu PyCharm báo xung đột (conflict) hoặc push bị từ chối (rejected), **không bấm Force Push**. Nhắn nhóm để cùng xử lý.

## Mốc tiến độ

| Mốc | Ngày | Kết quả |
|---|---|---|
| M0 | 29/11 | Game design 1 trang, repo, phân công đủ tên |
| M1 | 06/12 | Chạy ra 3 ô màn hình, nhân vật Mù đi được |
| M2 | 18/12 | Chơi trọn một ván thô, ghi log ra CSV |
| M3 | 27/12 | Đủ Start, Playing, Game Over, có biểu đồ. Đóng băng tính năng |
| M4 | 31/12 | Hết lỗi nặng, báo cáo và slide xong |
| Trình bày | 08/01 | |

Chi tiết công việc từng người nằm trong tài liệu kế hoạch của nhóm: (dán link tài liệu vào đây).
