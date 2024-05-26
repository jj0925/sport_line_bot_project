import datetime
import matplotlib.pyplot as plt
import pyimgur

def add_weight_entry(user_input):
    weight_str = user_input.split(':')[1].strip()
    weight = float(weight_str)
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d)
    
    # 將數據存入字典
    weight_data[current_time] = weight
    return f"體重數據 {weight} 公斤 已存儲於 {current_time}"

def plot_weight_changes():
    # 獲取時間和體重數據
    times = list(weight_data.keys())
    weights = list(weight_data.values())
    
    # 繪製曲線圖
    plt.figure(figsize=(10, 5))
    plt.plot(times, weights, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.title('Your Weight Change')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # 儲存圖像到文件
    file_path = 'weight_changes.png'
    plt.savefig(file_path)
    # 轉換成url
    CLIENT_ID = "CLIENT_ID"
    PATH = "weight_changes.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link

