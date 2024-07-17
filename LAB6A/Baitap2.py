import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Quét")
        self.root.geometry("800x500")
        self.root.configure(bg='#ffb6c1')  # Màu nền hồng

        self.create_widgets()

    def create_widgets(self):
        # Khung chính được chia thành thanh bên và khu vực nội dung chính
        main_frame = tk.Frame(self.root, bg='#ffb6c1')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Thanh bên
        side_frame = tk.Frame(main_frame, width=200, bg='#ffb6c1', padx=10, pady=10)
        side_frame.pack(side=tk.LEFT, fill=tk.Y)

        label_status = tk.Label(side_frame, text="Trạng thái:", font=("Helvetica", 14), bg='#ffb6c1')
        label_status.pack(pady=(20, 10))

        label_update = tk.Label(side_frame, text="Cập nhật:", font=("Helvetica", 14), bg='#ffb6c1')
        label_update.pack(pady=(10, 10))

        button_scan_now = tk.Button(side_frame, text="Quét ngay", width=15, font=("Helvetica", 12), command=self.scan_now)
        button_scan_now.pack(pady=10)

        button_help = tk.Button(side_frame, text="Trợ giúp", width=15, font=("Helvetica", 12))
        button_help.pack(pady=10)

        button_settings = tk.Button(side_frame, text="Cài đặt", width=15, font=("Helvetica", 12))
        button_settings.pack(pady=10)

        # Khu vực chính
        content_frame = tk.Frame(main_frame, bg='white', padx=20, pady=20)
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        label_title = tk.Label(content_frame, text="Ứng dụng Quét", font=("Helvetica", 24), bg='white')
        label_title.pack()

        label_subtitle = tk.Label(content_frame, text="Phiên bản 1.0", font=("Helvetica", 14), bg='white', fg='gray')
        label_subtitle.pack(pady=(0, 20))

        button_quick_scan = tk.Button(content_frame, text="Quét nhanh", width=15, font=("Helvetica", 12), command=self.quick_scan)
        button_quick_scan.pack(side=tk.LEFT, padx=10, pady=10)

        button_web_protection = tk.Button(content_frame, text="Bảo vệ web", width=15, font=("Helvetica", 12), command=self.web_protection)
        button_web_protection.pack(side=tk.LEFT, padx=10, pady=10)

        button_simple_update = tk.Button(content_frame, text="Cập nhật đơn giản", width=15, font=("Helvetica", 12), command=self.simple_update)
        button_simple_update.pack(side=tk.LEFT, padx=10, pady=10)

        button_full_scan = tk.Button(content_frame, text="Quét toàn bộ", width=15, font=("Helvetica", 12), command=self.full_scan)
        button_full_scan.pack(side=tk.LEFT, padx=10, pady=10)

        # Nhãn hiển thị trạng thái
        self.label_action_status = tk.Label(content_frame, text="Chưa có hành động nào được thực hiện.",
                                           font=("Helvetica", 12), bg='white', fg='gray')
        self.label_action_status.pack(pady=20)

    def scan_now(self):
        self.label_action_status.config(text="Đang quét ngay...")
        # Thêm các hành động khi nhấn nút "Quét ngay"

    def quick_scan(self):
        self.label_action_status.config(text="Đang quét nhanh...")
        # Thêm các hành động khi nhấn nút "Quét nhanh"

    def web_protection(self):
        self.label_action_status.config(text="Đang bảo vệ web...")
        # Thêm các hành động khi nhấn nút "Bảo vệ web"

    def simple_update(self):
        self.label_action_status.config(text="Đang cập nhật đơn giản...")
        # Thêm các hành động khi nhấn nút "Cập nhật đơn giản"

    def full_scan(self):
        self.label_action_status.config(text="Đang quét toàn bộ...")
        # Thêm các hành động khi nhấn nút "Quét toàn bộ"

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
