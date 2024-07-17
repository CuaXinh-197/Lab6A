import tkinter as tk

def submit_data():
    # Lấy thông tin từ các Entry
    first_name = entry_firstname.get()
    last_name = entry_lastname.get()
    position = entry_position.get()
    age = entry_age.get()
    nationality = entry_nationality.get()
    
    # Tạo một cửa sổ mới để hiển thị thông tin
    info_window = tk.Toplevel()
    info_window.title("Thông tin người dùng")
    info_window.geometry("300x200")
    
    # Hiển thị thông tin người dùng trong cửa sổ
    tk.Label(info_window, text=f"Tên: {first_name}").pack()
    tk.Label(info_window, text=f"Họ: {last_name}").pack()
    tk.Label(info_window, text=f"Chức danh: {position}").pack()
    tk.Label(info_window, text=f"Tuổi: {age}").pack()
    tk.Label(info_window, text=f"Quốc tịch: {nationality}").pack()
    

def main():
    root = tk.Tk()
    root.title("Đăng ký thông tin")

    # Cấu hình kích thước cửa sổ
    root.geometry("500x400")

    # Khung thông tin người dùng
    frame_userinfo = tk.LabelFrame(root, text="Thông tin người dùng")
    frame_userinfo.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    tk.Label(frame_userinfo, text="Tên:").grid(row=0, column=0, sticky="w")
    tk.Label(frame_userinfo, text="Họ:").grid(row=1, column=0, sticky="w")
    tk.Label(frame_userinfo, text="Chức danh:").grid(row=2, column=0, sticky="w")
    tk.Label(frame_userinfo, text="Tuổi:").grid(row=3, column=0, sticky="w")
    tk.Label(frame_userinfo, text="Quốc tịch:").grid(row=4, column=0, sticky="w")

    global entry_firstname, entry_lastname, entry_position, entry_age, entry_nationality
    
    entry_firstname = tk.Entry(frame_userinfo)
    entry_firstname.grid(row=0, column=1, padx=5, pady=5)
    entry_lastname = tk.Entry(frame_userinfo)
    entry_lastname.grid(row=1, column=1, padx=5, pady=5)
    entry_position = tk.Entry(frame_userinfo)
    entry_position.grid(row=2, column=1, padx=5, pady=5)
    entry_age = tk.Entry(frame_userinfo)
    entry_age.grid(row=3, column=1, padx=5, pady=5)
    entry_nationality = tk.Entry(frame_userinfo)
    entry_nationality.grid(row=4, column=1, padx=5, pady=5)

    # Khung đăng ký
    frame_registration = tk.LabelFrame(root, text="Đăng ký")
    frame_registration.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    check_registration = tk.Checkbutton(frame_registration, text="Trạng thái đăng ký")
    check_registration.grid(row=0, column=0, padx=5, pady=5)
    spin_completed_courses = tk.Spinbox(frame_registration, from_=0, to=10, width=5)
    spin_completed_courses.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame_registration, text="Học kỳ:").grid(row=0, column=2, padx=5, pady=5)
    spin_semester = tk.Spinbox(frame_registration, from_=1, to=8, width=5)
    spin_semester.grid(row=0, column=3, padx=5, pady=5)

    # Khung Điều khoản và Điều kiện
    frame_terms = tk.LabelFrame(root, text="Điều khoản và Điều kiện")
    frame_terms.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    check_terms = tk.Checkbutton(frame_terms, text="Tôi chấp nhận các điều khoản và điều kiện")
    check_terms.pack(padx=5, pady=5)

    # Nút Gửi
    btn_submit = tk.Button(root, text="Gửi", command=submit_data)
    btn_submit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
