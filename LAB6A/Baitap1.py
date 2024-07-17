import tkinter as tk

class FPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng FPS")
        self.root.geometry("600x300")
        self.root.configure(bg='pink')

        self.create_widgets()

    def create_widgets(self):
        # Tạo và căn chỉnh khung chứa các thành phần chính
        main_frame = tk.Frame(self.root, bg='pink')
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Nhãn tiêu đề
        label_title = tk.Label(main_frame, text="Ứng dụng FPS", font=("Helvetica", 24), bg='pink')
        label_title.pack(pady=(0, 20))  # Đặt khoảng cách phía dưới

        # Đầu vào FPS
        fps_frame = tk.Frame(main_frame, bg='pink')
        fps_frame.pack(pady=(0, 10))

        label_fps = tk.Label(fps_frame, text="FPS:", font=("Helvetica", 14), bg='pink')
        label_fps.pack(side=tk.LEFT, padx=(0, 10))

        self.entry_fps = tk.Entry(fps_frame, font=("Helvetica", 14))
        self.entry_fps.pack(side=tk.LEFT)

        # Nút Tạm dừng, Bắt đầu, Kết thúc
        button_frame = tk.Frame(main_frame, bg='pink')
        button_frame.pack(pady=20)

        self.button_pause = tk.Button(button_frame, text="Tạm dừng", width=12, font=("Helvetica", 12), command=self.pause)
        self.button_pause.pack(side=tk.LEFT, padx=10)

        self.button_start = tk.Button(button_frame, text="Bắt đầu", width=12, font=("Helvetica", 12), command=self.start)
        self.button_start.pack(side=tk.LEFT, padx=10)

        self.button_stop = tk.Button(button_frame, text="Kết thúc", width=12, font=("Helvetica", 12), command=self.stop)
        self.button_stop.pack(side=tk.LEFT, padx=10)

        # Nhãn trạng thái
        self.label_status = tk.Label(main_frame, text="Trạng thái: Chưa bắt đầu", font=("Helvetica", 14), bg='pink')
        self.label_status.pack()

    def pause(self):
        self.label_status.config(text="Trạng thái: Đã tạm dừng")
        # Các xử lý khi nhấn nút Tạm dừng

    def start(self):
        fps = self.entry_fps.get()
        if fps.isdigit():
            self.label_status.config(text=f"Trạng thái: Đã bắt đầu với FPS = {fps}")
            # Các xử lý khi nhấn nút Bắt đầu với FPS được nhập
        else:
            self.label_status.config(text="Trạng thái: Vui lòng nhập số cho FPS")

    def stop(self):
        self.label_status.config(text="Trạng thái: Đã kết thúc")
        # Các xử lý khi nhấn nút Kết thúc

if __name__ == "__main__":
    root = tk.Tk()
    app = FPSApp(root)
    root.mainloop()
