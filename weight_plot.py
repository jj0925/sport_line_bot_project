import datetime
import matplotlib.pyplot as plt
import pyimgur

user_weight_data = {}

def add_weight_entry(user_id, user_input):
    global user_weight_data
    weight_str = user_input.split(':')[1].strip()
    weight = float(weight_str)
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d") 
    if user_id not in user_weight_data:
        user_weight_data[user_id] = {}    
    user_weight_data[user_id][current_time] = weight
    return f"體重數據 {weight} 公斤 已存儲於 {current_time}"

def plot_weight_changes(user_id):
    global user_weight_data
    times = list(user_weight_data[user_id].keys())
    weights = list(user_weight_data[user_id].values())
    
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
    try:
        uploaded_image = im.upload_image(PATH, title="Uploaded with Pyimgur")
        plt.clf()
        return uploaded_image.link
    except KeyError:
        plt.clf()
        return None

