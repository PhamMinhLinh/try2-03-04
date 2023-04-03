import cv2
import pylivestream

# Thiết lập thông tin stream trên YouTube
stream_key = 'ptbs-s0rc-wdf1-tqkc-dkqd'  # Thay YOUR_STREAM_KEY bằng stream key của bạn trên YouTube
stream_url = 'rtmp://a.rtmp.youtube.com/live2/' + stream_key

# Thiết lập camera
cap = cv2.VideoCapture(0)

# Thiết lập stream
stream = pylivestream.FFMpegStream(stream_url, (640, 480))

# Bắt đầu stream
stream.start()

# Chạy vòng lặp để lấy hình ảnh từ camera và stream lên YouTube
while True:
    # Lấy khung hình từ camera
    ret, frame = cap.read()

    # Kiểm tra nếu không thể lấy được khung hình thì break khỏi vòng lặp
    if not ret:
        break

    # Hiển thị khung hình
    cv2.imshow('frame', frame)

    # Gửi khung hình lên YouTube
    stream.write(frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dừng stream và giải phóng bộ nhớ
stream.stop()
cap.release()
cv2.destroyAllWindows()
